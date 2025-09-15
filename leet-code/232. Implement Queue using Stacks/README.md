# LeetCode

## 232. Implement Queue using Stacks

스택을 이용해서 큐를 구현해야 한다.

<br>

### Python

#### 232_implement_queue_using_stacks

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

#### 232_implement_queue_using_stacks_2

교재에 나온 방식이다. 

두 개의 리스트를 사용한다는 점은 동일하나 앞선 풀이보다 나은 점은 매번 두개의 리스트를 비우고 넣는 작업을 할 필요가 없다.

input, output 리스트 2개를 사용하는데 input 은 요소를 넣는 경우에 사용하고 output 은 요소를 꺼내는 경우에 사용한다.

push 의 경우 append 를 통해 순차적으로 요소를 input 에 넣으면 된다.

pop 이나 peek 의 경우 output 에 요소가 하나라도 있으면 output 의 마지막 요소를 꺼내고, output 이 비어있으면 input 의 요소를 모두 꺼내서 output 으로 넣어주고 output 의 마지막 요소를 꺼내면 된다.

output 에 요소가 있을 경우는 input 을 비우고 output 에 넣는 작업을 할 필요가 없다.

<br>

### Java

#### ImplementQueueUsingStacks232

ArrayDeque 를 활용해서 풀이했다. ArrayDeque 에는 스택 구현을 위한 push, pop 메소드가 있다.

스택에 요소들을 push 한 후에 pop 으로 스택의 요소를 꺼내면 가장 마지막에 push 한 요소가 꺼내진다. 스택으로 큐를 구현해야 하는 문제라 이렇게 되면 안 돼서 2개의 ArrayDeque 를 사용한다.

push 는 stack1 변수에 push 메서드로 요소를 집어넣는다. 

pop 과 peek 이 거의 유사하게 동작하는데 약간의 차이가 있다.

pop 과 peek 모두 stack1이 빌 때까지 stack1 의 요소를 pop 으로 꺼내서 stack2 에 push 한다. 이러면 stack1 에서 가장 마지막에 들어간 요소가 stack2 로 가장 먼저 들어가고, stack1 에 가장 먼저 들어간 요소가 stack2 에 가장 마지막에 들어간다.

여기서 pop 과 peek 의 차이가 나타나는데 stack2 로 stack1 의 요소를 모두 옮긴 후 pop 은 stack2 에서 pop 으로 요소를 꺼내지만, peek 은 stack2 에서 element 로 요소를 꺼내지 않고 확인만 한다.

이후 pop 과 peek 모두 stack2 가 빌 때까지 stack2 의 요소를 pop 으로 꺼내서 stack1 에 push 한다.

<br>

### Kotlin

#### ImplementQueueUsingStacks232

두 개의 스택을 이용했다. 하나의 스택(stack)에서 요소를 관리하기 위해 다른 하나의 스택(stackHelper)은 연산 중에 잠시 차는 경우를 제외하고 항상 비어있다.

pop 메소드의 경우 stack 에 있는 요소를 모두 꺼내서 stackHelper 에 넣고 이때 stackHelper 에서 요소를 꺼내면 마치 큐에서 첫번째 요소를 얻는것처럼 요소를 얻을 수 있다. 그리고 stackHelper 를 비우기 위해 stack 에 다시 넣는다. 이렇게 되면 가장 첫번째로 스택에 들어온 요소가 제거되고 나머지 요소는 기존 스택의 구조를 그대로 유지한채로 남아있다.

peek 의 경우 pop 과 유사하다. 한 가지 차이는 stack 에 있는 요소를 모두 꺼내서 stackHelper 에 넣고 stackHelper 에서 요소를 꺼내는게 아니라 stackHelper 에서 가장 최상단에 있는 요소를 조회(peek) 만 한다.

<br>

#### ImplementQueueUsingStacks232_2

교재의 풀이를 참고해서 ImplementQueueUsingStacks232 의 풀이를 개선했다.

ImplementQueueUsingStacks232 에서는 pop, peek 메소드를 호출하면 매번 두 개의 스택에 요소가 왔다 갔다 이동하는 작업이 반복된다. ImplementQueueUsingStacks232_2 에서는 이렇게 하지 않는다. input 에 요소를 계속 쌓다가 peek 이나 pop 메소드가 호출되면 ouput 이 비었다면 input 에 있는 요소를 모두 output 으로 옮긴다. 이때부터 output 에 요소가 하나라도 있는동안 peek 이나 pop 이 호출되면 input 에서 output 으로 요소를 옮기는 작업없이 곧장 output 에서 조회할 수 있다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

