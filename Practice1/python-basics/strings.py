# 1. Python Strings
# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
# A single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.
a = "Hello, World!"
print(a[1])

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
  print(x)

# String Length
# To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

# Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")


# 2. Slicing Strings
b = "Hello, World!"
print(b[2:5])         # Get the characters from position 2 to position 5 (not included):

# Slice From the Start 
b = "Hello, World!"
print(b[:5])         # Get the characters from the start to position 5 (not included):  

# Slice To the End 
b = "Hello, World!"
print(b[2:])        # Get the characters from position 2, and all the way to the end:


# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])      # Get the characters: From: "o" in "World!" (position -5). To, but not included: "d" in "World!" (position -2):

# 3. Modify Strings 
# Upper Case
a = "Hello, World!"
print(a.upper())     # The upper() method returns the string in upper case:

# Lower Case
a = "Hello, World!"
print(a.lower())     # The lower() method returns the string in lower case:


# Remove Whitespace
a = " Hello, World! "
print(a.strip())     # The strip() method removes whitespace from both sides of the string:

# Replace String
a = "Hello, World!"
print(a.replace("Hello", "Hi"))  # The replace() method replaces a string with another string:

# Split String
a = "Hello, World!"
print(a.split(","))  # The split() method splits a string into a list.

# 4. String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # String concatenation using the + operator

# 5. Format - Strings
age = 36
txt = "My name is John, I am " + age    # This will produce an error:
print(txt)

# But we can combine strings and numbers by using f-strings or the format() method!
# F-Strings
""" F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
To specify a string as an f-string, simply put an f in front of the string literal, 
and add curly brackets {} as placeholders for variables and other operations.
"""
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"   # Add a placeholder for the price variable:
print(txt)

""" A placeholder can include a modifier to format the value.
A modifier is included by adding a colon : 
followed by a legal formatting type, like .2f which means fixed point number with 2 decimals: """
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


txt = f"The price is {20 * 59} dollars"
print(txt)


# 5. Escape Characters
# txt = "We are the so-called "Vikings" from the north."
print(txt)  # This will produce an error because of the double quotes inside the string.

txt = "We are the so-called \"Vikings\" from the north."
print(txt) # The escape character allows you to use double quotes when you normally would not be allowed:

#   Code	            Result	
" \' "                 # Single Quote	
" \\ "                 # Backslash	
" \n "	               # New Line	
" \r "	               # Carriage Return	
" \t "	               # Tab	
" \b "	               # Backspace	
" \f "	               # Form Feed	
" \ooo "	           # Octal value	
" \xhh "	           # Hex value	


# 6. String Methods
a = " Hello, World! "
# Method                     Description
a.capitalize()	           # Converts the first character to upper case
a.casefold()	           # Converts string into lower case
a.center()	               # Returns a centered string
a.count()	               # Returns the number of times a specified value occurs in a string
a.encode()	               # Returns an encoded version of the string
a.endswith()	           # Returns true if the string ends with the specified value
a.expandtabs()	           # Sets the tab size of the string
a.find()	               # Searches the string for a specified value and returns the position of where it was found
a.format()	               # Formats specified values in a string
a.format_map()	           # Formats specified values in a string
a.index()	               # Searches the string for a specified value and returns the position of where it was found
a.isalnum()	               # Returns True if all characters in the string are alphanumeric
a.isalpha()	               # Returns True if all characters in the string are in the alphabet
a.isascii()	               # Returns True if all characters in the string are ascii characters
a.isdecimal()	           # Returns True if all characters in the string are decimals
a.isdigit()	               # Returns True if all characters in the string are digits
a.isidentifier()	       # Returns True if the string is an identifier
a.islower()	               # Returns True if all characters in the string are lower case
a.isnumeric()	           # Returns True if all characters in the string are numeric
a.isprintable()	           # Returns True if all characters in the string are printable
a.isspace()	               # Returns True if all characters in the string are whitespaces
a.istitle()	               # Returns True if the string follows the rules of a title
a.isupper()	               # Returns True if all characters in the string are upper case
a.join()	               # Joins the elements of an iterable to the end of the string
a.ljust()	               # Returns a left justified version of the string
a.lower()	               # Converts a string into lower case
a.lstrip()	               # Returns a left trim version of the string
a.maketrans()	           # Returns a translation table to be used in translations
a.partition()	           # Returns a tuple where the string is parted into three parts
a.replace()	               # Returns a string where a specified value is replaced with a specified value
a.rfind()	               # Searches the string for a specified value and returns the last position of where it was found
a.rindex()	               # Searches the string for a specified value and returns the last position of where it was found
a.rjust()	               # Returns a right justified version of the string
a.rpartition()	           # Returns a tuple where the string is parted into three parts
a.rsplit()	               # Splits the string at the specified separator, and returns a list
a.rstrip()	               # Returns a right trim version of the string
a.split()	               # Splits the string at the specified separator, and returns a list
a.splitlines()	           # Splits the string at line breaks and returns a list
a.startswith()	           # Returns true if the string starts with the specified value
a.strip()	               # Returns a trimmed version of the string
a.swapcase()	           # Swaps cases, lower case becomes upper case and vice versa
a.title()	               # Converts the first character of each word to upper case
a.translate()	           # Returns a translated string
a.upper()	               # Converts a string into upper case
a.zfill()	               # Fills the string with a specified number of 0 values at the beginning


