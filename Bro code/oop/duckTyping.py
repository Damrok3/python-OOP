# Duck typing = concept where the class of an object is less important thatn the methods/attributes
#               class type is not checked if minumum methods/attributes are present
#               "If it walks like a duck, and it quacks like a duck, then it must be a duck"

class Duck:
    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is quacking")

class Chicken:
    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken is clucking")

class Person():
    def catch(self, object):
        object.walk()
        object.talk()
        print("you caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)