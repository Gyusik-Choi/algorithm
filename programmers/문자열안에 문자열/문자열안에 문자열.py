def solution(str1: str, str2: str):
    return 1 if str2 in str1 else 2


print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))
print(solution("ppprrrogrammers", "pppp"))
print(solution("AbcAbcA", "AAA"))
