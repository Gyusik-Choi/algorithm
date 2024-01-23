# 프로그래머스

## 큰 수 만들기

다른 분들의 풀이를 보면서 스택을 활용하는 문제임을 알았고 [이 문제](https://school.programmers.co.kr/learn/courses/30/lessons/154539)가 떠올랐다.

스택에 작은 수가 있으면 스택의 숫자를 제거하는 방법은 생각을 했지만 k 개 만큼만 빼면서 가장 큰 수를 어떻게 보장할 수 있을지는 파악하지 못했다.

k 개 만큼만 빼기 위해서는 while 문에 k 가 1이상인지 체크하는 조건을 넣으면 된다. 그리고 앞 자리에 가장 큰 숫자를 두기 때문에 가장 큰 수를 보장할 수 있다. 

앞자리 숫자가 커야 더 큰 숫자다. 이 풀이는 k 개 만큼 빼면서 현재 숫자보다 스택에 작은 숫자가 있으면 모두 제거해서 앞자리에 가장 큰 숫자를 둘 수 있도록 한다.

<br>

<참고>

https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%81%B0-%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

https://wellsw.tistory.com/205

https://school.programmers.co.kr/learn/courses/30/lessons/154539