# 백준

## 2156

[2579 계단 오르기][https://www.acmicpc.net/problem/2579] 문제와 유사한 문제다.

처음에 2579 문제를 풀었던 방법을 그대로 사용했더니 오답이 나왔다. 2579 문제에서 조금 더 추가해야할 조건들이 존재하는 문제다.

우선은 2579는 맨 마지막 계단을 반드시 밟아야 했다. 그래서 정답도 맨 마지막 계단을 밟았을때를 기준으로 최대값을 찾아내야 한다. 그러나 본 문제인 [2156 포도주 시식][https://www.acmicpc.net/problem/2156]은 이와 달리 맨 마지막 잔을 마셔야하는 조건이 없고 마실 수 있는 최대량을 찾으면 되는 문제다.

문제에서 예제로 주어진 입력인

```
6
6
10
13
9
8
1
```

이를 2579 문제 방식대로 dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i]) 해당 코드를 활용(dp 배열이 답을 답는 배열이고 wine 배열은 각 잔 별로 담긴 포도주의 양을 나타냄)해서 풀이하면 dp 배열은 [6, 16, 23, 28, 33, 32] 이렇게 나온다. 즉 마지막 잔을 마시는게 최대량을 보장해주지 못한다.

그래서 위의 dp 배열처럼 33 다음에 32가 나왔을 경우에는 33으로 바꿔주는 식으로 풀이해나갔다. 큰 뼈대로 dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i]) 이를 활용하되, if dp[i] < dp[i - 1]의 경우에는 dp[i] = dp[i - 1] 이렇게 현재까지 마신 최대량을 이전 잔까지 마신 최대량 값으로 바꿔주었다.

이렇게 해도 가능한 이유는, dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i]) 이 코드를 보면 dp[i] 값이 이전 잔의 값을 보는 것은 dp[i - 1]이 아니라 wine[i - 1]이다.

위에서 6번째 잔까지의 최대값인 32를 5번째 잔까지의 33으로 바꿔줬다고 하고서 7번째 잔이 있다고 할때 바라보게 되는 6번째 잔의 값은 dp 배열의 값이 아니라 wine 배열이다. 누적된 최대값이 아니라 6번째 잔의 포도주 양을 본다. 그래서 이렇게 5번째 잔의 값을 6번째 잔의 값으로 넣어주어도 무방하다. 8번째 잔의 경우에 영향을 줄 수 있지 않냐고 생각할 수도 있겠지만 8번째 잔과 6번째 잔은 연속된 잔이 아니라서 6번째 잔까지 최대량을 구해놓고 8번째 잔을 바라봐야 한다.

이 조건이 필요한 또 다른 이유는 0의 존재다. 문제에서 포도주의 양은 1000이하의 음이 아닌 정수라고 했다. 이 말은 0도 포함될 수 있다는 뜻이다. 만약에 0이 주어진다고 하면

예를 들어,

```
7
6
10
13
9
8
1
0
```

이런 입력이 있다고 했을 때 6번째 잔까지의 값을 5번째 잔까지의 값으로 교체하지 않으면 [7, 10, 16, 23, 28, 33, 32, 32] 이렇게 될 것이다. 그리고 8, 9 번째 잔이 있다고 하면 8번째 잔이 보게 되는 dp[i - 2]도 32가 되므로 옳지 않다.

<br>

추가적으로 주의할 점은, 4번째 잔부터 위의 조건이 대입 가능하므로 3번째 잔까지는 n의 입력 숫자에 따라서 직접 하드코딩 했다. 3번째 잔까지의 최대값은 3번째 잔이 0일 수 있기 때문에 1번째 잔과 2번째 잔의 합이 될 수 있다. 이를 처음에 고려하지 못해서 계속 오답이 났다.