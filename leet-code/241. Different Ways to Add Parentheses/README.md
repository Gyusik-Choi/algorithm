# LeetCode

## [241. Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/)

### Python

어려운 문제였다. 교재의 풀이를 참고했다.

처음에는 조합을 생각했으나 조합과는 다르게 접근해야 했다. 이 문제와 조합 모두 재귀를 활용하며, 가능한 '경우의 수' 를 따져야 하는 공통점이 있으나 차이가 존재한다.

조합과 달리 요소의 순서가 바뀌는 것을 고려해야 한다. 이는 순열과 비슷하다고 볼 수 있으나 순열과도 차이가 있다. 조합과 순열은 하나씩 골라나가는데 반해 이 문제는 2개의 요소를 동시에 고려해야 할 수 있다.

<br>

```python
expression = "2*3-4*5"
```

```
((2*3)-(4*5))
```

expression 이 위와 같을 때 경우의 수가 (2, 3), (4, 5) 를 묶어서 생각하는 경우의 수가 있다. 그러나 이는 조합과 순열에서는 나올 수 없는 경우의 수다. 조합과 순열은 요소를 하나씩 골라가기 때문에 하나의 요소에 대한 순서만 고려할 수 있다.

<br>

분할 정복 유형의 문제라 재귀를 활용해서 풀이할 수 있다. 

리스트 슬라이싱을 통해 좌측, 우측으로 분할해서 범위를 좁혀 나간다. 좌측, 우측의 요소가 하나씩 남을 때까지 나눈 뒤에 좌측, 우측의 요소를 연산자와 함께 연산한 결과를 리턴한다. 

여기서 유의할 점은 결과를 담는 result 를 파라미터로 두지 않는다. result 를 파라미터로 두게 되면 모든 숫자와 연산자를 계산한 수가 아니라 중간 과정의 수도 포함되게 된다. result 를 파라미터로 두지 않고 함수 안의 변수로 두면서 결과를 상위 호출로 전달한다.

<br>

### Java

#### DifferentWaysToAddParentheses241

어려운 문제였다.

교재의 풀이와 다른 점은 교재는 expression 을 통채로 for 문을 돌면서 연산자를 기준으로 앞, 뒤를 구분한다. 반면에 이 풀이는 숫자와 연산자를 구분하고 숫자를 기준으로 재귀호출 한다.

<br>

#### DifferentWaysToAddParentheses241_2

교재의 풀이를 참고했다. DifferentWaysToAddParentheses241 에 메모이제이션 기법을 추가한 풀이다.

재귀호출을 하면서 동일한 연산을 반복적으로 하기 때문에 이를 개선하기 위해 메모이제이션을 사용한다. 별도의 해시맵을 두고 low 부터 high 까지의 숫자를 배열에서 잘라낸 후 문자열로 변환한 값을 해시맵의 키로 한다.

DifferentWaysToAddParentheses241 풀이가 교재와 달라서 해시맵의 키도 교재와 다르다. 교재는 expression 을 범위만큼 잘라서 재귀호출하기 때문에 expression 을 그대로 해시맵의 키로 사용할 수 있으나 DifferentWaysToAddParentheses241 풀이의 경우 numbers 는 그대로 있고 인덱스만 변화하기 때문에 키를 만들기 위해서는 numbers 에서 해당 범위의 숫자들만 따로 잘라내야 한다.

<br>

### Kotlin

#### DifferentWaysToAddParentheses241

어려운 문제였다. 교재의 풀이를 참고했다.

<br>

#### DifferentWaysToAddParentheses241_2

어려운 문제였다. 교재의 풀이를 참고했다. DifferentWaysToAddParentheses241 풀이에서 메모이제이션 기법을 추가해서 반복적인 계산을 개선했다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

https://www.baeldung.com/java-slicing-arrays

