# 프로그래머스

## 피보나치 수

재귀나 메모이제이션 기법은 시간 초과 및 런타임 에러(최대 재귀호출 한도 초과) 가 발생한다.

리스트로 초기값 [0, 1] 을 설정한 후에 for 문을 돌면서 2부터 n까지 피보나치 수를 구했다. 

```python
fibo = [0, 1]
for num in range(2, n + 1):
    fibo.append(fibo[num - 1] + fibo[num - 2])
```

