# 백준

## 칸토어 집합

재귀로 풀이했다.

3 의 n 제곱 만큼의 길이의 - 를 조건에 맞게 변환해야 한다. 가운데 문자열은 공백으로 바꾸는데 이를 모든 - 의 길이가 1일 때까지 반복해야 한다.

가운데 문자열을 공백으로 바꾼 후 가운데를 기준으로 앞, 뒤의 문자열을 재귀호출해서 가운데 문자열을 공백으로 바꾸는 작업을 반복한다.

문자열의 길이가 1이 되면 재귀호출을 종료한다. 재귀호출 하는 부분에서 결과 값을 받아서 최종적으로 앞 문자열에 대한 재귀호출의 결과값, 가운데 문자열을 변환한 값, 그리고 뒤 문자열에 대한 재귀호출의 결과값을 더해서 리턴한다.


