def solution(names):
    return [names[i] for i in range(0, len(names), 5)]


print(solution(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]))
print(solution(["nami", "ahri", "jayce", "garen"]))
