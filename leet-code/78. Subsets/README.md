# LeetCode

## 78. Subsets

모든 부분집합을 구하는 문제다.

재귀 호출이 일어날 때마다 요소를 리스트에 더한다. 순서는 구분하지 않기 때문에 중복이 일어나지 않도록 재귀 호출시 for 문의 인덱스를 1씩 늘린다.

결과에 빈 리스트도 나와야 하는데 이는 재귀 호출을 하는 함수를 처음 호출할 때 추가된 요소가 없어서 빈 리스트가 더해진다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

