# LeetCode

## 1. Two Sum

2차 for 문을 사용하면 O(N^2) 시간 복잡도가 발생한다. 

O(N) 으로 풀이할 수 있는 방법이 있어서 해당 방법으로 풀이했다.

for 문을 돌면서 딕셔너리에 각 원소를 키로 원소의 인덱스를 값으로 해서 넣는다. 그리고 다시 for 문을 돌면서 target 에서 원소를 뺀 값이 딕셔너리에 있고 이 값을 딕셔너리의 키로 조회한 값이 해당 for 문의 인덱스와 같지 않다면 정답이 된다.

여기서 target 에서 원소를 뺀 값을 딕셔너리의 키로 조회한 값이 해당 for 문의 인덱스와 같지 않은지를 비교하는 이유는 자기 자신을 조회할 경우를 피하기 위해서다. 예를 들어 target 이 10 이고 num 이 5라고 하면 num 과 target - num 이 같은 값이 된다. 이런 경우를 피하려고 해당 비교를 추가한다.

처음에 target 에서 원소를 뺀 값을 입력으로 주어진 nums 리스트에서 찾으려고 했는데 이 보다 딕셔너리에서 찾는게 훨씬 빠르다. 배열에서 in 으로 찾으려면 O(N) 시간 복잡도가 필요한데 딕셔너리에서 in 으로 찾으면 O(1) 로 알 수 있다.

<br>

<참고>

파이썬 알고리즘 인터뷰

