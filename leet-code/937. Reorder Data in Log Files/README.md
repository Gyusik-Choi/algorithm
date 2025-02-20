#  LeetCode

## 937. Reorder Data in Log Files

### Python

파이썬 알고리즘 인터뷰 교재에는 로그의 종류가 2가지라는 내용이 없었다. 그래서 교재에서 식별자를 제외한 첫번째 문자열에 isdigit() 함수를 사용해서 해당 로그가 문자로 구성된 로그인지 숫자로 구성된 로그인지 판단하는게 어떻게 가능한지 이해하지 못했었다.

<br>

Leet Code 사이트의 문제에는 다음과 같이 로그의 종류가 2가지라고 명시되어 있다.

```
There are two types of logs:
- Letter-logs: All words (except the identifier) consist of lowercase English letters.
- Digit-logs: All words (except the identifier) consist of digits.
```

<br>

식별자를 제외하고 문자로만 구성된 문자열이거나 아니면 숫자로만 구성된 문자열 둘 중 하나이므로 식별자 다음의 첫번째 문자열에 대해서  isdigit() 함수를 통해 Letter-logs 인지, Digit-logs 인지 판단할 수 있다.

<br>

### Java

로그의 종류를 구분할때 전체 문자열을 볼 필요가 없다. 

Letter-logs 는 식별자를 제외하고 모두 영소문자로 되어있고, Digit-logs 는 식별자를 제외하고 모두 정수로 구성되어 있다. 

로그를 공백을 기준으로 잘라낸 후 식별자 이후의 문자열 하나를 골라서 해당 문자열의 한 글자만 확인하면 된다.

<br>

stream 사용 여부로 인한 차이는 1ms 정도 (13ms -> 12ms) 였으나, 전체 문자열을 검사하지 않고 한 글자만 검사하는 방법을 통해 시간을 3배 가까이(13ms -> 5ms) 빠르게 할 수 있었다.

<br>

### Kotlin

자바의 ReorderDataInLogFiles937_3 풀이와 동일한 방식으로 풀이했다.

split 메소드에서 limit 을 지정할 때 named parameter 로 limit 을 명시해야 하는 점이 자바와 달랐다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

