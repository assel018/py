names = ["Alice", "Bob", "Charlie"]
ages = [20, 21, 22]

# enumerate
for index, name in enumerate(names):
    print(index, name)

# zip
for name, age in zip(names, ages):
    print(name, age)

# Type conversions
x = "100"

print(int(x))
print(float(x))
print(str(200))
print(list("Python"))
print(tuple([1, 2, 3]))