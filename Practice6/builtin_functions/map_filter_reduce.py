from functools import reduce
numbers = [1, 2, 3, 4, 5] 
print("Length:", len(numbers)) 
print("Sum:", sum(numbers)) 
print("Min:", min(numbers)) 
print("Max:", max(numbers)) 
# map 
print(list(map(lambda x: x * 2, numbers))) 
# filter 
print(list(filter(lambda x: x % 2 == 0, numbers))) 
# reduce 
print(reduce(lambda x, y: x + y, numbers)) 
# sorted 
print(sorted([5, 1, 9, 3]))