# LeetCode

## [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

트라이를 구현하는 문제다.

<br>

### 첫번째 풀이

Node 클래스의 words 를 리스트로 선언했다. insert 할 때 word 에 대한 for 문을 돌면서 매 글자마다 words 리스트에 word 를 추가해준다. 이렇게 구현하면 starts_with 을 찾을 때 포함 여부 뿐만 아니라 어떤 단어들이 실제로 있는지 words 리스트만 보면 되기 때문에 찾기가 편하다.

다만 문제의 요구사항을 넘어가는 구현이다.

<br>

### 두번째 풀이

교재를 참고해서 작성했다.

Node 클래스의 word 를 False 로 초기화 한 후에 insert 할 때 for 문을 모두 마친 후 cur 노드의 word 값을 True 로 바꾼다. for 문을 탐색하면서 나오는 요소들의 word 값은 False 로 유지된 채 단어의 마지막 글자에 대해서만 word 가 True 가 된다.

search 할 때 cur.word 값을 통해 해당 단어가 Trie 에 포함이 됐는지 알 수 있다. cur.word 가 False 라면 이는 이 단어 자체는 없다는 의미다.

예를 들어 Trie 에 apple 이 들어있고 app 을 search 한다면 app 자체는 Trie 에 없어서 False 다. 

search 와 달리 starts_with 은 cur.word 로 판단할 필요가 없다. prefix 로 시작하는 단어가 있는지 여부만 보면 되기 때문에 prefix 자체가 Trie 에 있는지 여부와 관계가 없다. for 문을 순회하면서 not in 연산에 걸리지 않으면 for 문을 순회한 후 True 를 리턴한다.



