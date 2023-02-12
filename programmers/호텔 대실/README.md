# 프로그래머스

## 호텔 대실

문제를 풀이하려는 아이디어는 맞게 도출했으나, 시간을 비교하는 부분에서 간과한 점이 있어서 통과하는데 오래 걸린 문제다.

문제의 아이디어는 아래와 같다.

```
시작 시간이 짧은 순서로 정렬하고
종료 시간이 가장 짧은 방으로 예약한다.
이게 안 되면 새로운 방에 예약한다.
```

<br>

간과한 점은 50분 + 10분은 60분이면서 동시에 시를 1 더해줘야 한다는 점이다.

```python
def get_room(rooms, room_seeker):
    for i, room in enumerate(rooms):
        if room.end_hour < room_seeker.start_hour:
            rooms[i] = room_seeker
            return rooms

        if room.end_hour == room_seeker.start_hour:
            if room.end_minute + 10 <= room_seeker.start_minute:
                rooms[i] = room_seeker
                return rooms

    rooms.append(room_seeker)
    return rooms
```

<br>

위 로직은 문제가 있다.

위 로직에서는 room.end_hour < room_seeker.start_hour 일때는 무조건 room_seeker 을 해당 room 에 넣는데 이는 옳지 않다.

13시 55분과 14시 4분을 비교하면 물론 room.end_hour < room_seeker.start_hour 자체는 맞지만 문제 조건에 따르면 10분을 더한 시간과 비교해야 한다.

13시 55분에 10분을 더하면 14시 5분인데 이때는 14시 4분 보다 크기 때문에 room_seeker 를 해당 room 에 넣을 수 없다.

그래서 계산을 좀더 편하게 하기 위해 시와 분을 따로 비교하는 대신 시 * 60 + 분 을 통해 분으로 합산한 값으로 바꾸는 방법이 있다.

<br>

<참고>

https://leejams.github.io/%ED%98%B8%ED%85%94%EB%8C%80%EC%8B%A4/

