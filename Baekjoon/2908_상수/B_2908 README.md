# 백준

## 2908

String을 거꾸로 뒤집는 방법으로 StringBuffer를 사용할 수 있다.

```java
String num = '123';
StringBuffer sb = new StringBuffer();
sb.append(num)
sb.reverse();
```



StringBuffer에서는 바로 정수로 변환이 안돼서 String으로 변환한 후에 정수로 바꿔야 한다.

```java
int changeIntNum = Integer.parseInt(sb.toString());
```

