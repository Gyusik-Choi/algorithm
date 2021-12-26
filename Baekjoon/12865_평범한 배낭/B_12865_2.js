const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

// 동적계획법 문제다
// 문제의 아이디어는 우선 최대 무게와 주어진 물건 갯수를 바탕으로 2차원 배열을 만들어서
// 물건 하나를 했을때 최대 무게 - 물건 무게를 충족하는 경우에만 물건을 더 담는 방식을 활용해보려고 한다