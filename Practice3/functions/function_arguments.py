# Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Parameters vs Arguments
""" 
From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.

"""

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument


# Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")   # If your function expects 2 arguments, you must call it with exactly 2 arguments.

# Default Parameter Values
def my_function(name = "friend"): # If the function is called without an argument, it uses the default value:
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")


# Default value for country parameter:

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Keyword Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy") # You can send arguments with the key = value syntax.


# This way, with keyword arguments, the order of the arguments does not matter.

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")
 

# Positional Arguments
def my_function(animal, name):  # When you call a function with arguments without using keywords, they are called positional arguments.

  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

# The order matters with positional arguments:
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")

# Mixing Positional and Keyword Arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)


# Passing Different Data Types
"""
You can send any data type as an argument to a function (string, number, list, dictionary, etc.).

The data type will be preserved inside the function:

Example
Sending a list as an argument:
"""

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# Sending a dictionary as an argument:
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments.

# To specify positional-only arguments, add , / after the arguments:
def my_function(name, /):  # , /
  print("Hello", name)

my_function("Emil")


# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(name):
  print("Hello", name)

my_function(name = "Emil")  # =


# With , /, you will get an error if you try to use keyword arguments:
def my_function(name, /):  # , /
  print("Hello", name)

my_function(name = "Emil")  # =

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, name):   # * 
  print("Hello", name)

my_function(name = "Emil")  # =


# Without ( *, ), you are allowed to use positional arguments even if the function expects keyword arguments:
def my_function(name):
  print("Hello", name)

my_function("Emil")


# With ( *, ) , you will get an error if you try to use positional arguments:

def my_function(*, name):  # *
  print("Hello", name)

my_function("Emil")


# Combining Positional-Only and Keyword-Only
# Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)


