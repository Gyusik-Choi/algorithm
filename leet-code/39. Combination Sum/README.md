# LeetCode

## 39. Combination Sum

### Python

#### 첫번째 풀이

조합을 구하는 문제로 [이 문제](https://leetcode.com/problems/combinations/) 와 유사한 유형이다.

다만 이번 문제는 자기 자신은 중복될 수 있다는 점이 다르다. 기존의 조합은 자기 자신의 중복 없이 경우의 수를 구해야 하는데 이번 문제는 자기 자신은 중복되도 된다.

재귀 호출시 다음 인덱스가 아니라 현재 인덱스를 포함해서 자기 자신부터 다시 탐색될 수 있도록 한다.

<br>

#### 두번째 풀이

첫번째 풀이와는 재귀 호출 방법만 다르고 나머지는 동일하다.

재귀 호출 앞, 뒤로 append, pop 없이 재귀 호출할 때 + 연산자를 통해 리스트에 요소를 추가한다.

시간과 메모리 성능은 첫번째 풀이보다 조금 떨어지지만 코드가 간결하다.

|        | 시간   | 메모리    |
| ------ | ---- | ------ |
| 첫번째 풀이 | 57ms | 16.3MB |
| 두번째 풀이 | 63ms | 16.4MB |

<br>

### Java & Kotlin

#### CombinationSum39

재귀를 활용했다.

자신이 반복될 수 있어서 현재 인덱스를 재귀 호출의 인자로 넣어서 다음 재귀 호출에서도 자기 자신을 추가할 수 있도록 한다. 

무한대로 재귀 호출하지 않도록 재귀 탈출 조건으로 조합의 합이 target 이 넘으면 종료하고, 조합의 합이 target 과 같으면 조합 목록에 추가하고 종료한다.

<br>

#### CombinationSum39_2

CombinationSum39 와 동일한 방식으로 풀이했다.

자바에서 코틀린으로 풀이하면서 조합의 합을 stream 을 이용하지 않고 collection 함수인 sum 으로 구했고, 리스트에서 마지막 요소를 제거할 때 removeLast 함수를 사용했다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰