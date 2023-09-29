# 프로그래머스

## 내적

map 함수를 돌면서 a, b 의 곱셈의 합을 리턴했다.

map 함수에서 루프를 돌 대상을 1개가 아니라 2개 이상도 할 수 있다는 것을 알게 됐다.

```python
a = [1, 2, 3, 4]
b = [4, 3, 2, 1]
sum(list(map(lambda x, y: x * y, a, b)))
```

<br>

만약에 인자로 2개 이상의 요소가 들어왔을 때 서로 길이가 다르다면 더 짧은 길이만큼만 돌게 된다.

```python
a = [1, 2, 3, 4]
b = [1, 2, 3, 4, 5]
list(map(lambda x, y: x + y, a, b))
# [2, 4, 6, 8]
```



<br>

<참고>

https://docs.python.org/3/library/functions.html#map

