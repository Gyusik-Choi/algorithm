S = list(input())

characters = []
numbers = 0

for i, char in enumerate(S):
    if 'A' <= char <= 'Z':
        characters.append(char)
        continue

    numbers += int(char)

print(''.join(sorted(characters)) + str(numbers))
