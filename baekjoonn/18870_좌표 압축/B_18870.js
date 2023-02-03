const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = Number(input[0])
const originArr = input[1].split(' ').map(v => Number(v))
const arr = originArr.slice()
const setArr = [...new Set(arr)]
const sortedArr = setArr.sort((a, b) => {
    return a - b
})

let obj = {}
for (let i = 0; i < sortedArr.length; i++) {
    obj[sortedArr[i]] = i
}

let answer = ''
for (let i = 0; i < N; i++) {
    const idx = String(obj[originArr[i]])
    answer += idx + " "
}
console.log(answer)