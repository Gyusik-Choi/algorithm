import sys
sys.stdin = open("input.txt", "r")


def check(card):
    s = list()
    d = list()
    h = list()
    c = list()
    double = []
    for i in range(0, len(card), 3):
        double.append(card[i:i + 3])
        if card[i:i + 1] == 'S':
            s.append(card[i + 1:i + 3])
        elif card[i:i + 1] == 'D':
            d.append(card[i + 1:i + 3])
        elif card[i:i + 1] == 'H':
            h.append(card[i + 1:i + 3])
        else:
            c.append(card[i + 1:i + 3])
    double_check = set(double)
    # 겹치는게 있다면 ERROR 리턴
    if len(double) != len(double_check):
        return "ERROR"
    # 겹치는게 없다면 무늬별로 몇 장 없는지 파악
    else:
        ans = list()
        ans.append(str(13 - len(s)))
        ans.append(str(13 - len(d)))
        ans.append(str(13 - len(h)))
        ans.append(str(13 - len(c)))
        return ans


T = int(input())
for t in range(1, T+1):
    cards = input()
    short = check(cards)
    if short == "ERROR":
        print("#{} {}".format(t, short))
    else:
        print("#{} {}".format(t, ' '.join(short)))
