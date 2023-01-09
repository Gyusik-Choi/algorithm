# 이것이 코딩테스트다

## 챕터 18 42번 탑승구

서로소 집합(disjoint set)을 활용하는 문제다. 서로소 집합을 어떻게 활용해야 할지 판단하는게 어려운 문제였다.

탑승구 번호의 루트 노드 값을 find 연산하고 이 값이 0이 아니면 탑승구 번호와 탑승구 번호 - 1 을 union 연산한다. 탑승구 탑승구 번호의 루트 노드 값이 0이면 모든 탑승구가 도킹되어서 추가 도킹이 안되는 상황이다.

예를 들어 

3

3

3

2

3

다음과 같은 입력이 주어져서 3 2 3 을 도킹한다고 하면

```python
p = [0, 1, 2, 3]
```

<br>

3을 먼저 도킹하면

```python
p = [0, 1, 2, 2]
```

<br>

2를 도킹하면

```python
p = [0, 1, 1, 2]
```

<br>

이어서 3을 도킹하면

```python
# find_set 을 통해 아래와 같이 되고
p = [0, 1, 1, 1]
# 이후 union_set 을 통해 아래와 같이 된다
p = [0, 0, 1, 1]
```

<br>

<참고>

https://velog.io/@embeddedjune/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9D%B4%EA%B2%83%EC%9D%B4-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%9D%B4%EB%A1%A0-%EB%AC%B8%EC%A0%9C-Q42-%ED%83%91%EC%8A%B9%EA%B5%AC

https://cold-soup.tistory.com/117

https://blex.me/@mildsalmon/chap-18-%EA%B7%B8%EB%9E%98%ED%94%84%EC%9D%B4%EB%A1%A0-q42-%ED%83%91%EC%8A%B9%EA%B5%AC

