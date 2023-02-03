// 2차원 배열 안에 배열들이 들어있고
// 배열들의 요소 갯수가 각각 다르면서
// 갯수가 몇 개인지 모를 때의
// 정렬을 구현해 보았다

// 이를 궁금하게 된 것은
// 파이썬의 heap 내부 코드를 보면
// 요소 간의 비교를 < 로 수행하는데
// 파이썬은 요소가 여러개 일지라도 < 로
// 정렬이 제대로 수행되는데
// 자바스크립트에서는 그렇지 못하다
// 예를 들어
// [11, 2] < [2, 2] 는
// 파이썬은 False, 자바스크립트는 true 다

// 이전에 자바스크립트로 직접 구현해본 heap 은
// 요소가 하나일 경우 혹은
// 요소가 배열일 경우 갯수가 정해져 있으면
// 제대로 구현이 가능했는데
// 배열이 몇 개 인지 모를 경우에는
// 정렬을 어떻게 구현해야 할지를 모르겠어서
// 이 경우에 대비한 정렬을 구현해보게 됐다

const sortCallBack = function(a, b) {
  const aLength = a.length;
  const bLength = b.length;

  for (let i = 0; i < Math.min(aLength, bLength); i++) {
    if (a[i] < b[i]) {
      return -1;
    } else if (a[i] > b[i]) {
      return 1;
    } else {
      const copiedA = JSON.parse(JSON.stringify(a));
      const copiedB = JSON.parse(JSON.stringify(b));

      copiedA.shift();
      copiedB.shift();
      
      const result = sortCallBack(copiedA, copiedB);
      return result;
    }
  }

  if (aLength === 0 && bLength > 0) {
    return -1;
  }

  if (aLength > 0 && bLength === 0) {
    return 1;
  }
}

export default sortCallBack;

// const a = [[1, 1, 3], [1, 1, 2], [1, 1, 1], [1, 1, 4]];
// const a = [[1, 1, 3], [1, 1], [1, 1, 2], [1, 1, 1], [1, 1, 4]];
// const a = [[1, 1, 3], [1, 1]];
// const a = [[1, 2], [2, 2], [2], [2, 1], [9]];
// const a = [[1, 2, 3, 4], [1, 2, 3, 1]];
// a.sort(sortCallBack);
// console.log(a);
