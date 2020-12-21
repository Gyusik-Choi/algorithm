# 백준

## 2750

문제 안내에 '시간 복잡도가 O(n²)인 정렬 알고리즘으로 풀 수 있습니다. 예를 들면 삽입 정렬, 거품 정렬 등이 있습니다.' 라고 되어있다.

삽입 정렬, 거품 정렬과 마찬가지로 시간 복잡도 O(n²)인 선택 정렬을 활용해서 풀이했다. 이중 for문을 돌게 되므로 시간 복잡도는 배열 길이가 n이라고 하면 n X n 만큼 비교가 일어나서 n제곱만큼의 시간 복잡도를 갖는다.

오름차순으로 정렬할 때, 거품 정렬은 매번 비교 할때마다 앞의 요소가 뒤의 요소보다 크면 교환해야 한다. 그러나 선택정렬은 바깥 for문의 아이템이 안쪽 for문을 다 돌고나서 한번만 교환하게 된다.



문제의 예제 입력으로 교환 횟수를 비교하면

```python
# 선택 정렬
def selection_sort(lst):
    global s_cnt
    for j in range(len(lst) - 1):
        min_idx = j
        for k in range(j + 1, len(lst)):
            if lst[min_idx] > lst[k]:
                min_idx = k
        lst[j], lst[min_idx] = lst[min_idx], lst[j]
        s_cnt += 1
    return lst


N = int(input())
arr = []
for i in range(N):
    num = int(input())
    arr.append(num)

s_cnt = 0
s_ans = selection_sort(arr)
print(s_cnt)
# 출력: 4
```

```python
# 거품 정렬
def bubble_sort(lst):
    global b_cnt
    for j in range(len(lst) - 1, -1, -1):
        for k in range(j):
            if lst[k] > lst[k + 1]:
                lst[k], lst[k + 1] = lst[k + 1], lst[k]
                b_cnt += 1
    return lst


N = int(input())
arr = []
for i in range(N):
    num = int(input())
    arr.append(num)

b_cnt = 0
b_ans = bubble_sort(arr)
print(b_cnt)
# 출력: 7
```



예제 입력은 숫자가 5, 2, 3, 4, 1 이렇게 총 5개다. 선택 정렬은 교환 횟수가 4번이고 거품 정렬은 7번이다. 입력 받는 숫자가 커지면 (물론 입력 받는 숫자에 따라 달라질 수 있지만) 그 차이는 더욱 커질 확률이 높다.

