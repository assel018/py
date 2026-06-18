# This is multiple inheritance: when one class is inherited from several classes at once. 
class Fly:
    def fly(self):
        print("Flying")

class Swim:
    def swim(self):
        print("Swimming")

class Duck(Fly, Swim):
    pass

duck = Duck()

duck.fly()   # Flying
duck.swim()  # Swimming