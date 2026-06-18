# Create a Parent Class
# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


# Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

# Example
# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
  pass



    
# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# Add Properties
# Example
# Add a property called graduationyear to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019


# In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:

# Add a year parameter, and pass the correct year when creating objects:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

