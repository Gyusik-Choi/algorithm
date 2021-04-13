# Trie

문자열 검색시에 많이 이용되는 자료구조다.

문자열을 트리 형식으로 만들기 때문에 탐색 효율이 높다.

이어지는 단어의 글자들을 딕셔너리를 활용해서 key의 value 값으로 노드들을 이어나간다.

예를 들어서 "trie"라는 단어가 있다고 하면, {"t": {key: "t", data: None, children: {"r": data: None, children: {"i": data: "trie", children: {"e": {}}}}}} 이렇게 children이라는 value의 key 값에 계속해서 저장하는 형태다. 그리고 단어의 마지막 글자에서 data 변수에 단어 "trie"를 넣어서 이 지점이 해당 단어의 마지막 노드임을 나타낸다.