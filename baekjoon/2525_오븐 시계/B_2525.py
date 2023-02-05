hour, minute = list(map(int, input().split()))
cooking_time = int(input())

cooking_hour = (minute + cooking_time) // 60

finished_hour = (hour + cooking_hour) % 24
finished_minute = (minute + cooking_time) % 60

print(finished_hour, finished_minute)
