N = int(input())

# 공통규칙
rules = ['0666', '1666', '2666', '3666', '4666', '5666', '6660', '6661', '6662', '6663', '6664', '6665', '6666',
         '6667', '6668', '6669', '7666', '8666', '9666']
cycle = N // 19
rules_num = N % 19 - 1
if rules_num == -1:
    rules_num = 18
    cycle -= 1

ans = str(cycle) + rules[rules_num]
print(ans.lstrip("0"))