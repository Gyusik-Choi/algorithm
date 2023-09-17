a, b, c = sorted(list(map(int, input().split())))
if a + b > c:
    print(a + b + c)
else:
    print(2 * (a + b) - 1)

# 참고
# https://mathbang.net/92#gsc.tab=0
# https://velog.io/@iwtkmn0219/%EB%B0%B1%EC%A4%80-Python-14215%EB%B2%88-%EC%84%B8-%EB%A7%89%EB%8C%80
