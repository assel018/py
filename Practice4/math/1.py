def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

N = 5

for square in square_generator(N):
    print(square)