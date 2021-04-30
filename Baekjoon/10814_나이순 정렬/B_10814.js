const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = Number(input[0])
let arr = new Array(N)
for (let i = 1; i <= N; i++) {
    let item = input[i].split(' ')
    arr[i - 1] = item
}

let sortedArr = []
for (let i = 1; i < 201; i++) {
    for (let j = 0; j < N; j++) {
        if (Number(arr[j][0]) === i) {
            sortedArr.push(arr[j])
        }
    }
    if (sortedArr.length === arr.length) {
        break
    }
}

let answer = ''
for (let i = 0; i < N; i++) {
    answer += `${sortedArr[i][0]} ${sortedArr[i][1]}` + '\n'
}
console.log(answer)