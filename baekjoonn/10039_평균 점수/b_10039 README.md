# 백준

## 10039

- 만약에 배열을 선언해서 입력 값들을 저장했을 때 총합을 구하려면

  - 정수 0을 하나 선언하고 배열을 for 문을 돌려 하나씩 선언한 정수에 더해준다.

  - 라이브러리를 통해 구할 수도 있다.

    ```java
    import java.util.stream.IntStream;
    
    int[] arr = [10, 20, 30, 40, 50]
    int sums = IntStream.of(arr).sum();
    ```

  