# 백준

## 1427

list.sort() 와 sorted(list)는 둘 다 리스트를 정렬해준다.

차이점은 list.sort()는 원본 리스트를 정리하는데 반환 값이 따로 없다. 원본에는 영향을 주나 새로 반환하는 것이 없다.

```python
arr = [2, 1, 3]
lst = arr.sort()
lst
# 아무것도 나오지 않는다.
type(lst)
# <class 'NoneType'>
arr
# [1, 2, 3]
```



sorted(list) 는 원본 리스트에는 영향을 주지 않고 새로운 리스트를 생성한다.

```python
arr = [2, 1, 3]
sorted(arr)
# [1, 2, 3]
# 새로운 리스트를 생성한다.
arr
# [2, 1, 3]
# 원본에는 영향을 주지 않는다.
```

```python
arr = [2, 1, 3]
lst = sorted(arr)
lst
# [1, 2, 3]
```



역순으로 정렬하려면 둘 다 reverse=True 를 입력해줘야 한다.

```python
arr = [2, 1, 3]
lst = sorted(arr, reverse=True)
lst
# [3, 2, 1]

arr.sort(reverse=True)
arr
# [3, 2, 1]
```

