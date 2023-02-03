# 백준

## 10952 

- BufferedWriter의 write 메서드는 정수형 변수를 출력할 수 없다.
- 정수를 출력하고 싶다면 문자열로 형변환해서 출력할 수 있다.
- 정수를 문자로 형변환하는 방법은

```java
int sums = 30;
String sum = Integer.toString(sums);
```

- 이번 문제에서 정수를 System.out.println으로 출력하는 방법과 정수를 문자열로 변환해서 write 메서드로 출력하는 방법을 둘 다 시도해보았다.
- 후자가 시간은 아주 조금 빨랐으나, 형변환하는 작업으로 인해 메모리를 더 소모했다.