# LeetCode

## 232. Implement Queue using Stacks

스택을 이용해서 큐를 구현해야 한다.

<br>

### 232_implement_queue_using_stacks

pop, append 메소드로 큐를 구현하려 했다.

이전의 [큐로 스택을 구현하는 문제](https://leetcode.com/problems/implement-stack-using-queues/) 에서는 하나의 리스트로 구현이 가능했는데, 여기서는 두개의 리스트를 사용한다.

큐는 앞에서 꺼낸 요소들을 뒤로 넣으면 됐는데 스택은 뒤에서 꺼내고 다시 뒤로 넣는 방식이라 하나의 리스트로 구현할 수 없다.

아이디어는 append 를 할 때 리스트를 반대로 뒤집어 준다. 기존에 먼저 들어간 요소가 리스트의 마지막 (맨 우측) 에 있기 때문에 pop 으로 꺼낼 수 있다.

반대로 뒤집어 주는 방식은 리스트의 요소들을 pop 으로 빼서 임시 리스트에 넣어준 뒤에 새 아이템을 비어있는 리스트에 넣고 임시 리스트의 요소들을 다시 pop 으로 빼서 기존 리스트에 넣는다.

리스트에는 아이템이 역순으로 쌓이게 된다. 예를 들어 1, 2, 3, 4, 5 를 넣었다면 리스트에는 [5, 4, 3, 2, 1] 이렇게 들어있게 된다.

```
1, 2, 3 을 넣는다고 할 때 과정을 살펴보겠다.

먼저 arr, temp_arr 두개의 리스트가 있다.
arr = []
temp_arr = []

1) 1을 넣을 때는 
arr, temp_arr 이 비어있어서 arr 에 1을 넣기만 하면 된다.
arr = [1]
temp_arr = []

2) 2를 넣을 때는 
우선 arr 의 요소를 비워서 temp_arr 에 넣는다
arr = []
temp_arr = [1]

1이 temp_arr 에 들어왔다
이제 arr 에 2를 넣는다
arr = [2]
temp_arr = [1]

temp_arr 에 남은 1을 arr 에 넣는다
arr = [2, 1]
temp_arr = []

3) 3을 넣을 때는
먼저 arr 의 요소를 비워서 temp_arr 에 넣는다
arr = []
temp_arr = [1, 2]

arr 에 3을 넣는다
arr = [3]
temp_arr = [1, 2]

temp_arr 의 요소를 꺼내서 arr 에 넣는다
arr = [3, 2, 1]
temp_arr = []
```



<br>

### 232_implement_queue_using_stacks_2

교재에 나온 방식이다. 

두 개의 리스트를 사용한다는 점은 동일하나 앞선 풀이보다 나은 점은 매번 두개의 리스트를 비우고 넣는 작업을 할 필요가 없다.

input, output 리스트 2개를 사용하는데 input 은 요소를 넣는 경우에 사용하고 output 은 요소를 꺼내는 경우에 사용한다.

push 의 경우 append 를 통해 순차적으로 요소를 input 에 넣으면 된다.

pop 이나 peek 의 경우 output 에 요소가 하나라도 있으면 output 의 마지막 요소를 꺼내고, output 이 비어있으면 input 의 요소를 모두 꺼내서 output 으로 넣어주고 output 의 마지막 요소를 꺼내면 된다.

output 에 요소가 있을 경우는 input 을 비우고 output 에 넣는 작업을 할 필요가 없다.

<br><참고>

파이썬 알고리즘 인터뷰

