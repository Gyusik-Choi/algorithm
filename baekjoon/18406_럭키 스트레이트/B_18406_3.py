N = list(map(int, input()))
half = len(N) // 2
print('LUCKY') if sum(N[:half]) == sum(N[half:]) else print('READY')

# 참고
# https://docs.python.org/3/whatsnew/2.5.html#pep-308-conditional-expressions
# https://m.blog.naver.com/wideeyed/221858874414
