def solution(begin, target, words):
    inf = float('inf')
    min_change = inf

    def back_track(start, end, cnt, visited):
        nonlocal min_change

        # 탈출 조건 1 -> 최소 갯수를 넘음
        # 탈출 조건 2 -> target 찾음

        if min_change < cnt:
            return

        if start == end:
            min_change = min(min_change, cnt)
            return

        for idx, word in enumerate(words):
            if visited[idx]:
                continue

            if not is_can_change(start, word):
                continue

            visited[idx] = True
            back_track(word, end, cnt + 1, visited)
            visited[idx] = False

        if min_change == inf:
            return 0
        return min_change

    def is_can_change(one, two):
        difference_cnt = 0

        for idx, char_one in enumerate(one):
            char_two = two[idx]

            if char_one != char_two:
                difference_cnt += 1

        if difference_cnt == 1:
            return True
        return False

    return back_track(begin, target, 0, [False] * len(words))


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
