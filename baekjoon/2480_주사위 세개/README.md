# 백준

## 2480

조건문을 활용하는 문제다.

세 가지의 경우로 조건을 나눴다. 

먼저 같은 눈 3개가 나오는 경우는 조건문을 아래와 같이 작성했다.

```python
if first == second == third:
```

<br>

다음으로 모두 다른 눈이 나오는 경우의 조건문은 아래와 같다.

```python
def is_all_different_dice():
    if first != second and first != third and second != third:
        return True
    
    return False


if is_all_different_dice():
```

<br>

마지막으로 같은 눈 2개가 나오는 경우는 else 문으로 처리했다. 같은 눈 2개를 찾는 함수를 따로 작성했다.

```python
def get_same_dice():
    if first == second or first == third:
        return first
    
    if second == third:
        return second
```

<br>

한 가지 주의할 점은 아래의 조건은 first 와 third 가 같은 경우를 걸러낼 수 없다.

```python
# first 와 third 가 같을 수 있다
# first 가 3, second 가 1, third 가 3 일 경우에도
# 아래의 조건문을 만족한다
if first != second != third:
```

