# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

# Example
# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Note: The else block will NOT be executed if the loop is stopped by a break statement.

# Example
# Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")







# Nested Loops
# A nested loop is a loop inside a loop.

# The "inner loop" will be executed one time for each iteration of the "outer loop":

# Example
# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

# Example

for x in [0, 1, 2]:
  pass
