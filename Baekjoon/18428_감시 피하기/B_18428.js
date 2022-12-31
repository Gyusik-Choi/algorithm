// 완전탐색 + DFS

const findStudent = (corridor, t, dir) => {
  const [y, x] = t;

  // 학생을 찾거나 벽에 부딪히거나 범위를 벗어나면 종료
  // ? 가는길에 다른 선생님 있으면 ?
  const [yIdx, xIdx] = [y + yValue[dir], x + xValue[dir]];

  // 범위를 벗어났거나
  if (0 > yIdx || yIdx >= N || 0 > xIdx || xIdx >= N) {
    return false;
  }

  if (corridor[yIdx][xIdx] === 'S') {
    return true;
  }

  if (corridor[yIdx][xIdx] === 'O') {
    return false;
  }
  
  return findStudent(corridor, [yIdx, xIdx], dir);
}

const putObstacles = (newCorridor, comb) => {
  for (let i = 0; i < comb.length; i++) {
    const idx = comb[i];

    const [y, x] = emptySpaces[idx];

    newCorridor[y][x] = 'O';
  }
}

const getNewCorridor = (corridor) => {
  const newCorridor = [];

  for (let i = 0; i < N; i++) {
    const corridorRow = [];

    for (let j = 0; j < N; j++) {
      corridorRow.push(corridor[i][j]);
    }

    newCorridor.push(corridorRow);
  }

  return newCorridor;
}

const getObstacleCombinations = (num, numLimit, cnt, cntLimit, comb) => {
  if (cnt === cntLimit) {
    emptySpacesCombinations.push([...comb]);
    return;
  }

  for (let n = num; n < numLimit; n++) {
    comb.push(n);
    getObstacleCombinations(n + 1, numLimit, cnt + 1, cntLimit, comb);
    comb.pop();
  }
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '5',
//   'X S X X T',
//   'T X S X X',
//   'X X X X X',
//   'X T X X X',
//   'X X T X X'
// ];

// const input = [
//   '4',
//   'S S S T',
//   'X X X X',
//   'X X X X',
//   'T T T X'
// ];

// const input = [
//   '5',
//   'X X S X X',
//   'X X X X X',
//   'S X T X S',
//   'X X X X X',
//   'X X S X X'
// ];
// NO

// const input = [
//   '5',
//   'X T X T X',
//   'T X S X T',
//   'X S S S X',
//   'T X S X X',
//   'X T X X X'
// ];
// YES

// const input = [
//   '5',
//   'X S S S X',
//   'T X X S X',
//   'X T X S X',
//   'X X T X S',
//   'X X X T X'
// ];
// YES

const N = parseInt(input[0]);
input.shift();

const teachers = [];
const emptySpaces = [];

const corridor = input.map(v => v.split(' '));
corridor.forEach((c, y) => c.forEach((v, x) => v === 'X' ? emptySpaces.push([y, x]) : v === 'T' ? teachers.push([y, x]) : null));

const emptySpacesCombinations = [];
getObstacleCombinations(0, emptySpaces.length, 0, 3, []);

const yValue = [-1, 0, 1, 0];
const xValue = [0, 1, 0, -1];

// 하나의 조합당
// 선생님 한 명씩
// 4 방향으로 이동해서 학생 찾기

// true 로 설정을 해두고
// 어떤 하나의 조합에서
// 끝까지 학생을 못 찾으면
// false 로 변경하고 종료한다
// for 문 안에서 변수들에 false 를 설정한 것과 반대
let findStudentResult = true;

for (const comb of emptySpacesCombinations) {
  let findStudentTempResult = false;

  const newCorridor = getNewCorridor(corridor);

  putObstacles(newCorridor, comb);

  // 선생님들 중 한명이라도 학생을 찾는지
  for (const teacher of teachers) {
    let findStudentPerTeacherResult = false;

    for (let direction = 0; direction < 4; direction++) {
      if (findStudent(newCorridor, teacher, direction)) {
        findStudentPerTeacherResult = true;
        break;
      }
    }

    // 선생님 중 한명이라도 학생을 찾으면
    // 해당 조합은 실패
    if (findStudentPerTeacherResult) {
      findStudentTempResult = true;
      break;
    }
  }

  if (!findStudentTempResult) {
    findStudentResult = false;
    break;
  }
}

console.log(!findStudentResult ? 'YES' : 'NO');
