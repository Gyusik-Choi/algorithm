const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const n = Number(input[0])
const sequence = input[1].split(' ').map(v => Number(v))

// 문제의 아이디어가 쉽게 떠오르지 않아 좀 더 고민중