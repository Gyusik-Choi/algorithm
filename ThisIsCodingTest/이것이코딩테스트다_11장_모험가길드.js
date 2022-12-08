const N = 5;
const adventurers = [2, 3, 1, 2, 2];
adventurers.sort((a, b) => a - b);

let answer = 0;
let cnt = 0;

adventurers.forEach((v, i) => {
    cnt += 1;

    if (cnt == v) {
        answer += 1;
        cnt = 1;
    }
})

console.log(answer)
