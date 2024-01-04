from collections import defaultdict


def solution(genres, plays):
    genre_sums = defaultdict(int)
    music = defaultdict(list)

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        genre_sums[genre] += play
        music[genre].append([play, i])

    # genre_sums 를 value 를 기준으로 내림차순 정렬한 후
    # map 을 돌면서 key, value 중 key 만 남긴다
    most_played_genres = list(map(lambda x: x[0], sorted(genre_sums.items(), key=lambda x: -x[1])))

    for genre in most_played_genres:
        # 재생수 내림차순, 고유번호 오름차순
        music[genre].sort(key=lambda x: (-x[0], x[1]))

    answer = []

    for genre in most_played_genres:
        # 장르당 최대 2곡 까지 가능한데
        # 장르당 곡이 2개가 안 될 수 있어서
        # 인덱스 에러를 방지하기 위해
        # 장르별 최대 수록 가능한 곡인 2와
        # 장르별 곡의 수를 비교해서 더 작은 값으로 range 설정
        max_song = 2
        idx = min(max_song, len(music[genre]))
        for i in range(idx):
            answer.append(music[genre][i][1])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
