# 백준

## 10798

5 X 15 크기의 배열을 만들고 기본값을 빈 문자열("")로 설정했다. 

입력 받은 문자를 하나씩 넣은 후 빈 문자열인지 검사하여 빈 문자열이 아니면 출력했다.

빈 문자열인 경우 not 연산에 걸린다.

```python
a = ''
print(not a)
# True
```



<br>

문제에서 주의할 점이 있다.

sys.stdin.readline() 은 int(sys.stdin.readline()) 와 달리 마지막에 개행 문자가 함께 출력된다.

예를 들어 입력은 아래와 같다.

```
AABCDD
afzz
09121
a8EWg6
P5h3kx
```



위의 입력을 출력하면 개행문자가 함께 출력된다.

```python
for i in range(N):
    word = list(sys.stdin.readline())
    print(word)
```



```
['A', 'A', 'B', 'C', 'D', 'D', '\n']
['a', 'f', 'z', 'z', '\n']
['0', '9', '1', '2', '1', '\n']
['a', '8', 'E', 'W', 'g', '6', '\n']
['P', '5', 'h', '3', 'k', 'x', '\n']
```

<br>

개행 문자를 제거하기 위해 입력 받은 후 pop() 을 활용했다.



