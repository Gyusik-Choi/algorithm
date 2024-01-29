import sys
from collections import defaultdict


n = int(sys.stdin.readline().rstrip())
work_record = defaultdict(str)

for _ in range(n):
    name, record = sys.stdin.readline().split()
    work_record[name] = record

working_people = list(filter(lambda x: x[1] == 'enter', work_record.items()))
sorted_working_people = sorted(working_people, key=lambda x: x[0], reverse=True)
sys.stdout.write(''.join(list(map(lambda x: x[0] + "\n", sorted_working_people))))

