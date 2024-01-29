# 백준

## 7785

해시맵 유형의 문제다.

근무 중인 사람을 구하기 위해서 enter 를 했으면서 leave 하지 않은 사람을 구해야 한다. 이름을 키, 출입 기록을 값으로 해서 입력받은 값을 defaultdict 에 저장한다. 이름이 키라서 동일한 인물이 여러번 나오면 defaultdict 에 남는 출입 기록은 마지막에 나온 출입 기록이 된다.

defaultdict 의 default 값을 문자열로 설정해서 입력을 받을 때 in 메소드로 해당 키가 defaultdict 에 존재하는지 판단하지 않아도 된다.

출입 기록을 담은 defaultdict 를 출입 기록이 enter 인 사람만 filter 함수로 걸러낸 후에 키를 기준으로 내림차순 정렬해서 키만 출력한다.

<br>

<참고>

https://docs.python.org/3/library/collections.html#collections.defaultdict

