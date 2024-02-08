import sys
from collections import defaultdict


N, M = map(int, sys.stdin.readline().split())
never_heard_seen = defaultdict(int)

for _ in range(N):
    never_heard = sys.stdin.readline().rstrip()
    never_heard_seen[never_heard] += 1

for _ in range(M):
    never_seen = sys.stdin.readline().rstrip()
    never_heard_seen[never_seen] += 1

never_heard_seen_items = sorted(list(filter(lambda x: x[1] == 2, never_heard_seen.items())))

sys.stdout.write(str(len(never_heard_seen_items)) + "\n")
for item in never_heard_seen_items:
    sys.stdout.write(item[0] + "\n")
