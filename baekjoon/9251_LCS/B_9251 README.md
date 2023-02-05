# 백준

## 9251

ACAYKP
CAPCAK

<br>

   C A P C A A K	 
A 0 1 1 1 1 1 1 
C 1 1 1 2 2 2 2
A 1 2 2 2 3 3 3
Y 1 2 2 2 3 3 3
K 1 2 2 2 3 3 4
P 1 2 2 2 3 3 4

<br>

세로 방향(i)의 글자를 기준으로 가로 방향(j)의 글자들을 하나씩 비교해 나간다. 

서로(세로와 가로) 같을때 위(dp|i - 1||j|) 아래(dp|i||j - 1|)에서 더 큰 수를 1 더하는게 아니라 대각선 방향으로 구하는 이유는 A C A 에서 C A P C A A K 의 C A P C A와 C A P C A A 를 통해 알 수 있다.

A C A에서 C A P C A 가 3이 됐는데 만약에 대각선 방향이 아니라 위나 아래에서 구하게 되면 3이 아니라 4가 된다. i의 길이가 정해진 상황에서 j만 커지는데 LCS의 값 자체는 j에서 또 다시 i와 같은게 나왔다고 하더라도 i의 최대치인 3보다 커질 수 없다.

서로 다를때는 위와 아래에서 더 큰 수를 dp|i||j| 값으로 해준다. 서로가 만나기 이전 상황(대각선)에서 1을 더할 필요가 없다.

세로의 AC, CAPCA를 기준으로 할때 AC의 C와 CAPCA의 A를 비교하는 상황이라고 하자. 일단 C와 A는 다르다. 이때 C와 A가 만나게 되는 과정은 진행방향에 따라서 가로의 CAPCA에서 세로의 A가 만난 다음에 세로의 C를 만나려는 상황이거나, 세로의 AC에서 가로의 CAPC의 C 이후에 CAPCA의 A를 만나려는 상황이다. 그러므로 최장 공통 부분 수열을 구하기 위해서 최대값을 가져와야 한다. 그래서 둘 중에서 더 큰 값을 선택한다.