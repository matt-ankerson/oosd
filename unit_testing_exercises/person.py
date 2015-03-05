# Matt Ankerson
class Person:

    # constructor
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 45
        self.dead = False

    # change this persons name
    def change_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # increment this persons age
    def increment_age(self):
        self.age = self.age + 1
        return self.age

    # kill this person
    def kill(self):
        self.dead = True
