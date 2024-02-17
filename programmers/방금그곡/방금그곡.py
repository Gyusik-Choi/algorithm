def solution(m, musicinfos):
    # A# 을 A 로 바꾸면 안 돼서 소문자로 바꾼다
    # A# 과 A 는 다른데 A# 을 A 로 바꾸면
    # A# 과 A 를 구분할 수 없다
    def remove_sharp(melody):
        return (melody
                .replace("A#", "a")
                .replace("C#", "c")
                .replace("D#", "d")
                .replace("F#", "f")
                .replace("G#", "g"))

    def get_music_length(s, e):
        h1, m1 = list(map(int, s.split(":")))
        h2, m2 = list(map(int, e.split(":")))
        return (h2 * 60 + m2) - (h1 * 60 + m1)

    m = remove_sharp(m)
    musics = []

    for idx, music in enumerate(musicinfos):
        start, end, title, score = music.split(",")
        score = remove_sharp(score)
        music_length = get_music_length(start, end)
        score_length = len(score)

        if music_length > score_length:
            score = score * (music_length // score_length) + score[:music_length % score_length]
        else:
            score = score[:music_length]

        if m in score:
            musics.append([title, music_length, idx])

    if not musics:
        return "(None)"
    return sorted(musics, key=lambda x: (-x[1], x[2]))[0][0]


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
