import json
import urllib2
import threading

# Author: Matt Ankerson
# Date: 29 April 2015


class QueryCity(threading.Thread):
    METSERVICE_BASE = 'http://metservice.com/publicData/'
    LOCAL_FORECAST = 'localForecast'

    def __init__(self, city):
        threading.Thread.__init__(self)
        self.city = city
        self.forecast = {}

    def get_response(self, url):
        try:
            response = urllib2.urlopen(url)
        except urllib2.HTTPError:
            self.forecast = {}
        self.forecast = json.loads(response.read())

    def get_forecast(self):
        try:
            days = self.forecast["days"]
            today = days[0]
            weather_blurb = today["forecast"]
            return weather_blurb
        except TypeError:
            return "No forecast info"


if __name__ == "__main__":
    cities = ['dunedin', 'christchurch', 'wellington', 'auckland']
    forecasts = []
    # loop the cities array
    for city in cities:
        current = QueryCity(city)
        url = current.METSERVICE_BASE + current.LOCAL_FORECAST + city
        print(url)
        current.start()
        current.get_response(url)
        forecasts.append(current)

    for forecast in forecasts:
        forecast.join()
        formatted_city = forecast.city[0].upper() + forecast.city[1:]
        print(formatted_city + ": " + forecast.get_forecast())
