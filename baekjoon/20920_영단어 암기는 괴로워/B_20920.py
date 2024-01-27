import sys
from collections import Counter


N, M = map(int, input().split())
words = list(filter(lambda x: len(x) >= M, [sys.stdin.readline().rstrip() for _ in range(N)]))
print(Counter(words).items())
sorted_dict = sorted(Counter(words).items(), key=lambda x: (-x[1], -(len(x[0])), x))
sys.stdout.write(''.join(list(map(lambda x: x[0] + "\n", sorted_dict))))
