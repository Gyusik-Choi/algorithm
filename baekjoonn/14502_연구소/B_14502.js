const countSafeArea = (maps) => {
  let safeArea = 0;

  maps.forEach((area, i) => {
    area.forEach((section, i) => {
      if (section === 0) {
        safeArea += 1;
      }
    })
  })

  return safeArea;
}

const spreadVirus = (maps, virus) => {
  const yValue = [-1, 0, 1, 0];
  const xValue = [0, 1, 0, -1];

  for (const v of virus) {
    // 값 복사 되지 않도록 주의
    const q = [[...v]];

    let idx = 0;

    while (q.length > idx) {
      const [virusY, virusX] = q[idx];

      idx += 1;

      for (let i = 0; i < 4; i++) {
        const y = virusY + yValue[i];
        const x = virusX + xValue[i];

        if (0 > y || y >= N || 0 > x || x >= M) {
          continue;
        }

        if (maps[y][x] === 0) {
          // 바이러스
          maps[y][x] = 2;
          q.push([y, x]);
        }
      }
    }
  }
}

const getCopiedMaps = (maps) => {
  const newMaps = [];

  maps.forEach((v, i) => {
    newMaps.push([...v]);
  });

  return newMaps;
}

const setWall = (maps, comb) => {
  const [y, x] = emptySpace[comb];
  maps[y][x] = 1;
}

const getCombinations = (num, numLimit, cnt, cntLimit, comb) => {
  if (cnt === cntLimit) {
    // 값 복사 되지 않도록 주의
    combinations.push([...comb]);
    return;
  }

  for (let n = num; n < numLimit; n++) {
    comb.push(n);
    getCombinations(n + 1, numLimit, cnt + 1, cntLimit, comb);
    comb.pop();
  }
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//     '7 7',
//     '2 0 0 0 1 1 0',
//     '0 0 1 0 1 2 0',
//     '0 1 1 0 1 0 0',
//     '0 1 0 0 0 0 0',
//     '0 0 0 0 0 1 1',
//     '0 1 0 0 0 0 0',
//     '0 1 0 0 0 0 0'
// ];
// => 27

// const input = [
//     '4 6',
//     '0 0 0 0 0 0',
//     '1 0 0 0 0 2',
//     '1 1 1 0 0 2',
//     '0 0 0 0 0 2'
// ];
// => 9

// const input = [
//   '8 8',
//   '2 0 0 0 0 0 0 2',
//   '2 0 0 0 0 0 0 2',
//   '2 0 0 0 0 0 0 2',
//   '2 0 0 0 0 0 0 2',
//   '2 0 0 0 0 0 0 2',
//   '0 0 0 0 0 0 0 0',
//   '0 0 0 0 0 0 0 0',
//   '0 0 0 0 0 0 0 0'
// ];
// => 3

// const input = [
//   '4 3',
//   '2 0 0',
//   '2 0 0',
//   '2 0 1',
//   '0 1 0'
// ]
// => 3
// https://www.acmicpc.net/board/view/18602

// const input = [
//   '3 3',
//   '0 0 0',
//   '0 0 0',
//   '0 0 0'
// ]
// => 6
// https://www.acmicpc.net/board/view/19384

const [N, M] = input[0].split(' ').map(v => parseInt(v));
input.shift();

// 직사각형에 주의
const maps = input.map(v => v.split(' ').map(v => parseInt(v)));

const emptySpace = [];
const wall = [];
const virus = [];

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    switch (maps[i][j]) {
      case 0:
        emptySpace.push([i, j]);
        break;
      case 1:
        wall.push([i, j]);
        break;
      default:
        virus.push([i, j]);
        break;
    }
  }
}

const combinations = [];
getCombinations(0, emptySpace.length, 0, 3, []);

let maxSafeArea = 0;

for (const combination of combinations) {
  const newMaps = getCopiedMaps(maps)
  
  for (const comb of combination) {
    setWall(newMaps, comb);
  }

  spreadVirus(newMaps, virus);

  maxSafeArea = Math.max(maxSafeArea, countSafeArea(newMaps));
}

console.log(maxSafeArea);
