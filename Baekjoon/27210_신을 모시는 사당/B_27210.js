const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '5',
//   '1 1 2 1 2',
// ];

// const input = [
//   '2',
//   '1 2',
// ];

// const input = [
//   '1',
//   '2',
// ];

const N = parseInt(input.shift());
const stoneStatues = input[0].split(' ').map(v => parseInt(v));

let maxAwakening = 0;

let leftWayStatueSums = 0;

for (let statue of stoneStatues) {
  leftWayStatueSums += statue = statue === 1 ? 1 : -1;

  if (leftWayStatueSums < 0) leftWayStatueSums = 0;

  maxAwakening = Math.max(maxAwakening, leftWayStatueSums);
}

let rightWayStatueSums = 0;

for (let statue of stoneStatues) {
  rightWayStatueSums += statue = statue === 1 ? -1 : 1;

  if (rightWayStatueSums < 0) rightWayStatueSums = 0;

  maxAwakening = Math.max(maxAwakening, rightWayStatueSums);
}

console.log(maxAwakening);

// 참고
// https://nahwasa.com/entry/%EC%87%BC%EB%AF%B8%EB%8D%94%EC%BD%94%EB%93%9C-3%ED%9A%8C-%EB%B0%B1%EC%A4%80-27210-%EC%8B%A0%EC%9D%84-%EB%AA%A8%EC%8B%9C%EB%8A%94-%EC%82%AC%EB%8B%B9-%EC%9E%90%EB%B0%94-java

