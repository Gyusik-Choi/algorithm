const sortCallBack = (a, b) => {
  if (a[1] === b[1]) {
    if (a[2] === b[2]) {
      if (a[3] === b[3]) {
        // a[0], b[0] 은 정수가 아니라 문자열이기 때문에
        // a[0] - b[0] 이렇게 뺄셈으로 정렬을 수행할 수 없고
        // 대소 비교를 통해 -1, 1 등을 return 해야 한다
        return a[0] > b[0] ? 1 : -1;
      }

      return b[3] - a[3];
    }

    return a[2] - b[2];
  }

  return b[1] - a[1];
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '12',
//   'Junkyu 50 60 100',
//   'Sangkeun 80 60 50',
//   'Sunyoung 80 70 100',
//   'Soong 50 60 90',
//   'Haebin 50 60 100',
//   'Kangsoo 60 80 100',
//   'Donghyuk 80 60 100',
//   'Sei 70 70 70',
//   'Wonseob 70 70 90',
//   'Sanghyun 70 70 80',
//   'nsj 80 80 80',
//   'Taewhan 50 60 90',
// ];

const N = parseInt(input[0]);
input.shift();

const grades = input.map(grade => grade.split(' ').map((g, i) => i > 0 ? parseInt(g) : g));
grades.sort(sortCallBack);

// https://tesseractjh.tistory.com/53
// console.log 를 매번 하는 것에서
// 한번만 하는 것으로 변경해서 시간 초과에 걸리지 않을 수 있었다
const answer = [];
grades.forEach((grade) => answer.push(grade[0]));
console.log(answer.join('\n'));

// const a = ['Junkyu', 'Haebin'];
// a.sort((a, b) => a > b ? 1 : -1);
// console.log(a)

// const b = [10, 2];
// b.sort((a, b) => a - b);
// console.log(b);
