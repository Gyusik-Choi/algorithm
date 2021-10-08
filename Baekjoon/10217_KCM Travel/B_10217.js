const MinHeap = function() {
    this.arr = [null]

    MinHeap.prototype.insert = function(item) {
        this.arr.push(item)
    
        let idx = this.arr.length - 1
        while (idx > 1) {
            if (this.arr[Math.floor(idx / 2)][0] > this.arr[idx][0]) {
                let temp = this.arr[idx]
                this.arr[idx] = this.arr[Math.floor(idx / 2)]
                this.arr[Math.floor(idx / 2)] = temp
    
                idx = Math.floor(idx / 2)
            } else {
                break
            }
        }
    }
    
    MinHeap.prototype.remove = function() {
        if (this.arr.length < 2) {
            return
        }
    
        if (this.arr.length < 3) {
            const item = this.arr.pop()
            return item
        }
        
        let temp = this.arr[this.arr.length - 1]
        this.arr[this.arr.length - 1] = this.arr[1]
        this.arr[1] = temp
    
        const item = this.arr.pop()
        this.minHeapify(1)
        return item
    }
    
    MinHeap.prototype.minHeapify = function(idx) {
        let parentIdx = idx
            let leftChildIdx = idx * 2
            let rightChildIdx = idx * 2 + 1
    
            if (parentIdx * 2 < this.arr.length && this.arr[parentIdx][0] > this.arr[leftChildIdx][0]) {
                parentIdx = leftChildIdx
            } 
    
            if (parentIdx * 2 + 1 < this.arr.length && this.arr[parentIdx][0] > this.arr[rightChildIdx][0]) {
                parentIdx = rightChildIdx
            }
    
            if (parentIdx != idx) {
                let temp = this.arr[parentIdx]
                this.arr[parentIdx] = this.arr[idx]
                this.arr[idx] = temp
    
                return this.minHeapify(parentIdx)
            }
    }
}

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
    
    let arr = new Array(N + 1).fill(0).map(v => new Array())
    
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

        arr[u].push([v, c, d])
    }

    let dp = new Array(N + 1).fill(Infinity).map(v => new Array(M + 1).fill(Infinity))
    dp[1][0] = 0

    let mh = new MinHeap()
    // 출발, 비용, 시간
    mh.insert([1, 0, 0])

    while (mh.arr.length > 1) {
        const vertex = mh.remove()
        const start = vertex[0]
        const price = vertex[1]
        const time = vertex[2]
        
        if (dp[start][price] < time) {
            continue
        }

        arr[start].forEach((item) => {
            const e = item[0]
            const money = item[1]
            const duration = item[2]

            const nextPrice = price + money
            const nextTime = time + duration

            if (nextPrice > M) {
                return
            }

            if (dp[e][nextPrice] <= nextTime) {
                return
            }

            for (let k = nextPrice; k <= M; k++) {
                if (dp[e][k] > nextTime) {
                    dp[e][k] = nextTime
                } else {
                    break
                }
            }
            mh.insert([e, nextPrice, nextTime])
        })
    }
    
    if (dp[N][M] === Infinity) {
        console.log("Poor KCM")
    } else {
        console.log(dp[N][M])
    }
    idx += 1 + K
}

// 참고
// https://maivve.tistory.com/226
// https://kibbomi.tistory.com/178
// https://www.acmicpc.net/source/26477152
// https://www.acmicpc.net/board/view/63079
// https://www.acmicpc.net/source/25869168