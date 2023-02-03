const getDistance = (chicken, store) => {
  return Math.abs(chicken[0] - store[0]) + Math.abs(chicken[1] - store[1]);
}

const combination = (num, numLimit, cnt, cntLimit, store) => {
  if (cnt === cntLimit) {
    chickenStores.push([...store]);
  }

  for (let n = num; n < numLimit; n++) {
    store.push(n);
    combination(n + 1, numLimit, cnt + 1, cntLimit, store);
    store.pop();
  }
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '5 3',
//   '0 0 1 0 0',
//   '0 0 2 0 1',
//   '0 1 2 0 0',
//   '0 0 1 0 0',
//   '0 0 0 0 2'
// ];
// => 5

// const input = [
//   '5 2',
//   '0 2 0 1 0',
//   '1 0 1 0 0',
//   '0 0 0 0 0',
//   '2 0 0 1 1',
//   '2 2 0 1 2'
// ];
// => 10

// const input = [
//   '5 1',
//   '1 2 0 0 0',
//   '1 2 0 0 0',
//   '1 2 0 0 0',
//   '1 2 0 0 0',
//   '1 2 0 0 0'
// ];
// => 11

// const input = [
//   '5 1',
//   '1 2 0 2 1',
//   '1 2 0 2 1',
//   '1 2 0 2 1',
//   '1 2 0 2 1',
//   '1 2 0 2 1'
// ];
// => 32

const [N, M] = input[0].split(' ').map(v => parseInt(v));
input.shift();

const city = input.map(v => v.split(' ').map(v => parseInt(v)));

let numberOfChickenStores = 0;
const chickenStoresIdx = [];
const homeIdx = [];

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (city[i][j] === 0) {
      continue;
    }

    if (city[i][j] === 1) {
      homeIdx.push([i, j]);
      continue;
    }

    if (city[i][j] === 2) {
      numberOfChickenStores += 1;
      chickenStoresIdx.push([i, j]);
    }
  }
}

const chickenStores = [];
combination(0, numberOfChickenStores, 0, M, []);

// 치킨집 조합은 구했으나
// 도시가 어떤 치킨집을 선택할지 알 수 없다 
// => 하나씩 해보고 제일 거리 가까운 치킨집을 선택한다

let minDistance = Infinity;

// 치킨집 조합
for (const chickenStore of chickenStores) {
  // 하나의 치킨집 조합에 대한 거리 합
  let tempMinDistance = 0;

  // 집
  for (const home of homeIdx) {
    // 집에서 선택한 최소 거리 치킨집
    let tempMinDistanceForHome = Infinity;

    // 치킨 조합 중 하나의 치킨집
    for (const chicken of chickenStore) {
      tempMinDistanceForHome = Math.min(tempMinDistanceForHome, getDistance(chickenStoresIdx[chicken], home));
    }

    tempMinDistance += tempMinDistanceForHome;
  }

  minDistance = Math.min(minDistance, tempMinDistance);
}

console.log(minDistance);
