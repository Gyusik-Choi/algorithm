S = '02984';
const numbers = S.split('').map(v => parseInt(v));

let sums = numbers[0];

for (let i = 1; i < numbers.length; i++) {
    const number = numbers[i];

    // 더하기
    // 곱했을 때 0 일 경우, number 가 1일 경우
    if (sums * number === 0 || number === 1) {
        sums += number;
        continue;
    }

    sums *= number;
}

console.log(sums);
