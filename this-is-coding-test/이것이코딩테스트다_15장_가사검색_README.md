# 이것이 코딩테스트다

## 챕터 15 30번 가사검색

### Python

#### 첫번째 풀이

카카오 코딩테스트 기출문제다. 이진탐색 혹은 트라이를 활용할 수 있는 문제인데 트라이로 풀이했다.

단어의 한 글자마다 해당 단어의 총 길이를 알 수 있도록 Node 클래스에 self.length = [] 요소를 추가했다. queries 로 abc?? 가 있으면 c 까지 찾은 후에 abc 로 시작하면서 5 글자인 단어들은 모두 다 탐색하지 않고도 length 를 통해서 알 수 있도록 했다.

abcde, abcef, abcfg 단어가 있으면 a 에서 length 가 [5, 5, 5], b 에서 [5, 5, 5], c 에서 [5, 5, 5] 로 될 수 있도록 한다. 그래서 c 까지 탐색하고서 5가 3개 있음을 알 수 있다.

(혹시 테스트가 수행이 안 된다면 한글 파일 이름 문제다. 파일 이름을 영어로 바꿔서 실행하면 정상 동작한다.)

<br>

### JavaScript

#### 첫번째 풀이

python 으로 풀이한 방법을 사용했으나 시간초과가 발생했다.

Node 클래스의 len 인스턴스 변수를 글자 수를 담는 배열 대신에 글자수 자체를 세도록 했다.

대신 글자수를 세기 위해서 trie 인스턴스를 글자수만큼 만들어줘야 한다. 그래야 5글자일때의 len 변수 값과 6글자일때의 len 변수 값이 구분될 수 있다.

words 배열의 for loop 를 돌면서 요소의 글자수를 계산해서 해당 글자수를 키로 하는 trie 인스턴스가 없으면 새로 생성하고 글자를 넣어준다. 글자를 뒤집어서도 똑같이 실행해줘야 한다.

한 가지 주의할점은 tries 나 reversedTries 객체에 해당하는 글자수 키가 없으면 trie 인스턴스 변수를 생성만하면 안되고 글자도 넣어줘야 len 값을 1만큼 더해줄 수 있다.

```javascript
if (!tries.hasOwnProperty(wordLength.toString())) {
  tries[wordLength] = new Trie();
}

tries[wordLength].insert(word)
```



그리고 정답을 구하기 위해 queries 배열의 for loop 를 돌면서 요소의 글자수를 키로 하는 tries 나 reversedTries 객체의 값이 없으면 0, 있으면 startWithPrefix 함수를 호출해서 len 변수 값을 구할 수 있도록 한다.

<br>

### Java

#### 첫번째 풀이

JavaScript 풀이에서는 Object 로 tries, reversedTries 를 선언하고 단어의 길이를 key 로 하여 Trie 인스턴스를 생성하는 방법을 사용했다. 단어의 길이로 Trie 인스턴스를 생성한 이후에는 단어를 한 글자씩 loop 를 돌면서 children 속성에 Trie 를 생성하면서 len 값을 1씩 늘려나갔다.

처음에 단어 길이별로 Trie 인스턴스를 생성하기 때문에 len 속성의 값만 1씩 늘려주면 되고 답을 구할때도 len 속성의 값만 조회하면 답을 구할 수 있다. query 로 시작하는 단어 갯수를 찾는 startWithPrefix 함수를 호출할때 tries 에서 queryLength 로 조회한 Trie 인스턴스의 메소드를 호출한다.

```javascript
tries[queryLength].startWithPrefix(query)
```

<br>

Java 풀이에서는 JavaScript 풀이와 유사하지만 조금 다른 방식을 사용했다. Java 풀이에서는 처음에 단어 길이로 Trie 인스턴스를 생성하지 않고 전체 첫 head 노드는 하나로 한다. JavaScript 풀이에서는 같은 단어 길이별로 Trie 인스턴스를 생성하는데 Java 풀이에서는 그렇지 않기 때문에 단어의 길이별로 몇 개의 단어가 있는지 별도로 관리해줘야 한다.

HashMap 을 통해 단어의 길이를 key 로 하고 단어의 길이별 단어 수를 value 로 해서 단어의 길이별로 단어의 갯수가 몇 개 인지 세어준다.

<br>

<참고>

https://velog.io/@hope1213/프로그래머스-가사검색-파이썬

https://school.programmers.co.kr/learn/courses/30/lessons/60060/solution_groups?language=javascript

https://velog.io/@diddnjs02/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%82%AC-%EA%B2%8C%EC%9E%84