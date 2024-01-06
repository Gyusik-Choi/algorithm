def solution(wallpaper):
    wallpaper = list(map(lambda x: list(x), wallpaper))
    min_y = 51
    min_x = 51
    max_y = -1
    max_x = -1

    for i, paper in enumerate(wallpaper):
        for j, p in enumerate(paper):
            if p == '#':
                min_y = min(min_y, i)
                min_x = min(min_x, j)
                max_y = max(max_y, i)
                max_x = max(max_x, j)

    return [min_y, min_x, max_y + 1, max_x + 1]


print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))

