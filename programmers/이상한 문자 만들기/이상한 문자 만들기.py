def solution(s):
    return ' '.join(list(map(lambda word: ''.join(list(map(lambda w: w[1].upper() if not w[0] % 2 else w[1].lower(), enumerate(word)))), s.split(' '))))


print(solution("try hello world"))

# 참고
# https://bobbyhadz.com/blog/python-map-with-index
