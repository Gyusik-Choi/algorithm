# LeetCode

## 226. Invert Binary Tree

이진 트리를 뒤집는 문제다.

<br>

### Python

#### 첫번째 풀이

재귀로 풀이했다. 

재귀 호출을 통해 트리의 마지막 노드까지 내려간다. 마지막 노드의 자식 노드까지 호출하면 리턴 문으로 종료된 후에 마지막 노드의 자식 노드 (마지막 노드는 자식 노드가 없기 때문에 None) 간의 교환이 이루어진다. 그 뒤는 부모 노드로 이동하면서 교환이 이루어진다.

<br>

#### 두번째풀이

첫번째 풀이와 마찬가지로 재귀로 풀이했고 교재의 코드를 참고해서 코드를 간결하게 수정할 수 있었다.

root 가 None 인 경우 리턴하는 문을 제외하고 root 가 None 이 아닌 경우에 대해서만 교환 및 트리 노드를 리턴한다. 자바 등의 언어와 달리 파이썬에서는 리턴하지 않아도 에러가 발생하지 않고 None 을 할당할 수 있다.

<br>

#### 세번째 풀이

BFS 로 풀이했다.

재귀 호출은 자식 노드부터 교환하면서 부모 노드로 올라온다면 BFS 는 부모 노드부터 교환하면서 자식 노드로 내려간다.

루트 노드부터 시작해서 큐에서 꺼낸 노드가 None 이 아닌 경우에 해당 노드의 자식 노드간의 교환을 수행하고 자식 노드를 큐에 넣는다.

<br>

### Java

#### InvertBinaryTree226

직접 풀이했고 교재의 두번째 풀이와 완전히 동일하다.

<br>

#### InvertBinaryTree226_2

새로 노드를 생성하는 방식으로 풀이한다. 현재 노드에서 왼쪽, 오른쪽 자식노드를 뒤집어서 할당한다. 현재 노드의 left 속성값으로 오른쪽 자식노드를 인자로 넣어서 재귀호출 값을 할당하고 right 속성값으로 왼쪽 자식노드를 인자로 넣어서 재귀호출한 값을 할당한다.

재귀호출로 리프노드까지 내려가서 리턴된 값을 왼쪽 자식노드, 오른쪽 자식노드에 할당하고 다시 현재 노드를 리턴하는 방식으로 밑에서부터 위로 올라온다.

<br>

#### InvertBinaryTree226_3

첫번째 풀이와 유사한 풀이다. 첫번째 풀이는 왼쪽, 오른쪽 자식노드를 뒤집은 후 왼쪽, 오른쪽 자식노드를 재귀호출 했으나 이 풀이는 이를 반대로 수행한다. 재귀호출한 후 뒤집는다. 리프노드까지 내려간 다음 뒤집으면서 위로 올라온다.

<br>

#### InvertBinaryTree226_4

큐를 이용해서 순차적으로 뒤집는 방식으로 풀이했다.

<br>

#### InvertBinaryTree226_5

InvertBinaryTree226 와 동일한 방식으로 풀이했다. 언어를 Java 에서 Kotlin 으로 변경했다.

also 함수를 통해 python 과 유사하게 한줄로 swap 을 할 수 있었다. 아직 also 의 동작방식을 제대로 이해하지 못했다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

https://medium.com/@limgyumin/%EC%BD%94%ED%8B%80%EB%A6%B0-%EC%9D%98-apply-with-let-also-run-%EC%9D%80-%EC%96%B8%EC%A0%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94%EA%B0%80-4a517292df29

https://www.baeldung.com/kotlin/swap-utility

https://medium.com/@vibhanshusharma_93861/one-line-swap-algorithm-in-kotlin-e1cf6cc64708

https://kotlinlang.org/docs/scope-functions.html

