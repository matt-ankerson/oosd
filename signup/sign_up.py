import cherrypy
import requests

# Author: Matt Ankerson
# Date: 20 May 2015

# This is a micro-service intended to receive new details/credentials from a user
# and send them off to the user directory for storage.


class SignUpService(object):
    exposed = True  # expose all methods

    # force the responses content-type to be text/plain
    @cherrypy.tools.accept(media='application/json')
    def GET(self, email="", password="", screen_name=""):
        # validate the new user
        if email == "" or password == "" or screen_name == "":
            return '{"response":"invalid"}'
        else:
            return '{"response":"valid"}'

    # A sample request to the above ^^ function would be as follows:
    # r = s.get('http://127.0.0.1:8080/', headers={'Accept':'application/json'},
    #               params={'email':'yoyo@yoyo', 'password':'yoyo', 'screen_name':'yoyo'})

    def POST(self, email="", password="", screen_name=""):
        s = requests.Session()
        pay_load = {'email': email, 'password': password, 'screen_name': screen_name}
        # create a request to the user module for storage of a new user
        r = s.post("url to user directory", data=pay_load)
        if r.status_code == requests.codes.ok:
            return '{"response":"success"}'
        else:
            return '{"response":"error: "' + str(r.status_code) + '"}'

    # use session.post to call the POST function

# switch from the default mechanism of matching URLs to methods
# for one that is aware of the whole HTTP method shenanigan with: MethodDispatcher()
if __name__ == "__main__":
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.quickstart(SignUpService(), '/', conf)