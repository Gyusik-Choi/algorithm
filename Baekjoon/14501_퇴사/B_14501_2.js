const setDp = (dp) => {
  for (let i = 0; i < N; i++) {
    dp[i] = consultingSchedule[i][1];
  }
}

const getMaxProfit = () => {
  for (let i = 1; i < N; i++) {
    for (let j = 0; j < i; j++) {
      if (isConsultingPossible(j, i)) {
        dp[i] = Math.max(dp[i], dp[j] + consultingSchedule[i][1]);
      }
    }
  }

  return getMaxDp(dp);
}

// 현재 날짜보다 이전 날짜들이
// 현재 날짜 기준으로 상담이 가능한지 여부
// 여기서 문제는 
// 예를 들어 마지막 날짜가 1 이상이면
// 실제로는 상담을 못한다
// 그래서 이런 부분 날짜들을 포함하지 않기 위해
// isTodayConsultingPossible 에서 처리한다
const isConsultingPossible = (priorIdx, curIdx) => {
  return priorIdx + consultingSchedule[priorIdx][0] <= curIdx;
}

// 해당 날짜가 상담 가능한 날인지 여부
const isTodayConsultingPossible = (curIdx) => {
  return consultingSchedule[curIdx][0] + curIdx <= N;
}

const getMaxDp = (dp) => {
  let maxSums = 0;

  for (let i = 0; i < N; i++) {
    if (isTodayConsultingPossible(i)) {
      maxSums = Math.max(maxSums, dp[i]);
    }
  }

  return maxSums;
}

// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = [
//   '7',
//   '3 10',
//   '5 20',
//   '1 10',
//   '1 20',
//   '2 15',
//   '4 40',
//   '2 200',
// ];
// => 45

// https://www.acmicpc.net/board/view/102008
const input = [
  '4',
  '3 1',
  '1 100',
  '2 100',
  '1 1000',
];
// => 1100

const N = parseInt(input.shift());
const consultingSchedule = input.map(v => v.split(' ').map(v => parseInt(v)));

const dp = Array.from(Array(N).fill(0));

// dp 에 초기값을 넣어준다
// isTodayConsultingPossible 함수를 여러번 호출하지 않기 위해
// 일단 여기서 isTodayConsultingPossible 를 호출하지 않고
// 모든 날짜에 대한 dp 초기값을 넣어준다
// 그리고 getMaxProfit 에서도 isTodayConsultingPossible 를 조건에 포함하지 않고
// 마지막에 값을 구할때 isTodayConsultingPossible 로 구분한다
// getMaxProfit 에 isTodayConsultingPossible 를 넣더라도
// getMaxDp 에서 또 isTodayConsultingPossible 를 해줘야 한다
// setDp 에서 isTodayConsultingPossible 를 하지 않아서
//
// const input = [
//   '7',
//   '3 10',
//   '5 20',
//   '1 10',
//   '1 20',
//   '2 15',
//   '4 40',
//   '2 200',
// ];
//
// 2 20 같은 입력값이 실제로는 상담이 안되는 날짜지만
// dp 에 포함된다
// 그래서 dp 에 이미 포함되기 때문에
// 결국 getMaxDp 에서 isTodayConsultingPossible 를 해줘야 한다
// 
// setDp 에서 isTodayConsultingPossible 를 하더라도
// getMaxProfit 나 getMaxDp 둘 중 하나에서 isTodayConsultingPossible 를 해줘야 해서
// isTodayConsultingPossible 를 한번만 하기 위해
// getMaxDp 에서 isTodayConsultingPossible 를 처리한다
setDp(dp);

console.log(getMaxProfit());
