from unittest import TestCase


def solution(orders, course):
    def get_combination(cnt, cnt_limit, idx, order, comb):
        if cnt == cnt_limit:
            menu = ''.join(comb)
            if menu in menu_candidate[cnt_limit]:
                menu_candidate[cnt_limit][menu] += 1
            else:
                menu_candidate[cnt_limit][menu] = 1
            return

        for i in range(idx, len(order)):
            comb.append(order[i])
            get_combination(cnt + 1, cnt_limit, i + 1, order, comb)
            comb.pop()

    # { 단품 메뉴 갯수: { 메뉴: 갯수 } }
    menu_candidate = dict()

    for c in course:
        menu_candidate[c] = dict()

    for o in orders:
        # orders 의 각 원소는 오름차순 정렬되지 않았을 수 있다
        # 정답을 담은 배열의 각 원소는 오름차순 정렬되야 한다
        # orders 가 ["XYZ", "XWY", "WXA"] 인 경우
        # 원소를 오름차순 정렬하지 않으면 XW, WX 가 각각 1개씩 나온다
        # 오름차순 정렬을 통해 WX 2개를 구할 수 있도록 해야 한다
        o = ''.join(sorted(list(o)))
        for c in course:
            get_combination(0, c, 0, o, [])

    menus = []

    for c in course:
        sorted_menu_items = sorted(menu_candidate[c].items(), key=lambda x: -(x[1]))

        if not sorted_menu_items:
            continue

        # 가장 많이 주문한 메뉴 갯수와 일치하는 메뉴는 한 개가 아니라 여러개일 수 있다
        max_ordered_menu = sorted_menu_items[0][1]
        # 가장 많이 주문한 메뉴 갯수와 일치하면서 최소 2명 이상의 손님이 주문한 메뉴
        filtered_menu_items = list(filter(lambda x: x[1] == max_ordered_menu and x[1] >= 2, sorted_menu_items))
        selected_menu = list(map(lambda x: x[0], filtered_menu_items))
        menus.extend(selected_menu)

    return sorted(menus)


class SolutionTest(TestCase):
    def test_solution(self):
        answer = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
        self.assertEqual(answer, ["AC", "ACDE", "BCFG", "CDE"])

    def test_solution2(self):
        answer = solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
        self.assertEqual(answer, ["ACD", "AD", "ADE", "CD", "XYZ"])

    def test_solution3(self):
        answer = solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
        self.assertEqual(answer, ["WX", "XY"])
