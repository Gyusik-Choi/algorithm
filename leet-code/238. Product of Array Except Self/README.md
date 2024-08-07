# LeetCode

## 238. Product of Array Except Self

나눗셈 연산을 사용하면 안돼고 O(n) 에 풀이해야 한다는 제약조건이 있는 문제다. 그래서 nums 의 모든 요소를 곱한 값에서 각 인덱스에 해당하는 값을 나누는 방식으로는 풀이할 수 없다.

본인을 제외한 나머지 값의 곱이기 때문에 본인을 제외한 양쪽의 곱을 각각 구해서 서로 곱하는 방식을 사용할 수 있다.

예를 들어 [1, 2, 3, 4] 가 입력으로 주어지면 2의 경우 왼쪽의 1과 오른쪽의 3, 4를 곱한 12를 서로 곱해주면 되고 3의 경우 왼쪽의 1, 2를 곱한 2와 오른쪽의 4를 곱해주면 된다.

이를 구현하기 위해 두번의 for 문으로 풀이할 수 있다. 첫번째 for 문은 왼쪽에서 오른쪽으로 돌고 두번째 for 문은 오른쪽에서 왼쪽으로 돈다. 자신을 제외한 왼쪽 부분을 구하기 위해 첫번째 for 문을 돌고 자신을 제외한 오른쪽 부분을 구하기 위해 두번째 for 문을 돈다.

첫번째 for 문을 돌기 위해 값을 누적해나갈 변수 p 를 1로 설정한다. 첫번째 for 문의 첫번째 요소는 본인의 왼쪽에 값이 없다. 오른쪽의 값들과 곱해질 수 있도록 1로 설정한 변수 p의 값이 본인의 왼쪽 값이 된다. 정답을 담는 리스트 answer 에 1인 p 를 넣는다. 두번째 요소는 본인의 왼쪽에 첫번째 요소가 있다. 첫번째 요소를 구하기 위해 p 에서 첫번째 요소를 곱한 값을 answer 에 넣는다. 세번째 요소는 본인의 왼쪽에 첫번째, 두번째 요소가 있다. 이미 첫번째 요소는 이미 p와 곱해졌기 때문에 두번째 요소와 p 를 곱한 값을 answer 에 넣는다. 이런 식으로 첫번째 for 문을 돌면서 answer 에 값을 넣는다.

두번째 for 문을 돌기 위해 값을 누적해나갈 변수 p 를 첫번째 for 문과 마찬가지로 1로 설정한다. 두번째 for 문은 역순으로 돈다. 마지막 요소의 경우 본인의 오른쪽에 값이 없다. 왼쪽의 값들과 곱해질 수 있도록 1인 p가 본인의 오른쪽 누적 곱이 되는데 이때 answer 에 기존에 들어간 마지막 인덱스 값과 곱해주면 자신의 왼쪽 누적 곱과 자신의 오른쪽 누적 곱을 곱한 값을 구할 수 있다. 

마지막 요소의 다음 요소 (마지막에서 한 칸 왼쪽) 가 본인의 오른쪽 누적 곱을 구할 수 있도록 1인 p와 본인을 곱해서 (p = p * 마지막 요소) p를 갱신한다. 마지막에서 한 칸 왼쪽 요소의 경우 본인의 오른쪽에 마지막 요소가 있다. 앞서 구한 p와 a본인의 인덱스의 answer 값을 곱하면 자신을 제외한 나머지 왼쪽과 오른쪽의 누적곱이 된다. 이렇게 두번째 for 문을 돌고나면 answer 의 값을 모두 구하게 되고 최종적으로 answer 를 리턴한다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

