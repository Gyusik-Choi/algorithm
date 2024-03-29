# 이것이 코딩테스트다

## 챕터 12 10번 자물쇠와 열쇠

#### python

카카오 코딩테스트 기출문제로서 구현 유형의 문제다.

풀이하는데 굉장히 오래 걸렸다. 삽질도 여러번 하면서 '이것이 코딩테스트다' 교재의 답안에서 제시한 방법으로 접근해서 해결할 수 있었다.

가로와 세로를 각각 열쇠 길이 + 열쇠 길이 + 자물쇠 길이 만큼으로 하는 배열을 생성하고 배열의 가운데에 자물쇠 정보를 넣어준다. 이렇게 되면 열쇠가 바깥에서부터 자물쇠와 맞물리는 모든 경우를 체크할 수 있다.

자물쇠와 열쇠가 둘 다 0이거나 1인 경우는 열 수 없는 경우라 자물쇠와 열쇠가 맞물리는 부분은 합해서 1이 돼야 한다.

배열의 1 인덱스부터 자물쇠와 열쇠 길이 - 1까지 2차원 for 문을 돌면서 맞물리는 부분을 체크할 수 있다.

```python
for i in range(1, key_length + lock_length):
    for j in range(1, key_length + lock_length):
        # 키의 크기 만큼 자물쇠의 영역과 더해주고
        # 자물쇠가 위치한 가운데의 숫자를 체크한다
        # 다음 위치를 검사하기 위해 더한 부분을 다시 빼준다
```

<br>

첫 탐색인 i, j가 (1, 1)인 부분은 자물쇠의 왼쪽 상단 첫번째칸과 딱 한칸만 겹치게 되고, 마지막 탐색인 (key_length + lock_length - 1, key_length + lock_length - 1)은 오른쪽 하단 마지막칸과 딱 한칸만 겹치게 된다.

배열(한 변을 열쇠 길이 + 열쇠 길이 + 자물쇠 길이로 만든 전체 배열)에서 키의 영역만큼 자물쇠의 값과 더해준다. 그리고 배열에서 자물쇠의 영역을 검사하면 키의 영역과 자물쇠의 영역이 겹친 부분만 실제로는 합해지고 나머지는 기존 자물쇠의 값을 유지하게 된다.

키로 자물쇠를 열 수 있는지를 봐야하므로 더하는 것은 키의 영역만큼하되 검사는 자물쇠의 영역만큼을 검사해야 한다.

자물쇠 영역의 모든 숫자가 1이면 자물쇠를 열 수 있다.

<br>

#### javascript

3차원 배열을 통해 [[[key, lock], [key, lock] ...]] key, lock 값을 비교했다.

key, lock 이 모두 1 이거나, key, lock 이 모두 0 이거나, 혹은 lock 이 0인데 home 이 1 이 아닌 경우는 모두 false 로 처리했다.

<br>

이번 문제를 3차원 배열로 접근하면서 예상치 못한 배열 동작을 확인할 수 있었다. 배열의 값이 예상과 다르게 변화하길래 한참을 디버깅한 끝에 3차원 이상의 배열을 만들때, 배열 리터럴과 Array.from, new Array 간의 차이를 발견할 수 있었다.

배열 리터럴과 달리 나머지 두 방식은 값이 복사되는 현상이 발생했다.

```javascript
const arr = [[[-1, -1], [-1, -1], [-1, -1]], [[-1, -1], [-1, -1], [-1, -1]], [[-1, -1], [-1, -1], [-1, -1]]];
const arr = new Array(3).fill(0).map(v => new Array(3).fill([-1, -1]));
const arr = Array.from(Array(3).fill(0), () => new Array(3).fill([-1, -1]));

arr[0][0][1] = 1;
console.log(arr);
```

<br>

```javascript
// 배열 리터럴
[
  [ [ -1, 1 ], [ -1, -1 ], [ -1, -1 ] ],
  [ [ -1, -1 ], [ -1, -1 ], [ -1, -1 ] ],
  [ [ -1, -1 ], [ -1, -1 ], [ -1, -1 ] ]
]
```

<br>

```javascript
// new Array, Array.from
// 배열 리터럴과 달리 
// [0][0][1] 만 바뀌는게 아니라 나머지 [0][1][1], [0][2][1] 의 값도 바뀐다...
[
  [ [ -1, 1 ], [ -1, 1 ], [ -1, 1 ] ],
  [ [ -1, -1 ], [ -1, -1 ], [ -1, -1 ] ],
  [ [ -1, -1 ], [ -1, -1 ], [ -1, -1 ] ]
]
```



<br>

<참고>

이것이 코딩테스트다

https://velog.io/@tjdud0123/자물쇠와-열쇠-2020-카카오-공채-python

