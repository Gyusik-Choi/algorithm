def solution(today, terms, privacies):
    t_year, t_month, t_day = list(map(int, today.split('.')))
    terms_info = dict()
    for term in terms:
        term_type, term_expiration = term.split()
        terms_info[term_type] = int(term_expiration)

    answer = []
    for idx, privacy in enumerate(privacies):
        p_start, p_type = privacy.split()
        p_year, p_month, p_day = list(map(int, p_start.split('.')))

        month_sums = p_month + terms_info[p_type]
        # 1 ~ 12는 0이 나와야 하고
        # 13 ~ 24는 1이 나와야 한다
        # 1을 뺀 값에서 12를 나누면 된다
        add_year = (month_sums - 1) // 12

        p_year += add_year
        # 1 ~ 12 로 month 값을 바꾼 후에 13 으로 나눈 나머지를 구한다
        p_month = (month_sums - (12 * add_year)) % 13

        if t_year > p_year:
            answer.append(idx + 1)
            continue

        if t_year == p_year and (t_month > p_month or (t_month == p_month and t_day >= p_day)):
            answer.append(idx + 1)

    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
print(solution("2020.01.01", ["A 12"], ["2018.12.1 A", "2019.01.01 A", "2019.01.02 A"]))
print(solution("2020.01.01", ["A 24"], ["2018.12.1 A", "2019.01.01 A", "2019.01.02 A"]))

# 참고
# https://velog.io/@bweb/Python%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4-%EC%88%98%EC%A7%91-%EC%9C%A0%ED%9A%A8%EA%B8%B0%EA%B0%84
