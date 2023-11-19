from collections import defaultdict


def find_min_height_trees(n, edges):
    if n == 1:
        return [0]

    nodes = defaultdict(list)

    for a, b in edges:
        nodes[a].append(b)
        nodes[b].append(a)

    leaves = []

    # 리프 노드를 찾는다
    # 이 for 문을 while 문 안으로 넣고 싶었으나 넣을 수 없었다
    #
    # 여기는 리프 노드 제거가 없기 때문에
    # 전체 for 문을 돌면서 리프 노드를 찾을 수 있는데
    # while 문 안에는 리프 노드 제거가 있어서
    # for 문을 도는 과정에서 리프 노드 후보 값의 길이가 0이 될 수 있기 때문에
    # 리프 노드 제거한 후에 바로 길이를 봐야 한다
    for i in range(n + 1):
        if len(nodes[i]) == 1:
            leaves.append(i)

    while n > 2:
        n -= len(leaves)

        new_leaves = []

        for leaf in leaves:
            # 서로의 연결을 끊는다
            # 리프 노드의 값을 제거해서 빈 리스트로 만들고
            # 제거한 리프 노드의 값이 자신의 값으로 갖던 리프 노드를 제거한다
            #
            # 키 leaf 값의 길이가 1이라 pop 을 통해
            # nodes[left] 를 빈 리스트로 만든다
            # 키 left 값에서 pop 으로 꺼낸 노드가
            # 자신의 값으로 갖던 leaf 를 제거한다
            neighbor = nodes[leaf].pop()
            nodes[neighbor].remove(leaf)

            # 남은 for 문이 돌면서 len(nodes[neighbor]) 이 0이 될 수 있어서
            # len(nodes[neighbor]) 이 1인 경우 미리 new_leaves 에 담는다
            if len(nodes[neighbor]) == 1:
                new_leaves.append(neighbor)

        leaves = new_leaves

    return leaves


# print(find_min_height_trees(4, [[1, 0], [1, 2], [1, 3]]))
# print(find_min_height_trees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
print(find_min_height_trees(6, [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]))
