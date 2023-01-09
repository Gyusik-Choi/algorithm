const isPossibleToUnlock = (arr, lockLength, i, j) => {
  // 0 홈, 1 돌기
  // [key, lock]
  // lock 영역을 전체 검사해야 한다
  // [1, 1] 이 있으면 안 된다 => 돌기와 돌기가 만나면 안 된다
  // [0, 0] 도 안 된다 => 자물쇠의 홈을 채우지 못함
  // lock 이 0 인데 home 이 1이 아니면 안 된다
  // lock 이 0 이면 home 이 무조건 1이어야 한다

  for (let y = i; y < i + lockLength; y++) {
    for (let x = j; x < j + lockLength; x++) {
      if (arr[y][x][0] === 1 && arr[y][x][1] === 1) {
        return false;
      }

      if (arr[y][x][0] !== 1 && arr[y][x][1] === 0) {
        return false;
      }
    }
  }

  return true;
}

const getArray = (key, lock, i, j) => {
  const m = key.length;
  const n = lock.length;
  const length = (n + (m - 1) * 2);

  // [key, lock];
  // const arr = new Array(length).fill([-1, -1]).map(v => new Array(length).fill([-1, -1]));
  // 위의 방법을 하게 되면 [0][0][1] 로 접근하더라도 [0]번 인덱스의 0부터 length 인덱스의 모든 1번 인덱스가 동시에 바뀐다
  // Array.from 으로 생성한 배열도 마찬가지였다
  // 2차원 배열은 reference 방식으로 생성되는 듯 하다
  const arr = new Array(length);
  for (let y = 0; y < length; y++) {
    arr[y] = [];
    for (let x = 0; x < length; x++) {
      arr[y].push([-1, -1]);
    }
  }

  // lock 배치 (lock 위치는 고정)
  // lock 시작 인덱스는 m - 1
  for (let y = 0; y < n; y++) {
    for (let x = 0; x < n; x++) {
      arr[m - 1 + y][m - 1 + x][1] = lock[y][x]
    }
  }

  // key 배치 (y, x 축 값 필요)
  for (let y = 0; y < m; y++) {
    for (let x = 0; x < m; x++) {
      arr[i + y][j + x][0] = key[y][x];
    }
  }

  return arr;
}

const rotateKey = (key) => {
  const keyLength = key.length;
  const newKey = new Array(keyLength).fill(0).map(v => new Array(keyLength).fill(0));

  for (let i = 0; i < keyLength; i++) {
    for (let j = 0; j < keyLength; j++) {
      newKey[j][keyLength - 1 - i] = key[i][j];
    }
  }

  return newKey;
}

const solution = (key, lock) => {
  const m = key.length;
  const n = lock.length;
  const length = (n + (m - 1) * 2);

  // 총 루프
  // 회전 4회 * 가로 길이 * 세로 길이
  for (let k = 0; k < 4; k++) {
    // https://dapsu-startup.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9E%90%EB%AC%BC%EC%87%A0%EC%99%80-%EC%97%B4%EC%87%A0-%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8JavaScript
    key = k === 0 ? key : rotateKey(key);

    for (let i = 0; i < length - m + 1; i++) {
      for (let j = 0; j < length - m + 1; j++) {
        const newArray = getArray(key, lock, i, j);

        if (isPossibleToUnlock(newArray, n, m - 1, m - 1)) {
          return true;
        }
      }
    }
  }

  return false;
}

// console.log(solution([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]));
// => false
console.log(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]));
// => true
// console.log(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1]]));
// => true
// console.log(solution([[0, 1, 0], [1, 0, 0], [0, 0, 1]], [[1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1]]));
// => true

// const arr = [[[-1, -1], [-1, -1], [-1, -1]], [[-1, -1], [-1, -1], [-1, -1]], [[-1, -1], [-1, -1], [-1, -1]]];
// const arr = new Array(3).fill(0).map(v => new Array(3).fill([-1, -1]));
// const arr = Array.from(Array(3).fill(0), () => new Array(3).fill([-1, -1]));
// 배열 리터럴과 달리 값이 복사된다...
// arr[0][0][1] = 1;
// console.log(arr);
// [
//   [ [ -1, 1 ], [ -1, -1 ], [ -1, -1 ] ],
//   [ [ -1, -1 ], [ -1, -1 ], [ -1, -1 ] ],
//   [ [ -1, -1 ], [ -1, -1 ], [ -1, -1 ] ]
// ]

// [
//   [ [ -1, 1 ], [ -1, 1 ], [ -1, 1 ] ],
//   [ [ -1, -1 ], [ -1, -1 ], [ -1, -1 ] ],
//   [ [ -1, -1 ], [ -1, -1 ], [ -1, -1 ] ]
// ]