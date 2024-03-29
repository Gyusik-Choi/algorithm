# 프로그래머스

## 2개 이하로 다른 비트

완전 탐색으로 하나씩 문제 조건에 맞는 큰 수를 찾으려 했으나 시간 초과가 발생했다.

<br>

다른 분들의 풀이를 살펴보니 접근을 아예 다르게 했어야 했다.

완전 탐색으로 찾는 방법이 아니라 주어진 숫자를 이진수 기준으로 문제의 조건에 맞게 더 큰 숫자로 직접 변환하고 이를 다시 십진수 숫자로 변환해야 한다.

짝수의 경우 이진수로 바꾸면 가장 작은 자리 수가 항상 0이다. 그래서 이 0을 1로 바꿔주면 비트가 1개가 다르면서 해당 숫자보다 큰 숫자를 구할 수 있다. 이진수로 변환하고 다시 십진수로 변환하는 과정 없이 1 만 더해주면 된다.

홀수의 경우 비트가 1개 다른 숫자를 구할 수도 있지만 2개 다른 숫자가 더 가까운 큰 수라서 비트 2개가 다른 숫자를 구한다. 비트가 1개 다른 숫자를 구하려면 이진수로 변환한 값에서 0을 찾고 0을 1로 바꿔주면 된다. 1로 바꾼 자리 보다 한 칸 작은 자리 수를 0으로 바꿔주면 더 작으면서 홀수로 변환한 숫자보다는 큰 수를 구할 수 있다.

예를 들어 9를 이진수로 변환하면 1001이다. 여기서 가장 오른쪽에 있는 0을 찾아서 1로 변환하면 1011이 된다. 그리고 1로 변환한 자리 보다 한 칸 작은 자리의 수를 0으로 바꾸면 1010이 된다. 이를 다시 십진수로 바꾸면 10이 된다.

만약에 9를 위에서처럼 비트 2개가 다른 수가 아니라 비트 1개가 다른 수로 바꾸면 1011이 되는데 이는 십진수로 바꾸면 11이다. 11보다 10이 더 작기 때문에 10이 정답이 된다.

<br>

이진수에서 0을 찾아야 한다고 했는데 0이 없을 수 있다. 이를 대비해서 아예 맨 앞에 0을 붙여서 0을 찾으면 0을 항상 찾을 수 있다. 원래 0이 없는 숫자였다면 맨 앞에 붙여준 0을 찾게 된다.

<br>

이진수로 변환하고, 십진수로 변환하는 코드를 직접 구현해서도 해보았는데 내장 함수를 쓰는게 훨씬 더 빨랐다.

<br>

<참고>

https://velog.io/@kerri/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Lv2-2%EA%B0%9C-%EC%9D%B4%ED%95%98%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EB%B9%84%ED%8A%B8

https://prgms.tistory.com/57

https://ye0nn.tistory.com/28

