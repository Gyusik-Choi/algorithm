const move = (info, sums) => {
  const copiedFishInfo = getCopiedFishInfo(info);

  // 물고기 이동
  moveFish(copiedFishInfo);

  // 상어 현재 위치
  const curShark = getSharkIdx(copiedFishInfo);

  // 상어가 이동할 수 있는 위치
  const moveSharkIdxes = getPossibleMoveSharkIdxes(curShark);

  if (moveSharkIdxes.length === 0) {
    maxSums = Math.max(maxSums, sums);
    return;
  }

  // 상어 이동 (완전 탐색)
  for (const futureShark of moveSharkIdxes) {
    const fishValue = moveShark(copiedFishInfo, curShark, futureShark);

    move(copiedFishInfo, sums + fishValue);
  }
}

const getCopiedFishInfo = (copiedInfo) => {
  const copiedFishInfo = [];

  for (let i = 0; i < 4; i++) {
    const tempCopiedFishInfo = [];

    for (let j = 0; j < 4; j++) {
      const oneCopiedFishInfo = [];

      for (let k = 0; k < 2; k++) {
        oneCopiedFishInfo.push(copiedInfo[i][j][k]);
      }

      tempCopiedFishInfo.push(oneCopiedFishInfo);
    }

    copiedFishInfo.push(tempCopiedFishInfo);
  }

  return copiedFishInfo;
}

const moveFish = (copiedInfo) => {
  let fishNumber = 1;

  while (fishNumber < 17) {
    const fishIdx = getFishIdx(copiedInfo, fishNumber);

    fishNumber += 1;

    if (fishIdx.length === 0) {
      continue;
    }

    const moveFishIdx = getPossibleMoveFishIdx(copiedInfo, fishIdx);

    if (moveFishIdx.length === 0) {
      continue;
    }

    changeFish(copiedInfo, fishIdx, moveFishIdx);
  }
}

const getFishIdx = (copiedInfo, fishNum) => {
  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < 4; j++) {
      if (copiedInfo[i][j][0] === fishNum) {
        return [i, j];
      }
    }
  }

  return [];
}

const getPossibleMoveFishIdx = (copiedInfo, fish) => {
  const [i, j] = fish;

  let curFishDirection = copiedInfo[i][j][1];

  const yValue = [-1, -1, 0, 1, 1, 1, 0, -1];
  const xValue = [0, -1, -1, -1, 0, 1, 1, 1];

  for (let k = 0; k < 8; k++) {
    const idx = (k + curFishDirection - 1) % 8;

    const y = i + yValue[idx];
    const x = j + xValue[idx];
    
    // 공간의 경계를 넘는다면
    if (0 > y || y >= 4 || 0 > x || x >= 4) {
      continue;
    }

    // 상어가 있는 칸이라면
    if (copiedInfo[y][x][0] === -1) {
      continue;
    }

    // 현재 물고기 위치의 방향 정보 갱신
    // idx 는 0 ~ 7 범위고
    // 방향 정보는 1 ~ 8 범위라
    // idx 에서 1을 더한 값을 넣어준다
    copiedInfo[i][j][1] = idx + 1;

    return [y, x];
  }

  return [];
}

const changeFish = (copiedInfo, a, b) => {
  const temp = copiedInfo[a[0]][a[1]];
  copiedInfo[a[0]][a[1]] = copiedInfo[b[0]][b[1]];
  copiedInfo[b[0]][b[1]] = temp;
}

const getSharkIdx = (copiedInfo) => {
  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < 4; j++) {
      if (copiedInfo[i][j][0] === -1) {
        return [i, j];
      }
    }
  }
}

const getPossibleMoveSharkIdxes = (shark) => {
  const possibleMoveSharkIdxes = [];
  
  // 값을 누적해서 구하므로 바꿔줘야 한다
  let [y, x] = shark;

  const sharkDirection = fishInfo[y][x][1];

  const yValue = [-1, -1, 0, 1, 1, 1, 0, -1];
  const xValue = [0, -1, -1, -1, 0, 1, 1, 1];

  for (let i = 0; i < 3; i++) {
    y += yValue[sharkDirection - 1];
    x += xValue[sharkDirection - 1];

    // 공간의 경계를 넘는다면
    if (0 > y || y >= 4 || 0 > x || x >= 4) {
      continue;
    }

    // 빈칸이라면
    if (fishInfo[y][x][0] === 0) {
      continue;
    }

    if (0 < fishInfo[y][x][0] && fishInfo[y][x][0] <= 16) {
      possibleMoveSharkIdxes.push([y, x]);
    }
  }

  return possibleMoveSharkIdxes;
}

const moveShark = (copiedInfo, cur, future) => {
  const [curY, curX] = cur;
  const [futureY, futureX] = future;

  const fishValue = copiedInfo[futureY][futureX][0];

  // 상어가 있던 위치는 빈칸으로
  copiedInfo[curY][curX][0] = 0;

  // 상어가 이동
  // 상어의 방향 값 이동한 위치의 방향 값으로 가져간다
  copiedInfo[futureY][futureX][0] = -1;

  return fishValue;
}


// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const input = [
  '7 6 2 3 15 6 9 8',
  '3 1 1 8 14 7 10 1',
  '6 1 13 6 4 3 11 4',
  '16 1 8 7 5 2 12 2',
];
// => 33

// const input = [
//   '16 7 1 4 4 3 12 8',
//   '14 7 7 6 3 4 10 2',
//   '5 2 15 2 8 3 6 4',
//   '11 8 2 4 13 5 9 4',
// ];
// => 43

const fishInfo = [];

input.map(v => {
  const f = v.split(' ').map(v => parseInt(v));

  const temp = [];

  for (let i = 0; i < 8; i += 2) {
    temp.push([f[i], f[i + 1]]);
  }

  fishInfo.push(temp);
});

let maxSums = fishInfo[0][0][0];

// 빈칸 0, 상어 -1
fishInfo[0][0][0] = -1;

move(fishInfo, maxSums);

console.log(maxSums);
