# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

# Example
# Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
# Note: The else block will NOT be executed if the loop is stopped by a break statement.