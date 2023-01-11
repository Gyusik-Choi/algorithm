const setDp = (dp) => {
  for (let i = 0; i < N; i++) {
    if (isTodayConsultingPossible(i)) {
      dp[i] = consultingSchedule[i][1];
    }
  }
}

const getMaxProfit = () => {
  for (let i = 1; i < N; i++) {
    for (let j = 0; j < i; j++) {
      // 여기서 isTodayConsultingPossible 를 하면
      //
      // const input = [
      //   '4',
      //   '3 1',
      //   '1 100',
      //   '2 100',
      //   '1 1000',
      // ];
      //
      // 위와 같은 input 의
      // 1 100 를 제대로 처리하지 못한다
      // 당일은 상담이 가능한데
      // 앞의 3 1 때문에
      // 아래 if 조건에 포함되지 않아서
      // dp 값이 업데이트 되지 못한다
      // 그래서 setDp 에서
      // isTodayConsultingPossible 조건을 걸고
      // dp 값을 먼저 세팅해준다
      // 이때의 단점은 isTodayConsultingPossible 를
      // 2번 수행해야 한다
      if (isTodayConsultingPossible(i) && isConsultingPossible(j, i)) {
        dp[i] = Math.max(dp[i], dp[j] + consultingSchedule[i][1]);
      }
    }
  }

  return Math.max(...dp);
}

// 현재 날짜보다 이전 날짜들이
// 현재 날짜 기준으로 상담이 가능한지 여부
// 여기서 문제는 
// 예를 들어 마지막 날짜가 2 이상이면
// 실제로는 상담을 못한다
// 그래서 이런 날짜들을 포함하지 않기 위해
// isTodayConsultingPossible 에서 검사한다
const isConsultingPossible = (priorIdx, curIdx) => {
  return priorIdx + consultingSchedule[priorIdx][0] <= curIdx;
}

const isTodayConsultingPossible = (curIdx) => {
  return consultingSchedule[curIdx][0] + curIdx <= N;
}

// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const input = [
  '7',
  '3 10',
  '5 20',
  '1 10',
  '1 20',
  '2 15',
  '4 40',
  '2 200',
];
// => 45

// https://www.acmicpc.net/board/view/102008
// const input = [
//   '4',
//   '3 1',
//   '1 100',
//   '2 100',
//   '1 1000',
// ];
// => 1100

const N = parseInt(input.shift());
const consultingSchedule = input.map(v => v.split(' ').map(v => parseInt(v)));

const dp = Array.from(Array(N).fill(0));

// dp 에 초기값을 넣어준다
// 상담이 가능한 날짜에 대한 dp 초기값을 넣기 위해 
// isTodayConsultingPossible 조건에 해당하는 날짜만
// dp 값을 업데이트 한다
setDp(dp);

console.log(getMaxProfit());
