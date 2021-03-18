# 데이터의 개수 n과 부분 연속 수열의 합 m을 입력 받기
n = 10
m = 15
data = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]

cnt = 0
sums = 0
start = 0
end = 0


# for start in range(n):
#     while sums < m and end < n:
#         sums += data[end]
#         end += 1
#
#     if sums == m:
#         cnt += 1
#     sums -= data[start]

# 위의 코드는 동빈나 님의 코드다
# 이 코드 그대로 공부해도 되겠지만
# 조금 더 투 포인터를 이해해보고자 코드를 바꿔보기로 했다
# 우선 start 와 end 를 한번에 while 문에 넣고 싶었다

# while start < n or end < n:
#     if sums == m:
#         cnt += 1
#         sums -= data[start]
#         start += 1
#     elif sums > m:
#         sums -= data[start]
#         start += 1
#     else:
#         sums += data[end]
#         end += 1

# 위 코드에서는 start 8, end 10, sums 10, cnt 2의 상황에서
# end 는 끝까지 갔으나 기준 합인 15 보다 작아서 end 에 해당하는 인덱스의 값을 더하고 end 의 값을 1 증가시켜야 한다
# 그러나 end 는 이미 10이기 때문에 data 의 인덱스를 초과했는데 값을 더하려고 하니 에러가 난다
# start 와 end 가 모두 n 보다 작을 때까진 계속 반복을 돌아야 하지만
# end 가 끝까지 갔다면 end 는 더 이상 돌지 않도록 해야 한다
# 그래서 while start < n and end < n 조건으로는 구하기 어렵다

# while start < n or end < n:
#     if sums == m:
#         cnt += 1
#         sums -= data[start]
#         start += 1
#     elif sums > m:
#         sums -= data[start]
#         start += 1
#     else:
#         if end < n:
#             sums += data[end]
#             end += 1
#         else:
#             sums -= data[start]
#             start += 1

# 이렇게 하면 가능하긴 하지만 그러면 while 문의 조건을 건 의미가 없어진다

# 아래와 같은 방법으로 start 만 while 을 도는 방식으로 변경했다
# 조건문은 sums 와 m 의 대소관계를 통해 3가지로 나눴다.
# sums 보다 m 이 큰 경우에만 추가 조건문을 통해 end 가 n 보다 작은지 체크했고
# end 가 n 보다 작으면 아직 end 는 끝까지 가지 않은 상태라 값을 더해줘도 된다
# 그러나 end 가 n 과 같거나 n 보다 더 크면 이미 끝까지 가서 data 의 인덱스를 초과한 상황이다
# 이때부터는 sums 가 m 보다 작더라도 start 인덱스를 늘리고 sums 에서 start 인덱스의 값을 줄여나간다
# 그러면서 기준 합을 구할 수 있는지 체크해보고 start 도 끝까지 가면 while 문이 종료되면서 끝난다
# 다만 코드의 중복이 있다
# sums == m 인 경우와 sums > m 인 경우에 공통적으로 sums -= data[start] 와 start += 1 을 수행하므로
# 이를 중복되지 않게 줄일 수 있다

# while start < n:
#     if sums < m:
#         if end < n:
#             sums += data[end]
#             end += 1
#         else:
#             sums -= data[start]
#             start += 1
#     elif sums == m:
#         cnt += 1
#         sums -= data[start]
#         start += 1
#     else:
#         sums -= data[start]
#         start += 1
# print(cnt)

# 아래처럼 sums < m 만 아니면 (sums == m 이거나 sums > m 이면)
# sums -= data[start] 와 start += 1은 수행한다
# 다만 이를 수행하기 전에 sums == m 인지만 체크해서 맞으면 cnt 를 1 더해준다
# 이를 통해서 코드의 중복과 길이를 줄일 수 있다

while start < n:
    if sums < m:
        if end < n:
            sums += data[end]
            end += 1
        else:
            sums -= data[start]
            start += 1
    else:
        if sums == m:
            cnt += 1
        sums -= data[start]
        start += 1

print(cnt)

# 참고
# https://www.youtube.com/watch?v=rI8NRQsAS_s