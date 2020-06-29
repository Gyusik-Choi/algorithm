import sys
sys.stdin = open("input.txt", "r")


def check(nums_arr):
    # 길이가 1이거나 혹은 2이상인 숫자 중에서 단조 증가하는 수로 거른다.
    cut = []
    for j in nums_arr:
        if len(str(j)) == 1:
            cut.append(j)
        elif len(str(j)) > 1:
            j = str(j)
            for k in range(len(j) - 1):
                if int(j[k]) > int(j[k + 1]):
                    break
            else:
                cut.append(int(j))
    # 거르고나서 cut 배열에 아무것도 없으면 -1, 하나라도 있으면 max 값 리턴.
    if len(cut) > 0:
        answer = max(cut)
        return answer
    else:
        return -1


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    nums = []
    # 붙어있는 두개의 수가 아니라 모든 숫자를 비교
    for i in range(1, len(arr) - 1):
        # 인덱스에서 실수하지 말자. i가 아니라 i + 1이어야 한다. i면 숫자가 중복된다.
        for l in range(i + 1, len(arr)):
            num = arr[i] * arr[l]
            nums.append(num)
    print("#{} {}".format(t, check(nums)))
