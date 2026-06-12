# Python Numbers
x = 5       # int
y = 3.14    # float
z = 2 + 3j  # complex

# Python type() Function
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

# Int or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))


x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

# Complex numbers are written with a "j" as the imaginary part:

x = 1j
y = complex(1, 1)
z = 3 + 4j
print(type(x))
print(type(y))
print(type(z))

# Type Conversion. You can convert from one type to another with the int(), float(), and complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number. Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
# Import the random module, and display a random number from 1 to 9:
import random
print(random.randrange(1, 10))

