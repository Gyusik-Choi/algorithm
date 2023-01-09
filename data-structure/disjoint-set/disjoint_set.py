def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] == x:
        return x
    else:
        return find_set(p[x])


def union(x, y):
    # x의 대표자, y의 대표자를 찾아야 한다
    p[find_set(y)] = find_set(x)


N = 8
p = [0] * (N + 1)
for i in range(1, N + 1):
    make_set(i)

union(1, 3)
union(2, 3)
union(5, 6)
union(6, 8)
union(1, 5)
union(6, 7)
print(p)
# [0, 2, 2, 1, 4, 2, 5, 2, 5]
# path compression 과의 차이는 요소 6에서 드러난다
# path compression 은 요소 6의 값이 2가 된다.
# 본 코드에서는 요소 6을 제외하고는 2번의 재귀를 돌지 않고 재귀 한번에 끝나서
# path compression 을 수행한 코드와 큰 차이가 나지 않을지 모르나
# find_set 연산에서 6은 재귀를 돌아 5로 가고 5에서 2를 리턴하게 된다.
# path_compression 이었다면 union(6, 7)을 수행하는 과정에서 요소 6의 값을 2로 바꾸겠지만
# 이 코드는 path compression 이 아니라서
# union 연산을 수행한 union(5, 6) 에 의해서 6은 5를 갖게 되고 union(6, 7)을 수행하더라도 요소 6의 값은 변하지 않는다.
