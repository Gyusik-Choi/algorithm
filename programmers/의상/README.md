# 프로그래머스

## 의상

경우의 수를 구하는 문제다.

옷 종류별 갯수의 누적곱을 구하면 되는데 옷을 입지 않는 경우도 고려해야 한다.

입지 않는 경우를 포함하기 위해 옷 종류별 갯수에서 1을 더한다.

모두 안 입는 경우는 포함되면 안 되기 때문에 누적곱에서 1을 빼준다.

<br>

그간 JavaScript, Dart 언어로는 reduce 함수를 사용해봤는데 Python 언어로 처음 reduce 함수를 사용해볼 수 있었다.

람다식으로 누적곱을 구하고 싶었는데 구할 방법을 찾지 못하다가 구글링으로 reduce 함수로 구할 수 있다는 것을 알게 됐다.

<br>

<참고>

https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/

https://stackoverflow.com/questions/13840379/how-can-i-multiply-all-items-in-a-list-together-with-python

https://github.com/python/cpython/blob/main/Lib/functools.py

