function paint(curBW, counterBW, v, h) {
    let cnt = 0
    for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            if ((i + v) % 2 === 0) {
                if ((j + h) % 2 === 0) {
                    if (arr[i + v][j + h] !== curBW) {
                        cnt++
                    }
                } else {
                    if (arr[i + v][j + h] !== counterBW) {
                        cnt++
                    }
                }
            } else {
                if ((j + h) % 2 === 0) {
                    if (arr[i + v][j + h] !== counterBW) {
                        cnt++
                    }
                } else {
                    if (arr[i + v][j + h] !== curBW) {
                        cnt++
                    }
                }
            }
        }
    }
    if (minPaint > cnt) {
        minPaint = cnt
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

let nums = input[0].split(' ').map(v => Number(v))
let N = nums[0]
let M = nums[1]

// let arr = new Array(M).fill(0).map(v => new Array(N).fill(v))
let arr = []

// input에서 배열 받아놨다. 이걸 반복문 돌면서 새로운 2차원 배열에 옮기기
for (let i = 1; i < input.length; i++) {
    let row = input[i].split('')
    arr.push(row)
}

let vertical = N - 8
let horizontal = M - 8

let minPaint = 65
for (let k = 0; k < 2; k++) {        
    for (let i = 0; i <= vertical; i++) {
        for (let j = 0; j <= horizontal; j++) {
            if (k === 0) {
                paint("B", "W", i, j)        
            } else {
                paint("W", "B", i, j)
            }
            
        }
    }
}

console.log(minPaint)