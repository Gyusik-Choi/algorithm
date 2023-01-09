const getAnswer = (word) => {
    const upperCase = [];
    let sums = 0;

    word.split('').map(char => {
        const asciiValue = char.charCodeAt();

        if (asciiValue >= 65 && asciiValue <= 90) {
            upperCase.push(char);
        } else {
            sums += parseInt(char);
        }
    });

    upperCase.sort();

    if (sums > 0) {
        return upperCase.join('') + sums.toString();
    }

    return upperCase.join('')
}

// const input = 'K1KA5CB7';
// https://github.com/ndb796/python-for-coding-test/blob/master/12/2.py
// input 이 0일 경우 출력 X
// const input = '0';
// const input = '321CBA';
// 아래의 input 에서 ABC0 으로 출력되는 오류가 있어서 위의 코드 수정
// const input = 'CBA';
console.log(getAnswer(input));

