#  LeetCode

## 937. Reorder Data in Log Files

### 937_reorder_data_in_log_files.py

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

<참고>

파이썬 알고리즘 인터뷰