# With functions - reusable code:

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# Return Values
def get_greeting():
  return "Hello from a function"    # When a function reaches a return statement, it stops executing and sends the result back. 

message = get_greeting()
print(message)

# Using the return value directly:
def get_greeting():
  return "Hello from a function"

print(get_greeting())
# If a function doesn't have a return statement, it returns None by default.

def no_return_function():
    print("This function has no return statement.")

result = no_return_function()
print(result)  # This will print "None"

# Return Values
# Functions can return values using the return statement:

def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

# Returning Different Data Types
# Functions can return any data type, including lists, tuples, dictionaries, and more.
# A function that returns a list:

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# A function that returns a tuple:

def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)
