class Time:
    def __init__(self, s_hour=None, s_minute=None, e_hour=None, e_minute=None):
        self.start_hour = s_hour
        self.start_minute = s_minute
        self.end_hour = e_hour
        self.end_minute = e_minute


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


def get_sorted_book_time(book_time):
    new_book_time = []

    for idx, book in enumerate(book_time):
        start, end = book

        s_hour, s_minute = map(int, start.split(':'))
        e_hour, e_minute = map(int, end.split(':'))

        new_book_time.append(Time(s_hour, s_minute, e_hour, e_minute))

    return sorted(new_book_time, key=lambda x: (x.start_hour, x.start_minute, x.end_hour, x.end_minute))


def solution(book_time):
    sorted_book_time = get_sorted_book_time(book_time)

    rooms = []

    for i, time in enumerate(sorted_book_time):
        rooms = get_room(sorted(rooms, key=lambda x: (x.end_hour, x.end_minute)), time)

    return len(rooms)


# 시작 시간이 짧은 순서로 정렬하고
# 종료 시간이 가장 짧은 방으로 예약한다
# 그게 안 되면 새로운 방에 예약한다

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
# print(solution([["15:00", "17:00"], ["17:10", "18:00"]]))
# print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))
# print(solution([["09:10", "10:10"], ["10:20", "12:20"], ["12:30", "13:20"]]))

# 참고
# https://velog.io/@shininghyunho/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%98%B8%ED%85%94-%EB%8C%80%EC%8B%A4
