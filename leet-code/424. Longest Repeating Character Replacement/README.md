# LeetCode

[424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

어려운 문제였다. 교재의 풀이를 최대한 이해하려고 했다.

교재에서는 최대 길이를 갱신하는 부분 없이 보다 효율적으로 최대 길이를 구할 수 있다고 했다. 

이를 더 상세히 이해하기 위해 첫번째 풀이에서는 최대 길이를 갱신하는 코드를 넣고, 두번째 풀이에서는 첫번째 풀이를 개선하면서 최대 길이를 갱신하는 코드도 제거했다.

<br>

문제의 주요 아이디어는 left 부터 right 범위를 한 문자로 채울 수 있으면 right 만 이동하고 그럴 수 없으면 left 도 함께 이동하는 것이다.

left 부터 right 를 한 문자로 채울 수 있는지 판단하기 위해 left 부터 right 의 범위가 가장 많이 나온 문자 하나와 k 를 더한 값보다 큰지 비교한다. k 횟수 만큼 문자를 변경할 수 있어서 가장 많이 나온 문자는 k 횟수만큼 더 늘어날 수 있다.

<br>

한 문자로 left 와 right 를 채울 수 있는 경우만 left 가 이동해서 범위를 좁히기 때문에 한 문자로 채울 수 있는한 left 는 증가하지 않는다. 그러다 한 문자로 채울 수 없으면 left 도 증가한다.

left 는 최대 1씩만 증가하기 때문에 한번 벌어진 right 와 left 의 간격은 좁혀지지 않는다. 따라서 기존에 구한 범위보다 더 큰 범위의 연속 문자가 나오지 않으면 left 와 right 의 범위는 유지된다. 별도로 최대 길이를 저장하는 변수를 사용할 필요가 없이 for 문을 마치고 right 와 left 사이의 길이를 구하면 된다.