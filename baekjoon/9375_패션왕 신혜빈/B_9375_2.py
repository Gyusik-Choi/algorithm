import sys


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        sys.stdout.write(str(0) + "\n")
    else:
        wardrobe = dict()
        for i in range(n):
            item_name, item_category = map(str, sys.stdin.readline().split())
            if item_category in wardrobe.keys():
                wardrobe[item_category] += 1
            else:
                wardrobe[item_category] = 1

        answer = 1
        for val in wardrobe.values():
            answer *= val + 1
        answer -= 1
        sys.stdout.write(str(answer) + "\n")
