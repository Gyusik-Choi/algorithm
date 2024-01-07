def solution(today, terms, privacies):
    terms_info = dict()
    for term in terms:
        term_type, term_expiration = term.split()
        terms_info[term_type] = int(term_expiration)

    answer = []
    t_year, t_month, t_day = list(map(int, today.split('.')))
    t_total = (t_year * 12 * 28) + (t_month * 28) + t_day

    for idx, privacy in enumerate(privacies):
        p_start, p_type = privacy.split()
        p_year, p_month, p_day = list(map(int, p_start.split('.')))
        p_total = (p_year * 12 * 28) + ((p_month + terms_info[p_type]) * 28) + p_day

        if t_total >= p_total:
            answer.append(idx + 1)

    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
print(solution("2020.01.01", ["A 12"], ["2018.12.1 A", "2019.01.01 A", "2019.01.02 A"]))
print(solution("2020.01.01", ["A 24"], ["2018.12.1 A", "2019.01.01 A", "2019.01.02 A"]))

# 참고
# https://magentino.tistory.com/61
