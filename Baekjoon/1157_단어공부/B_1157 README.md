# 백준

## B_1157 

String을 받아서 한 글자씩 나눌때는

```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
String word = br.readLine();
for (int i = 0; i < word.length(); i++) {
    char alpha = word.charAt(i);
}
```

이렇게 charAt을 사용해서 char형으로 변환한다.

이를 대문자나 소문자로 변환할 때는 toUpperCase()나 toLowerCase()를 사용할 수 없다.

이것들은 String에서 가능하다.

char를 대문자나 소문자로 변환하려면

```java
alpha = Character.toUpperCase(alpha) // 대문자
alpha = Character.toLowerCase(alpha) // 소문자
```

