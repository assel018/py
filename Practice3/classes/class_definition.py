# Python Classes/Objects
# Create a class named MyClass, with a property named x:

class MyClass:
  x = 5


# Create Object
# Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)


# Delete Objects
# You can delete objects by using the del keyword:
del p1



# Multiple Objects
# You can create multiple objects from the same class:

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

# Note: Each object is independent and has its own copy of the class properties.

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Person:
  pass
