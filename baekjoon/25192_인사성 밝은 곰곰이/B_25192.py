import sys
from functools import reduce

N = int(sys.stdin.readline())
# rstrip('\n') 으로 개행문자 제거
chats = [sys.stdin.readline().rstrip('\n') for _ in range(N)]
print(' '.join(chats).split('ENTER'))
# 'ENTER' 를 기준으로 나누고 ENTER 는 '' 처럼 빈 문자열로 리스트에 남아서 제거하기 위해 filter 함수 사용
chats_split_by_enter_with_no_empty_string = list(filter(lambda x: x != '', ' '.join(chats).split('ENTER')))
# 위에서 ' '.join 으로 묶고 split('ENTER') 를 하면서 리스트의 각 문자열 요소의 앞 뒤로 한 칸씩 공백이 생긴다
# ex> ['', ' abc def '] (여기서 '' 는 'ENTER' 였던 문자열이 split('ENTER') 에 의해 빈 문자열만 남음)
# strip() 으로 문자열 요소의 앞 뒤 공백을 제거하고
# set 에 담아서 중복 요소를 제거하고 요소의 갯수를 구한다
sums_per_chat = list(map(lambda x: len(set(x.strip().split())), chats_split_by_enter_with_no_empty_string))
# reduce 로 누적합 구한다
print(reduce(lambda acc, cur: acc + cur, sums_per_chat))
