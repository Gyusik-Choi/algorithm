const isCorrectWord = (u) => {
  let stack = [];

  for (const char of u) {
    if (char === '(') {
      stack.push('(');
      continue;
    }

    // ')'
    if (stack.length === 0) {
      return false;
    }

    stack.pop();
  }

  return true;
}

const splitWord = (w) => {
  let u = '';
  let v = '';

  let leftParenthesisCnt = 0;
  let rightParenthesisCnt = 0;

  for (let i = 0; i < w.length; i++) {
    const char = w[i];

    u += char;

    if (char === '(') {
      leftParenthesisCnt += 1;
    } else {
      rightParenthesisCnt += 1;
    }

    if (leftParenthesisCnt !== 0 && rightParenthesisCnt !== 0 && leftParenthesisCnt === rightParenthesisCnt) {
      v = w.split('').filter((c, idx) => idx > i).join('');

      break;
    }
  }

  return [u, v];
}

const solution = (p) => {
  if (p.length === 0) {
    return '';
  }

  // 분리
  let [u, v] = splitWord(p);

  // 올바른 괄호 문자열 여부
  // 올바른 괄호 문자열이면 v 로 solution 재귀 수행
  if (isCorrectWord(u)) {
    return u + solution(v);
  };

  // 올바른 괄호 문자열이 아니면 ( 생성
  let word = '(';

  // v 로 solution 재귀 수행
  word += solution(v);

  // ) 붙이기
  word += ')';

  // u 의 첫번째 문자와 마지막 문자 제거
  // 나머지 문자열의 괄호 방향 뒤집어서 뒤에 붙이기
  // -> 주의할점은 괄호 방향을 뒤집는게 전체를 reverse 하는게 아니라
  //    loop 를 돌면서 각각의 괄호 방향을 바꿔줘야 한다
  // https://school.programmers.co.kr/questions/20512
  word += u.split('').filter((char, idx) => idx !== 0 && idx !== u.length - 1).map(v => v === ')' ? '(' : ')').join('');

  // return 문자열
  return word;
}

console.log(solution("(()())()"));
console.log(solution(")("));
console.log(solution("()))((()"));
console.log(solution("()"));
console.log(solution("))))(((("));
console.log(solution("))()(("));
console.log(solution(")()()()("));
