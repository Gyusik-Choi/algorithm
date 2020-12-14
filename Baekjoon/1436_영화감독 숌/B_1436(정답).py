N = int(input())
num = 666
while N > 0:
    # 666부터 1씩 더해가면서 666이 포함된 가장 작은 수를 계속해서 찾아나간다
    if "666" in str(num):
        N -= 1
    num += 1

print(num - 1)

# 참고
# https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-1436%EB%B2%88-%EC%98%81%ED%99%94%EA%B0%90%EB%8F%85-%EC%88%8C-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
