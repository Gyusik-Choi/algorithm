const populationMove = (m, vHistory, avg) => {
  vHistory.forEach((v, i) => m[v[0]][v[1]] = avg);
}

const isCanMove = (maps, start, end) => {
  const populationDifference = Math.abs(maps[start[0]][start[1]] - maps[end[0]][end[1]]);

  if (L <= populationDifference && populationDifference <= R) {
    return true;
  }

  return false;
}

// 인구 이동 있었다면 return true,
// 인구 이동 없었으면 return false,
const bfs = (maps, visit, go) => {
  const visitHistory = [go];
  const q = [go];
  // 첫 출발점 방문 처리
  visit[go[0]][go[1]] = true;

  let visitSums = maps[go[0]][go[1]];
  let visitCnt = 1;

  while (q.length > 0) {
    const start = q.shift();

    for (let i = 0; i < 4; i++) {
      const end = [start[0] + yValue[i], start[1] + xValue[i]];      

      if (0 > end[0] || end[0] >= N || 0 > end[1] || end[1] >= N) {
        continue;
      }

      if (visit[end[0]][end[1]]) {
        continue;
      }

      if (isCanMove(maps, start, end)) {
        // 방문 처리
        visit[end[0]][end[1]] = true;
        visitHistory.push(end);
        q.push(end);
        visitSums += maps[end[0]][end[1]];
        visitCnt += 1;
      }
    }
  }
  
  const populationAvg = Math.floor(visitSums / visitCnt);

  populationMove(maps, visitHistory, populationAvg);

  if (visitHistory.length === 1) {
    return false;
  }

  return true;
}

const getNewVisitedArr = () => {
  const visited = [];

  for (let i = 0; i < N; i++) {
    const temp = [];

    for (let j = 0; j < N; j++) {
      temp.push(false);
    }

    visited.push(temp);
  }

  return visited;
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '2 20 50',
//   '50 30',
//   '20 40'
// ];

// const input = [
//   '2 40 50',
//   '50 30',
//   '20 40'
// ];

// const input = [
//   '2 20 50',
//   '50 30',
//   '30 40',
// ];

// const input = [
//   '3 5 10',
//   '10 15 20',
//   '20 30 25',
//   '40 22 10',
// ];

// const input = [
//   '4 10 50',
//   '10 100 20 90',
//   '80 100 60 70',
//   '70 20 30 40',
//   '50 20 100 10'
// ];

const [N, L, R] = input[0].split(' ').map(v => parseInt(v));
input.shift();

const maps = input.map(v => v.split(' ').map(v => parseInt(v)));

const yValue = [-1, 0, 1, 0];
const xValue = [0, 1, 0, -1];

let days = 0;

while (true) {
  // 방문 기록 초기화
  const visited = getNewVisitedArr(N);
  // 한 번이라도 인구 이동 있었는지
  let isVisited = false;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (!visited[i][j]) {
        // 방문 처리
        visited[i][j] = true;

        // 탐색
        if (bfs(maps, visited, [i, j], N)) {
          isVisited = true;
        }
      }
    }
  }

  // 한 번이라도 인구 이동 없었다면 더 이상 인구 이동 X
  if (!isVisited) {
    break;
  }

  days += 1;
}

console.log(days);
