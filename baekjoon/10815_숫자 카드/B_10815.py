import sys
from collections import Counter


N = int(sys.stdin.readline())
nums_info = Counter(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
print(*list(map(lambda x: 1 if x in nums_info else 0, list(map(int, sys.stdin.readline().split())))))
