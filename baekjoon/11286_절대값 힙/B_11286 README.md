# 백준

## 11286

heapq 모듈을 이용한 방식과 최소힙을 클래스로 구현한 방식으로 2가지 풀이를 했다. 공통적으로 sys 모듈을 사용해서 입출력의 속도를 높이려 했다.

<br>

### heapq 모듈

heapq 모듈을 활용한 방식에서는 절대값을 기준으로 정렬이 되어야해서 heap에 넣어줄 때 (절대값으로 변환한 값, 기존값) 형태로 튜플을 넣어줬다.

abs() 메서드는 인자로 넣어준 값 자체를 변환하는게 아니라 변환한 값을 새로 던져준다.

```python
num = -1
abs_num = abs(num)

print(abs_num)
# 1
print(num)
# -1
```

<br>

### 최소힙 클래스

heapq 모듈을 이용했을때처럼 숫자를 추가할때 절대값으로 변환한 값과 기존값을 [절대값으로 변환한 값, 기존값] 이렇게 배열로 넣어줬다.

값을 넣을때는 절대값을 기준으로 힙을 정렬하되 부모 노드의 절대값이 자식 노드의 절대값 보다 큰 경우 뿐만 아니라 같은 경우도 고려해야 한다. 같을 경우에는 기존값이 부모 노드가 자식 노드보다 더 큰 경우에 서로의 위치를 바꿨다.

값을 제거하고 힙을 재정렬할때도 부모 노드의 절대값이 자식 노드의 절대값 보다 큰 경우 뿐만 아니라 같은 경우도 고려해야 한다. 같을 경우에는 기존값이 작은 경우에 재정렬될 수 있도록 해야한다.



