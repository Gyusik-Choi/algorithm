from collections import defaultdict


def can_finish(num_courses, pre_requisites):
    node = defaultdict(list)

    for [s, e] in pre_requisites:
        node[s].append(e)

    # 방문 검사
    visited = [False] * num_courses

    def dfs(start, temp_route):
        if temp_route[start]:
            return False

        # 위의 temp_route[start] 조건문 보다
        # visited[start] 조건문이 먼저 나오면 안 된다
        # temp_route[start] 조건문으로
        # 사이클 발생 여부를 알 수 있다
        # 사이클이 발생한 경우
        # temp_route[start] 에 걸려서
        # return False 를 해야 하는데
        # visited[start] 가 먼저 나오면
        # visited[start] 를 만족하게 돼서
        # return True 를 하게 된다
        if visited[start]:
            return True

        visited[start] = True
        temp_route[start] = True

        for end in node[start]:
            if not dfs(end, temp_route):
                return False

        temp_route[start] = False
        return True

    # dictionary 가 변경되는 경우
    # RuntimeError: dictionary changed size during iteration
    # 위와 같은 에러가 발생한다
    # 에러를 방지하기 위해
    # iteration 을 할 때 list 로 감싸서
    # 복사본을 생성하여 iteration 을 한다
    # 변수 node 는 defaultdict 로 되어 있는데
    # dfs 함수 안의 for 문인 node[start] 에서
    # start 의 key 가 없을 경우 key error 가 발생하지 않고
    # 기본 값으로 지정한 list 에 의해
    # key 로 start 가 추가되고
    # value 로 빈 list 가 생성된다
    # dictionary 의 크기가 변하기 때문에
    # dictionary 가 변하는 것과 관계 없이
    # 복사해둔 dictionary 로 iteration 을 하면
    # 원본의 크기가 변하는 것과 관계 없이 고정된 크기로
    # iteration 을 할 수 있다
    for key in list(node):
        if not dfs(key, [False] * num_courses):
            return False

    return True


print(can_finish(2, [[1, 0]]))
print(can_finish(2, [[1, 0], [0, 1]]))
