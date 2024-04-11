# LeetCode

## [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

이진탐색을 활용하는 문제다.

교재의 풀이를 참고해서 두번의 이진탐색으로 풀이했다.

<br>

### 최소값

정렬된 배열이 특정 지점을 기준으로 회전되었다. 최소값이 위치한 인덱스가 문제에서 말하는 pivot index 가 된다.

교재에서는 이 최소값을 이진 탐색으로 찾는데 어떻게 이진 탐색으로 회전된 배열에서 최소값을 찾을 수 있는지 이해하는데 시간이 걸렸다.

<br>

pivot index 오른쪽 요소들은 왼쪽 요소들보다 작다. mid 인덱스의 값이 right 인덱스의 값 보다 크다면 mid 를 포함한 왼쪽 요소들은 모두 right 인덱스의 값보다 크다. 이때 left 를 mid + 1 로 설정해야 한다. mid 이하는 모두 right 인덱스의 값보다 큰 값들만 있기 때문에 mid 다음 인덱스부터 탐색할 수 있도록 탐색 범위를 좁힌다.

만약에 mid 인덱스의 값이 right 인덱스의 값보다 같거나 작다면 mid 를 포함해서 mid 왼쪽에 더 작은 값이 있을 수 있다. mid 인덱스의 값이 최소값일 수 있어서 right 를 mid - 1 이 아니라 mid 로 설정하여 mid 도 탐색 범위에 포함되게 한다.

<br>

pivot index 를 찾는 코드는 bisect 모듈의 bisect_left 함수와 유사하다. 

bisect_left 함수는 찾는 숫자가 2개 이상인 경우 가장 왼쪽에 있는 인덱스를 리턴한다. 소스코드도 mid 를 리턴하지 않고 left 를 리턴하는 방식이라 교재의 방법과 상당히 유사하다.

<br>

### mid_pivot

교재에서 pivot index 를 구한 후 다시 이진 탐색을 하면서 mid_pivot 을 구해서 해당 인덱스를 기준으로 target 을 찾는다.

mid_pivot 은 회전하지 않고 정렬된 배열의 mid 값이다. mid_pivot 은 mid 에서 pivot index 만큼 더한 값에서 배열의 길이로 나눈 나머지 값이다. 배열의 길이로 나눠야 mid + pivot 이 배열의 인덱스를 벗어나지 않는다. mid_pivot 을 구해서 회전된 배열에서도 이진 탐색을 할 수 있도록 한다.

mid 에서 pivot index 를 더하는건 pivot index 를 기준으로 mid 만큼 이동한다는 의미다.

<br>

<참고>

파이썬 알고리즘 인터뷰

https://github.com/python/cpython/blob/3.9/Lib/bisect.py

