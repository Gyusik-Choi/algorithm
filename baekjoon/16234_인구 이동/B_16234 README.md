# 백준

## 16234

이것이 코딩테스트다 교재에 수록된 문제며 bfs로 풀이했다.

시간 초과가 발생하던 부분은 인구 이동을 위해 별도의 함수에서 모든 국가를 for 문으로 돌면서 인구 이동 가능한 국가 여부를 체크해서 이동을 했는데, 이 부분이 비효율적이었다. 인구 이동 가능한 국가 여부를 bfs 함수에서 판단하면서 이동 가능한 국가 정보를 갖는 배열에 넣고 인구 이동을 실시할때는 모든 국가를 돌지 않아도 되고 배열에 들어간 국가만 변경해주면 된다. 

pypy3만 통과했고 python3도 통과를 해보려했으나 계속 시간초과가 발생중이다. 그러나 일단은 추가적으로 해당 문제를 python3로 통과하려는 시도는 더 안하려고 한다. 로직 자체는 크게 변화 없이 시간 초과에 걸리지 않으려는 코드만을 작성하고 있다고 느꼈다. 함수 호출을 줄이고 전역 코드 위주로 작성하거나, 변수에 할당한 값을 할당하지 않고 사용하는 등의 코드를 작성하고 있었다.

그럼에도 불구하고 python3로 통과하지 못한건 아쉬움이 남는다.