import sys


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        sys.stdout.write(str(0) + "\n")
    else:
        wardrobe = []
        for i in range(n):
            item_name, item_category = map(str, sys.stdin.readline().split())
            wardrobe.append([item_name, item_category])
        wardrobe = sorted(wardrobe, key=lambda x: x[1])

        # 의상의 종류 총 개수
        category_cnt = 1
        # 각 의상 종류별 수
        per_category_cnt = []
        per_cnt = 1
        last_category = wardrobe[0][1]
        if n > 1:
            for i in range(1, n):
                item_n, item_c = wardrobe[i][0], wardrobe[i][1]
                if last_category != item_c:
                    category_cnt += 1
                    per_category_cnt.append(per_cnt)
                    per_cnt = 1
                    last_category = item_c
                else:
                    per_cnt += 1
        # 마지막 남은 per_cnt
        per_category_cnt.append(per_cnt)

        answer = 1
        if n > 1:
            for i in range(category_cnt):
                answer *= per_category_cnt[i] + 1
            answer -= 1
        sys.stdout.write(str(answer) + "\n")
