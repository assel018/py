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