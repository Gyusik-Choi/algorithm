# LeetCode

## 49. Group Anagrams

### Python

#### 49_group_anagrams

파라미터 strs 를 for loop 돌면서 오름차순으로 정렬하여 defaultdict 에 넣어줬다.

<br>

### Dart

#### 49_group_anagrams

49_group_anagrams.py 와 방식 자체는 같으나defaultdict 가 아닌 Map 을 사용했기 때문에 key error 가 발생하지 않도록 해당 key 가 존재하는지 확인하는 작업이 추가됐다.

<br>

### Java

#### GroupAnagrams49, GroupAnagrams49_2

HashMap 을 이용해서 위의 풀이와 같은 방식으로 풀이했다.

<br>

### Kotlin

#### GroupAnagrams49, GroupAnagrams49_2

Java 풀이와 동일한 방식으로 풀이했다.

Java 보다 간결하게 풀이할 수 있는 방식이 있어서 코드 양을 줄일 수 있었다.

문자열의 문자를 정렬하기 위해서 Java 와 Kotlin 모두 Character Array 형태로 변환한다. 

Java 는 Arrays.sort 를 이용해서 정렬하고 이 정렬은 원본을 정렬하고 반환값이 없어서 정렬을 위한 코드를 한 줄 추가해야 한다.

반면에 Kotlin 은 메소드 체이닝이 가능한 sorted 메소드가 있는데다가 문자열로 변환하는 joinToString 까지 메소드 체이닝으로 모두 가능하다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

https://www.techiedelight.com/ko/sort-string-java/

https://www.baeldung.com/kotlin/arraylist-vs-mutablelistof

