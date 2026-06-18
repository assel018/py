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


# Add Methods
# Example
# Add a method called welcome to the Student class:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.



# Add the __init__() Function
""" 
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Note: The __init__() function is called automatically every time the class is being used to create a new object.
"""
# Add the __init__() function to the Student class:
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)


# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

