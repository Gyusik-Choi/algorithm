# LeetCode

## 771. Jewels and Stones

### Python

해시맵을 활용하는 문제다. 파이썬은 딕셔너리를 활용할 수 있다.

<br>

#### 771_jewels_and_stones

defaultdict 를 활용했다. 

딕셔너리 기반이나 딕셔너리와 달리 없는 키를 조회하더라도 키 에러가 발생하지 않고 디폴트로 설정한 값이 세팅된다.

int 를 디폴트로 한 경우 없는 키를 조회하면 0이 값으로 설정된다.

<br>

#### 771_jewels_and_stones_2

Counter 클래스를 활용했다.

딕셔너리를 기본 자료구조로 활용하는데 인자로 들어온 요소들의 갯수를 세어준다.

defaultdict 와 마찬가지로 없는 키를 조회하더라도 키 에러가 발생하지 않는다. 

없는 키를 조회할 경우 키 에러 대신 0이 반환 된다.

<br>

#### 771_jewels_and_stones_3

해시맵 대신 한 줄로 풀이할 수도 있다.

<br>

### Java & Kotlin

#### JewelsAndStones771

Character, Boolean 을 각각 키, 값으로 갖는 해시맵에 jewels 정보를 저장했다. stones 를 문자 단위로 for 문을 돌면서 해시맵에 몇개나 문자가 들어있는지 구했다.

<br>

#### JewelsAndStones771_2

교재의 풀이를 참고했다. JewelsAndStones771 와 유사한데 조금 차이가 있다. JewelsAndStones771 에서는 해시맵으로 키의 존재 여부만 판단하면서 Boolean 으로 선언한 값이 역할이 없었다.

이 풀이에서는 해시맵의 값으로 Boolean 이 아닌 Integer 로 두면서 key 의 갯수를 저장한다. 그리고 jewels 가 아닌 stones 의 정보를 해시맵에 담고, jewels 를 문자 단위로 for 문을 돌면서 해시맵에 포함되었다면 해시맵의 값을 구해서 총합을 반환한다.

<br>

#### JewelsAndStones771_3

JewelsAndStones771 와 유사한데 해시맵이 아닌 해시셋으로 풀이했다.

<br>

#### JewelsAndStones771_4

stones 의 각 문자별 갯수를 해시맵으로 구한 뒤, jewels 의 각 문자를 해시맵에서 조회하여 동일한 키가 존재하는 경우 값을 누적했다.

문제의 조건으로 jewels 의 모든 문자는 unique 하다고 했기 때문에 동일한 문자를 중복으로 구하지 않는다.

<br>

### Kotlin

#### JewelsAndStones771

JewelsAndStones771_3 를 자바에서 코틀린으로 변경했다. 코틀린에서는 변경이 가능한 해시셋과 변경이 불가능한 해시셋이 따로 있다. 변경이 가능한 해시셋을 사용하기 위해 타입을 MutableSet 으로 선언했다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

