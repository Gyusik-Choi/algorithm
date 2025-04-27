# LeetCode

## 46. Permutations

### Python

#### 46_permutations

순열을 구하는 문제다.

중첩 함수를 이용해서 재귀적으로 구했다.

<br>

### Java

#### Permutations46

파이썬이나 코틀린과 달리 자바는 중첩 함수를 사용할 수 없어서 별도의 private 함수를 이용해서 재귀적으로 순열을 구했다.

<br>

#### Permustaions46_2

Permutations46 과 동일한 방법이지만 세부 구현만 조금 다르게 풀이했다. 

Permutations46 에서는 요소의 사용 여부를 관리하는 별도의 배열을 사용하지 않는 대신 요소의 사용 여부를 perm 을 순차 탐색하면서 찾았다.

Permutations46_2 에서는 요소의 사용 여부를 관리하는 별도의 배열을 사용하고 요소의 사용 여부를 배열에 대한 인덱스 접근으로 찾았다.

<br>

### Kotlin

#### Permutations46

Permutations46 와 풀이 방법은 같으나 중첩함수를 활용해서 풀이했다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

