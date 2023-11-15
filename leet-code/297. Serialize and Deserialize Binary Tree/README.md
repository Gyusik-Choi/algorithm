# LeetCode

## 297. Serialize and Deserialize Binary Tree

이진 트리를 문자열로 변환하고, 변환한 문자열을 이진 트리로 변환해야 한다.

<br>

### 첫번째 풀이

#### serialize

BFS 로 탐색한다. 데크에 root 노드를 넣고 데크가 빌 때까지 while 문을 반복한다. 

데크에서 꺼낸 노드가 None 이 아니면 해당 노드의 val 값을 리스트에 넣고 데크에는 노드의 왼쪽, 오른쪽 자식을 넣는다. 노드가 None 이라면 노드가 없다는 것을 표현하기 위해 리스트에 # 를 넣었다. 문자열로 리턴하기 위해 None 은 문자열로 변환이 되지 않아서 None 대신 # 를 넣었다.

<br>

#### deserialize

```
Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
```

코드 입력 란에 주석으로 된 설명을 보면 serialize 를 호출하고 받은 값을 deserialize 함수의 인자로 넣는다.

<br>

문자열인 deserialize 함수의 파라미터를 리스트로 변환한 후에 리스트의 첫번째 요소를 TreeNode 로 변환하고 데크에 담는다. serialize 함수에서 리스트에 루트 노드부터 담기 때문에 리스트의 첫번째 요소는 루트 노드다.

데크가 빌 때까지 while 문을 돌면서 리스트의 인덱스를 한 칸씩 늘려가면서 탐색한다. 데크에서 꺼낸 노드의 왼쪽, 오른쪽 자식 노드를 찾는다.

데크에서 꺼낸 노드가 루트 노드고 해당 노드부터 left, right 변수에 객체를 이어가는 형태다. 그리고 이 left, right 변수에 담긴 객체들이 다시 데크에 들어가기 때문에 객체 참조에 의해 전체 트리를 구성할 수 있다.

<br>

<참고>

파이썬 알고리즘 인터뷰

