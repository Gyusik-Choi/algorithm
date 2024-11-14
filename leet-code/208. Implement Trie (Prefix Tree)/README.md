# LeetCode

## [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

트라이를 구현하는 문제다.

<br>

### Python

#### 첫번째 풀이

Node 클래스의 words 를 리스트로 선언했다. insert 할 때 word 에 대한 for 문을 돌면서 매 글자마다 words 리스트에 word 를 추가해준다. 이렇게 구현하면 starts_with 을 찾을 때 포함 여부 뿐만 아니라 어떤 단어들이 실제로 있는지 words 리스트만 보면 되기 때문에 찾기가 편하다.

다만 문제의 요구사항을 넘어가는 구현이다.

<br>

#### 두번째 풀이

교재를 참고해서 작성했다.

Node 클래스의 word 를 False 로 초기화 한 후에 insert 할 때 for 문을 모두 마친 후 cur 노드의 word 값을 True 로 바꾼다. for 문을 탐색하면서 나오는 요소들의 word 값은 False 로 유지된 채 단어의 마지막 글자에 대해서만 word 가 True 가 된다.

search 할 때 cur.word 값을 통해 해당 단어가 Trie 에 포함이 됐는지 알 수 있다. cur.word 가 False 라면 이는 이 단어 자체는 없다는 의미다.

예를 들어 Trie 에 apple 이 들어있고 app 을 search 한다면 app 자체는 Trie 에 없어서 False 다. 

search 와 달리 starts_with 은 cur.word 로 판단할 필요가 없다. prefix 로 시작하는 단어가 있는지 여부만 보면 되기 때문에 prefix 자체가 Trie 에 있는지 여부와 관계가 없다. for 문을 순회하면서 not in 연산에 걸리지 않으면 for 문을 순회한 후 True 를 리턴한다.

<br>

### Java

#### ImplementTrie208

Trie 클래스 안에 TrieNode 클래스를 내부 클래스로 뒀다. TrieNode 클래스는 문자 하나를 나타내는 character, 단어를 나타내는 word, 자식 노드들을 관리하는 children 변수를 갖는다.

children 변수는 길이 26의 배열로 고정해서 소문자 알파벳 a 부터 z 까지 알파벳 순서대로 인덱스 접근할 수 있도록 한다. 

<br>

#### ImplementTrie208_2

교재의 풀이를 참고했다. ImplementTrie208 보다 간결하게 풀이했다. 

TrieNode 클래스에서 character 변수를 사용하지 않으며 word 도 단어 전체를 나타내지 않고 boolean 으로 두어서 해당 TrieNode 까지가 한 단어를 구성하는지 여부만 판단한다.

그리고 알파벳의 인덱스를 구할 때 char 타입의 문자에서 아스키 코드 97을 빼지 않고 문자에서 문자를 빼는 방식으로 접근한다. 자바는 문자에서 문자를 빼면 유니코드 값을 반환하는데 알파벳의 유니코드는 아스키코드와 일치한다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

