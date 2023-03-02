N = int(input())
homes = list(map(int, input().split()))
homes.sort()
print(homes[N // 2] if N % 2 else homes[N // 2 - 1])
