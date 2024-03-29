# Trie

문자열 검색시에 많이 이용되는 자료구조다.

문자열을 트리 형식으로 만들기 때문에 탐색 효율이 높다.

이어지는 단어의 글자들을 딕셔너리를 활용해서 key의 value 값으로 노드들을 이어나간다.

예를 들어서 "trie"라는 단어가 있다고 하면, {"t": {key: "t", data: None, children: {"r": data: None, children: {"i": data: "trie", children: {"e": {}}}}}} 이렇게 children이라는 value의 key 값에 계속해서 저장하는 형태다. 그리고 단어의 마지막 글자에서 data 변수에 단어 "trie"를 넣어서 이 지점이 해당 단어의 마지막 노드임을 나타낸다.

<br>

trie(ver3) 를 구현하면서 아쉬운점이 있었다. 단어가 'ABC', 'ABD', 'ACD', 'ADE', 'BAC' 가 있다고 할때 A로 시작하는 단어를 찾는 함수에서는 BAC 는 찾을 수 없었다. 이게 trie 자료구조 자체의 특성상 어쩔 수 없는 부분일 수 있으나 추후에는 특정 단어로 시작하는 함수 외에 특정 단어가 들어간 단어를 찾을 수 있는 함수도 작성해보고 싶다.

<br>

trie_ver4.py 와 trie2.js 파일에서 기존의 파일에 있던 오류를 수정했다. 'A', 'ABC', 'ABD' 단어가 있을 때 기존 파일은 'A' 로 시작하는 단어를 찾을 때, 'A' 는 찾지 못한다. 이 부분은 기존 파일도 수정해야 한다.
