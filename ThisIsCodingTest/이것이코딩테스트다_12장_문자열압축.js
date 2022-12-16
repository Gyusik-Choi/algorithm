const addWord = (word, cnt) => {
  return cnt === 1 ? word : cnt.toString() + word;
}

const getIdx = (i, length, s) => {
  let idx = i + length;

  if (idx > s.length) {
    idx = s.length;
  }

  return idx;
}

const solution = (s) => {
  if (s.length === 1) {
    return 1;
  }

  let answer = Infinity;
  let length = Math.floor(s.length / 2);;

  while (length > 0) {
    let word = s.slice(0, length);
    let words = '';
    let cnt = 1;

    for (let i = length; i < s.length; i += length) {
      let idx = getIdx(i, length, s);

      const targetWord = s.slice(i, idx);

      if (word === targetWord) {
        cnt += 1;
        continue;
      }

      words += addWord(word, cnt);
      word = targetWord;
      cnt = 1;
    }

    words += addWord(word, cnt);;
    answer = Math.min(answer, words.length);
    length -= 1;
  }

  return answer;
}

console.log(solution('a'));
console.log(solution('aabbaccc'));
console.log(solution('ababcdcdababcdcd'));
console.log(solution('abcabcdede'));
console.log(solution('abcabcabcabcdededededede'));
console.log(solution('xababcdcdababcdcd'));
// index 11 ~ 15
// 11 + 6 => 17

// 짝수
// aabb accc
// 8 -> 4

// 홀수
// aa bba
// 5 -> 2
