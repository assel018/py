# 1. Elif Statement
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


# Multiple Elif Statements
score = 75
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")


# Categorizing age groups:
age = 25
if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")


# Day of the week checker:
day = 3
if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")




# 2. Else Statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# Else Without Elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# Checking even or odd numbers:
number = 7
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

# Complete If-Elif-Else Chain
# Temperature classifier:
temperature = 22
if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")


# Else as Fallback
# Validating user input:
username = "Emil"
if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

