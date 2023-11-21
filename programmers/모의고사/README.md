# 프로그래머스

## 모의고사

완전탐색 유형의 문제다.

1번, 2번, 3번 수포자의 찍는 패턴을 리스트에 담았다. 

각각 패턴별로 answers 와 일치하는 정답의 갯수가 몇 개인지 구하기 위해 answers 를 for 문을 돌면서 answers 의 인덱스 값과 패턴의 값이 일치하는지 판단한다.

```
answers = [1, 2, 3, 4, 5]
pattern = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

<br>

한 수포자의 패턴이 위의 pattern 리스트라고 가정한다. pattern 리스트의 0번부터 4번 인덱스까지는 answers 의 1, 2, 3, 4, 5 와 비교해야 하고 5번부터 마지막인 8번 인덱스까지는 다시 answers 의 처음부터 비교를 시작해서 1, 2, 3, 4 와 비교가 되야 한다.

answers 로 for 문을 돌면서 answers 의 인덱스에서 pattern 길이를 나눈 나머지 값이 patterns 의 인덱스가 된다. 

```python
answers = [1, 2, 3, 4, 5, 6]
pattern = [1, 2, 3]

cnt = 0
for idx, answer in enumerate(answers):
  # 0, 1, 2, 0, 1, 2
  i = idx % len(pattern)
  if answer == pattern[i]:
    cnt += 1
```



