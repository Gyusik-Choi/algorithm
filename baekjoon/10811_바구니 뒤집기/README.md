# 백준

## 10811

### B_10811.py

basket 배열 외에 temp 배열을 하나 더 두고 temp 배열의 값을 basket 에 대입하는 방식으로 진행했다.

입력 받은 바구니 번호 보다 앞의 번호는 그대로 temp 배열에 넣고 입력 받은 바구니 번호는 역순으로 temp 배열에 넣고 입력 받은 바구니 번호 보다 뒤의 번호는 그대로 temp 배열에 넣었다. 그리고 temp 배열의 값을 basket 에 대입한다. 이 과정을 반복하고 basket 배열을 출력했다.

<br>

### B_10811_2.py

투포인터 방식을 활용했다. 

입력 받은 i, j 가 같아지기 전까지 서로의 인덱스에 해당하는 값을 교체하고 i 는 1 증가, j 는 1 감소 시켰다.

<br>

<참고>

https://codecollector.tistory.com/427

