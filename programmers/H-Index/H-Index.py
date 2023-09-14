def more_or_equal_cited_article(citations, num):
    return len(list(filter(lambda x: x >= num, citations)))


def solution(citations):
    max_cite_num = max(citations)

    # h편 이상의 논문이 h번 이상 인용과
    # n - h 편 이하의 논문이 h번 이하 인용이 맞아야 한다
    for cite in range(max_cite_num, -1, -1):
        # 인용 횟수 이상 인용된 논문 수 >= 인용 횟수
        if more_or_equal_cited_article(citations, cite) >= cite:
            return cite


print(solution([3, 0, 6, 1, 5]))
