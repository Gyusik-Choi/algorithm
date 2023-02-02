const getAscii = (doSkip, char, limit) => {
  let asciiIdx = char.charCodeAt() - 97;
  
  let num = 0;

  while (num < limit) {
    asciiIdx = (asciiIdx + 1) % 26;

    // 해당 인덱스의 값이 false 라면 1 더해준다
    if (!doSkip[asciiIdx]) {
      num += 1;
    }
  }

  return asciiIdx + 97;
}

const solution = (s, skip, index) => {
  const isSkip = new Array(26).fill(false);

  for (const c of skip) {
    isSkip[c.charCodeAt() - 97] = true;
  }

  let answer = '';

  for (const c of s) {
    answer += String.fromCharCode(getAscii(isSkip, c, index));
  }

  return answer;
}

console.log(solution("aukks", "wbqd", 5));
// 아스키번호
// a ~ z
// 97 ~ 122
