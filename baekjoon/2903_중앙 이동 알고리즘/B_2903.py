N = int(input())
dot = 3

while N > 1:
    dot += dot - 1
    N -= 1

print(dot ** 2)
