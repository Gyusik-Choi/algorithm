# LeetCode

## [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

### Python

이진탐색트리의 전위 순회와 중위 순회 리스트를 토대로 트리를 구성해야 한다.

전위 순회의 값은 중위 순회의 값을 좌, 우측으로 이등분한다.

전위 순회는 부모, 왼쪽 자식, 오른쪽 자식 순서로 이루어진다. 중위 순회는 왼쪽 자식, 부모, 오른쪽 자식 순서로 이루어진다. 

중위 순회에서 부모 노드는 왼쪽 자식 보다 늦게 탐색한다. 전위 순회 리스트에 담긴 요소들을 순서대로 중위 순회 리스트에서 찾으면 중위 순회를 왼쪽, 오른쪽으로 나눠 가면서 점점 작은 단위로 분할 정복 하듯이 탐색한다.

전위 순회 리스트를 순서대로 탐색하면서 노드를 생성하고 노드를 생성한 요소의 인덱스를 중위 순회 리스트에서 찾는다. 인덱스를 기준으로 리스트의 왼쪽을 왼쪽 자식 노드를 찾기 위한 재귀 호출을 하고, 리스트의 오른쪽을 오른쪽 자식 노드를 찾기 위한 재귀 호출을 한다.

<br>

### Java

전위 순회와 중위 순회의 관계를 파악하는게 중요했다.

전위 순회 배열의 요소를 순차적으로 꺼내서 중위 순회 리스트를 분할 정복해 나간다. 전위 순회 배열의 요소로 중위 순회 배열을 왼쪽, 오른쪽 구간으로 나눈다. 나눠진 왼쪽, 오른쪽 구간을 각각 왼쪽, 오른쪽 자식 노드를 찾기 위한 재귀 호출을 한다.

이 부분이 이해하기 어려웠는데 재귀 호출 속에서 전위 순회 배열의 첫번째 요소를 계속 꺼낸다. 재귀 호출은 나눠진 중위 순회 배열을 기준으로 이루어지는데 재귀 호출에서 전위 순회 배열의 첫번째 요소를 꺼내는게 어떻게 올바른 전위 순회 요소에 대한 접근이 될 수 있을지 궁금했다. 

중위 순회 배열은 전위 순회 배열의 요소에 따라서 왼쪽, 오른쪽 구간이 나눠지고 이를 재귀 호출한다. 전위 순회 배열을 하나씩 꺼내는게 재귀 호출의 순서와 어떻게 딱 맞을 수 있는지 이해하기 어려웠다.

하나의 이진 트리에서 나온 전위 순회, 중위 순회 결과라서 서로 연관되어 있다.

예를 들어 루트 노드가 1, 오른쪽 자식노드가 3, 오른쪽 자식노드의 오른쪽 자식노드가 5라고 가정한다. 이때 전위 순회 결과는 [1, 3, 5] 가 되고 중위 순회 결과도 [1, 3, 5] 가 된다. 

이 트리는 왼쪽 자식노드가 없고 오른쪽 자식노드만 있다. 

전위 순회의 1을 기준으로 중위 순회 배열을 분할하면 왼쪽은 없고 오른쪽에 3, 5 가 있다. 왼쪽 자식노드에 대한 재귀 호출은 중위 순회 배열이 null 이라 전위 순회 요소를 꺼내지 않고 종료된다. 오른쪽 자식노드에 대한 재귀 호출은 중위 순회 배열은 [3, 5] 가 있다. 

전위 순회의 3을 기준으로 중위 순회 배열 [3, 5] 를 분할하면 왼쪽은 없고 오른쪽에 5 가 있다. 왼쪽 자식노드에 대한 재귀 호출은 중위 순회 배열이 null 이라 전위 순회 요소를 꺼내지 않고 종료된다. 오른쪽 자식노드에 대한 재귀 호출은 중위 순회 배열은 [5] 가 있다.

전위 순회의 5를 기준으로 중위 순회 배열을 분할하면 왼쪽은 없고 오른쪽에도 없어서 재귀 호출이 되자마자 종료되고 재귀 호출이 끝난다.

전위 순회의 순서는 중위 순회를 분할하고 재귀 호출하는 순서와 일치한다.

만약에 루트 노드가 1, 왼쪽 자식 노드가 3, 오른쪽 자식노드가 5인 경우라면 전위 순회 결과는 [1, 3, 5], 중위 순회 결과는 [3, 1, 5] 가 된다. 이때는 전위 순회의 1을 기준으로 중위 순회 배열을 분할하면 왼쪽에 3 이 있어서 왼쪽의 3을 기준으로 재귀 호출이 되고 이때 전위 순회의 다음 순서는 3이라 역시 전위 순회의 순서와 중위 순회를 분할하고 재귀 호출하는 순서는 일치한다.

<br>

### Kotlin

```
전위순회 - [1, 2, 4, 5, 3, 6, 7, 9, 8]
중위순회 - [4, 2, 5, 1, 7, 9, 6, 8, 3]
```

전위순회, 중위순회 결과가 위와 같다고 가정한다. 

전위순회의 첫번째 값인 1은 중위순회 결과를 왼쪽, 오른쪽으로 분할한다. 그리고 이 1은 중위순회에서는 인덱스 3에 위치하는데 전위순회 인덱스 3은 중위순회의 왼쪽을 포함하는 인덱스다. 중위순회에서 왼쪽에 위치한 4, 2, 5 를 포함한다.

전위순회의 요소를 중위순회에서 찾은 인덱스로 중위순회를 왼쪽, 오른쪽으로 구분할 수 있을 뿐만 아니라 전위순회 또한 왼쪽, 오른쪽으로 구분할 수 있다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰