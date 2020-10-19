# 백준

## 10809

파이썬에서 배열을 출력하는 방식으로는

```python
arr = [1, 2, 3]
print(arr)
```

자바에서는 배열 전체를 출력할 수 없다.

```java
int[] arr = {1, 2, 3};
System.out.println(arr); // 이렇게 하면 제대로 출력 안 된다. 배열의 hashcode가 출력 된다.
System.out.println(arr[0]); // 이건 가능하다.
```

이런 방식으로 배열 전체를 출력할 수 없다.



이 방법으로 가능하다.

```java
import java.util.Arrays;

int[] arr = {1, 2, 3};
System.out.println(Arrays.toString(arr));
System.out.println(Arrays.deepToString(arr));
```



참고

https://seongsillvanas.tistory.com/9