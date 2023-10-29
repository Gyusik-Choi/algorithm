# LeetCode

## 771. Jewels and Stones

해시맵을 활용하는 문제다. 파이썬은 딕셔너리를 활용할 수 있다.

<br>

### 첫번째 풀이

defaultdict 를 활용했다. 

딕셔너리 기반이나 딕셔너리와 달리 없는 키를 조회하더라도 키 에러가 발생하지 않고 디폴트로 설정한 값이 세팅된다.

int 를 디폴트로 한 경우 없는 키를 조회하면 0이 값으로 설정된다.

<br>

### 두번째 풀이

Counter 클래스를 활용했다.

딕셔너리를 기본 자료구조로 활용하는데 인자로 들어온 요소들의 갯수를 세어준다.

defaultdict 와 마찬가지로 없는 키를 조회하더라도 키 에러가 발생하지 않는다. 

없는 키를 조회할 경우 키 에러 대신 0이 반환 된다.

<br>

### 세번째 풀이

해시맵 대신 한 줄로 풀이할 수도 있다.

<br>

<참고>

파이썬 알고리즘 인터뷰
