const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const T = parseInt(input[0])
let idx = 0
for (let i = 0; i < T; i++) {

    const NMK = input[idx + 1].split(' ').map(v => parseInt(v))
    // 공항의 수
    const N = NMK[0]
    // 총 지원비용
    const M = NMK[1]
    // 티켓정보의 수
    const K = NMK[2]


    for (let j = idx + 2; j < idx + 2 + K; j++) {
        const uvcd = input[j].split(' ').map(v => parseInt(v))
        // 출발공항
        const u = uvcd[0]
        // 도착공항
        const v = uvcd[1]
        // 비용
        const c = uvcd[2]
        // 소요시간
        const d = uvcd[3]
    }

    idx += 1 + K + 1
}

// 총 지원비용 안에서 최단 시간 구하기

// 참고
// https://maivve.tistory.com/226
