# LeetCode

## 121. Best Time to Buy and Sell Stock

O(N) 으로 풀이하기 위해 고민한 문제다. 단순히 for 문으로 최대값, 최소값을 구한 다음 최대값에서 최소값을 빼는 방식은 안 된다. 최대값은 최소값 보다 뒤에 있어야 한다.

for 문을 돌면서 최소값을 계속 구하고, 현재 for 문의 요소에서 최소값을 뺀 값의 최대값을 구한다. for 문의 현재 요소에서 최소값을 빼면 현재 요소가 최소값과 같은 인덱스이거나 뒤의 인덱스인게 보장된다. 

최소값이 갱신되면 for 문의 현재 요소와 같은 인덱스고 최소값이 갱신되지 않으면 for 문의 현재 요소보다 앞의 인덱스 값이다.

<br>

### Java 풀이

#### BestTimeToBuyAndSellStock121

기존의 min 보다 더 작은 값이 나오면 max 와 min 모두 갱신한다.

이전의 값은 어차피 팔 수 없기 때문에 현재 값을 기준으로 더 큰 profit 이 나올 수 있는지 봐야 한다.

max 보다 더 큰 값이 나오면 max 를 갱신하고, profit 과 max - min 를 비교해서 max - min 가 더 크다면 profit 을 갱신한다.

<br>

기존 profit 과 비교하지 않고 바로 profit 을 max - min 으로 갱신하면 안 된다.

기존의 min 보다 더 작은 값이 나와서 min 이 갱신되면 max 도 함께 갱신된다. 이후 max 보다 큰 값이 나오면 max - min 을 하는데 이 값이 기존의 profit 보다 작을 수 있어서 Math.max 로 둘 중 큰 값을 profit 으로 설정한다.

<br>

#### BestTimeToBuyAndSellStock121_2

교재의 풀이를 참고했고 이 풀이가 BestTimeToBuyAndSellStock121 보다 훨씬 간결하다.

minPrice 의 최소값을 계속 갱신하면서 profit 도 계속 갱신한다.

<br>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰



