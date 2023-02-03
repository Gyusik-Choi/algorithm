const checkSquare = function(val, idx) {
    const y = Math.floor(idx[0] / 3) * 3
    const x = Math.floor(idx[1] / 3) * 3

    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (arr[y + i][x + j] === val) {
                return false
            }
        }
    }
    return true
}

const checkVertical = function(val, idx) {
    const y = idx[0]
    const x = idx[1]

    for (let i = 0; i < 9; i++) {
        if (arr[i][x] === val) {
            return false
        }
    }
    return true
}

const checkHorizontal = function(val, idx) {
    const y = idx[0]
    const x = idx[1]
    
    for (let i = 0; i < 9; i++) {
        if (arr[y][i] === val) {
            return false
        }
    }
    
    return true
}

const findCandidate = function(idx) {
    let candidate = new Array(10).fill(0)

    const y = idx[0]
    const x = idx[1]
    // 가로
    for (let i = 0; i < 9; i++) {
        candidate[arr[y][i]] = 1
    }

    // 세로
    for (let i = 0; i < 9; i++) {
        candidate[arr[i][x]] = 1
    }

    // 작은 사각형
    const yI = Math.floor(y / 3) * 3
    const xJ = Math.floor(x / 3) * 3
    
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            candidate[arr[yI + i][xJ + j]] = 1
        }
    }

    let finalCandidate = []
    for (let i = 1; i < candidate.length; i++) {
        if (candidate[i] === 0) {
            finalCandidate.push(i)
        }
    }
    
    return finalCandidate
}

const sudoku = function(index) {
    if (index === zeroArr.length) {
        for (let i = 0; i < 9; i++) {
            console.log(arr[i].join(' '))
        }
        process.exit(0)
    } else {
        const idx = zeroArr[index]
        const candidates = findCandidate(idx)
        
        for (let j = 0; j < candidates.length; j++) {
            const item = candidates[j]
            // 1개 이상 0이 비어있는 경우가 있으므로 숫자가 2개 이상 겹치는게 없다면 진행해야함
            if (checkHorizontal(item, idx) && checkVertical(item, idx) && checkSquare(item, idx)) {
                arr[idx[0]][idx[1]] = item
                sudoku(index + 1)
                arr[idx[0]][idx[1]] = 0
            }
        }
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

let zeroArr = []
const arr = new Array(9).fill(0).map(v => new Array(9).fill(0))
for (let i = 0; i < 9; i++) {
    let oneArr = arr[i].split(' ').map(v => Number(v))
    for (let j = 0; j < 9; j++) {
        arr[i][j] = oneArr[j]
        if (arr[i][j] === 0) {
            zeroArr.push([i, j])
        }
    }
}

sudoku(0)