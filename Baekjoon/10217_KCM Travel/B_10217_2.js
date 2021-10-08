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

const T = Number(input[0])
let idx = 0
for (let i = 0; i < T; i++) {

  const [N, M, K] = input[idx + 1].split(' ').map(Number)
  
  let arr = new Array(N + 1).fill(0).map(v => new Array())
  
  for (let j = idx + 2; j < idx + 2 + K; j++) {
      const [u, v, c, d] = input[j].split(' ').map(Number)

      arr[u].push([v, c, d])
  }

  let dp = new Array(N + 1).fill(Infinity).map(v => new Array(M + 1).fill(Infinity))
  dp[1][0] = 0

  let mh = new MinHeap()
  mh.insert([0, 0, 1])
  
  let answer = -1
  
  while (mh.arr.length > 1) {
      const vertex = mh.remove()
      const time = vertex[0]
      const price = vertex[1]
      const start = vertex[2]

      if (time > dp[start][price]) {
          continue
      }
      
      if (start === N) {
          answer = time
          break
      }

      arr[start].forEach((item) => {
          const [e, money, duration] = item

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
          
          mh.insert([nextTime, nextPrice, e])
      })
  }

  if (answer === -1) {
      console.log("Poor KCM")
  } else {
      console.log(dp[N][M])
  }
  
  idx += 1 + K
}