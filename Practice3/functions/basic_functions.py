# Creating a Function
def my_function():
  print("Hello from a function") # In Python, a function is defined using the def keyword, followed by a function name and parentheses:
# This creates a function named my_function that prints "Hello from a function" when called.



# Calling a Function
def my_function():
  print("Hello from a function") 
my_function()  # To call a function, write its name followed by parentheses. 





def my_function():
  print("Hello from a function")
my_function()
my_function()
my_function() # You can call the same function multiple times. 



# Function Names
def calculate_sum():
  print("This is calculate_sum")

def _private_function():
  print("This is a private function")

def myFunction2():
  print("This is myFunction2")



# Why Use Functions?
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

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