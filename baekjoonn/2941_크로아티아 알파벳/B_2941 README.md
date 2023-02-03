문자열은 " ", 문자는 ' '로 나타낸다.



배열 선언시

아래처럼 하면 안 된다.

```java
String[] arr = new String[3];
String arr = {'ab', 'bc', 'cd'}
// 이렇게 하면 에러난다
```

이건 가능하다.

```java
String[] arr = {'ab', 'bc', 'cd'};
```



참고

https://gismo99.tistory.com/entry/java-Array-constants-can-only-be-used-in-initializers