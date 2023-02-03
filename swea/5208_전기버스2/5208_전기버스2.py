def back_track(idx, charge_num):
    global min_charge
    # 인덱스가 마지막 정류장 인덱스와 같거나 더 클때
    if idx >= station[-1]:
        if min_charge >= charge_num:
            min_charge = charge_num
        return
    # 충전 횟수가 최소 횟수를 넘어서면 종료(최소값이 필요하므로 재귀를 더 돌지 않고 종료)
    if charge_num > min_charge:
        return
    else:
        for j in range(idx + battery[idx], idx, -1):
            idx = j     # 인덱스
            charge_num += 1     # 충전 횟수
            back_track(idx, charge_num)
            idx -= j    # 이 코드는 있어도 되고 없어도 된다. 안 빼줘도 위의 idx = j에 의해서 j 값이 초기화 된다. 기존 방식처럼 +=이 아니라 =이므로 따로 빼주지 않아도 된다.
            charge_num -= 1     # 충전 횟수를 빼준다


T = int(input())
for t in range(1, T + 1):
    battery = list(map(int, input().split()))
    station = list(range(1, battery[0] + 1))
    for i in range(len(station)):
        station[i] -= 1
    battery.pop(0)
    min_charge = 1000000
    back_track(0, 0)
    print("#{} {}".format(t, min_charge - 1))
