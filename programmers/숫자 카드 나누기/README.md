# 프로그래머스

## 숫자 카드 나누기

최대 공약수를 활용해서 풀이했다.

모든 숫자를 비교해서 최대 공약수를 구해야 하는데 잘못 접근해서 정렬 후 작은 숫자 2개를 가지고 최대 공약수를 구한 뒤 리스트의 모든 요소를 나눌 수 있는지 판단했다. 최대 공약수 자체를 제대로 구하지 못해서 정답이 나올 수 없었다.

최대 공약수를 구하는 코드는 유클리드 호제법을 통해 구현했다.

<br>

<참고>

https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95

https://allmymight.tistory.com/198

https://hstory0208.tistory.com/entry/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv2-%EC%88%AB%EC%9E%90-%EB%82%98%EB%88%84%EA%B8%B0-%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C%ED%98%B8%EC%A0%9C%EB%B2%95