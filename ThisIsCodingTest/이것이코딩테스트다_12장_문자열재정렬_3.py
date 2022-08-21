S = list(input())

characters = []
num_sum = 0

# 65 ~ 90
for idx, character in enumerate(S):
    if 65 <= ord(character) <= 90:
        characters.append(character)
    else:
        num_sum += int(character)

characters.sort()
print(''.join(characters) + str(num_sum))
