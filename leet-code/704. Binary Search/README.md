# LeetCode

## [704. Binary Search](https://leetcode.com/problems/binary-search/)

이진 탐색을 구현하는 문제다.

<br>

### Python

#### 첫번째 풀이

파이썬에서 이진 탐색을 사용할 수 있는 bisect 모듈이 있다. 이 모듈에 bisect_left, bisect_right 메소드가 있는데 이 중 bisect_left 메소드를 참고해서 첫번째 풀이를 풀이했다.

bisect_left 메소드는 찾으려는 숫자가 여러개일 경우 가장 첫번째 인덱스를 리턴한다. 

이 메소드에서 주의할점은 찾으려는 숫자가 없는 경우도 값을 리턴하고 리턴 값이 리스트의 길이를 넘어갈 수도 있어서 주의해야 한다.

소스코드를 보면 lo, hi 변수를 이용해 while 문으로 이진탐색을 하는데 hi 변수의 값이 리스트의 길이로 되어있다. 만약에 찾으려는 값이 리스트에 있는 최대값 보다 더 큰 경우 리스트의 길이가 리턴된다. 이 값으로 리스트를 조회하면 잘못된 인덱스로 에러가 발생한다.

리턴 값이 리스트에서 조회할 수 있는 인덱스 범위를 벗어났는지 검사하고, 인덱스 범위를 벗어나지 않았다면 해당 인덱스 값이 실제로 찾으려는 값과 일치하는지 확인해야 한다.

<br>

구현한 코드는 while 문 내부에서 값을 찾으면 low 에 mid 값을 할당하고 break 문으로 바로 while 문을 빠져나왔다. while 문 밖에서는 low 인덱스에 있는 리스트 값이 찾으려는 값과 다를 수 있어서 같지 않은 경우 -1을 리턴하고 같은 경우만 low 를 리턴한다.

<br>

#### 두번째 풀이

교재의 풀이를 참고했다.

첫번째 풀이와 달리 while 문을 low 가 high 보다 작거나 같은 경우 반복한다. 

그리고 while 문 안에서 값을 찾으면 mid 를 리턴하고 mid 의 값보다 target 이 작으면 high 에 mid - 1을 할당한다.

<br>

### Java

#### BinarySearch704

while 문을 사용해서 반복 구조로 풀이했다.

<br>

```java
int mid = low + (high - low) / 2;
```

mid 를 구할 때 (low + high) / 2 가 아니라 위의 방법으로 풀이했다. low + high 를 했을 때 int 의 범위를 넘는 오버플로우가 발생할 수 있어서 위와 같이 구했다.

<br>

```java
int mid = (low + high) >>> 1
```

위와 같은 방법도 가능하다. 위의 경우 부호 비트로 쓰이는 최상위 비트도 함께 비트 이동을 하기 때문에 오버플로우 영향을 받지 않고 구할 수 있다.

[스택오버플로우](https://stackoverflow.com/questions/19058859/what-does-mean-in-java) 에 자세한 설명이 나와 있는데 오버플로우가 발생할 경우 최상위 비트가 1로 되면서 음수가 될 수 있는데 이때 2로 나누면 몫은 음수가 된다. 그런데 2로 나누는게 아니라 >>> 연산자 (>> 가 아니다) 를 사용해서 비트 연산을 하면 최상위 비트도 비트를 이동하기 때문에 음수가 아닌 양수가 된다.

연산자 >>> 는 가능한데 >> 는 안되는 이유는 >> 의 경우 빈자리를 0으로 채우는게 아니라 최상위 비트의 값으로 채우기 때문에 최상위 비트가 1이라 음수인 경우 1로 채워진다. 

여기서 빈자리는 shift 를 하면서 밀린 자릿수만큼 새로 채워야할 자릿수를 의미한다. 예를 들어 11100 에서 우측으로 비트를 2칸 이동하면 00이 밀려서 없어진다. 111 앞에 두 자릿수를 채워야 하는데 이때 채워야할 자릿수 2개가 빈자리다. 빈자리를 0으로 채우면 00111 이고, 빈자리를 1로 채우면 11111이 된다. 

<br>

#### BinarySearch704_2

재귀를 활용해서 풀이했다.

left 가 right 보다 작거나 같을 때까지 재귀를 이어나간다. mid 인덱스의 값보다 target 이 크면 left 를 mid + 1 로 재귀호출하고, mid 인덱스의 값보다 target 이 작으면 high 를 mid - 1 로 재귀호출한다.

<br>

<참고>

파이썬 알고리즘 인터뷰

https://github.com/python/cpython/blob/v3.9.0/Lib/bisect.py

자바 알고리즘 인터뷰

https://github.com/python/cpython/blob/3.11/Lib/bisect.py

https://research.google/blog/extra-extra-read-all-about-it-nearly-all-binary-searches-and-mergesorts-are-broken/

https://stackoverflow.com/questions/19058859/what-does-mean-in-java

https://park-youjin.tistory.com/17