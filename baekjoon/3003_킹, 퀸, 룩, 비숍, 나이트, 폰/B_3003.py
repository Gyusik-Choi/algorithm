pieces = list(map(int, input().split()))
right_pieces = [1, 1, 2, 2, 2, 8]

answer = []

for idx, piece in enumerate(pieces):
    answer.append(str(right_pieces[idx] - piece))

print(' '.join(answer))
