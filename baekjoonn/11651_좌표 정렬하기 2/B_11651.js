const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
let arr = []
for (let i = 1; i <= N; i++) {
    const temp = input[i].split(" ").map(v => Number(v))
    arr.push(temp)
}

arr.sort((a, b) => {
    if (a[1] !== b[1]) {
        return a[1] - b[1]
    } else {
        return a[0] - b[0]
    }
})

let sortedArr = ''
for (let i = 0; i < N; i++) {
    sortedArr += `${arr[i][0]} ${arr[i][1]}\n`
}
console.log(sortedArr)
