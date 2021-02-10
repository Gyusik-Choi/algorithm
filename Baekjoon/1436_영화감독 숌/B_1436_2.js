const fs = require('fs')
const N = Number(fs.readFileSync('/dev/stdin'))

let n = N
let num = 666
while (n > 0) {
    let stringNum = String(num)
    // includes 는 true 혹은 false 를 반환(ES6 이상에서 적용 가능)
    if (stringNum.includes("666") === true) {
        n--
    }
    num++
}
console.log(num - 1)

// 참고
// https://enzycut.tistory.com/entry/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EB%AC%B8%EC%9E%90%EC%97%B4%EC%97%90%EC%84%9C-%EB%AC%B8%EC%9E%90-%ED%8F%AC%ED%95%A8-%EC%97%AC%EB%B6%80