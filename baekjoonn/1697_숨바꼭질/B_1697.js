// 추가할 사항
// 방문체크 배열을 통해 중복된 요소가 큐에 들어가는 것을 막아주기
// https://chanhuiseok.github.io/posts/baek-14/
// https://hsp1116.tistory.com/20

const Node = function(value, next = null) {
  this.value = value
  this.next = next
}

const Queue = function() {
  this.head = new Node(null)
  this.tail = this.head
}

Queue.prototype.isEmpty = function() {
  return this.head.value === null && this.tail.value === null
}

Queue.prototype.enQueue = function(value) {
  if (this.isEmpty()) {
    this.head = new Node(value)
    this.tail = this.head
  } else {
    const tail = this.tail
    this.tail = new Node(value)
    tail.next = this.tail
  }
}

Queue.prototype.deQueue = function() {
  if (this.isEmpty() === false) {
    const popNumber = this.head.value

    // Queue의 길이가 1
    if (this.head === this.tail) {
      this.head = new Node(null)
      this.tail = this.head
    // Queue의 길이가 2 이상
    } else {
      this.head = this.head.next
    }

    return popNumber
  }
}

const bfs = function(n, sister) {
  const q = new Queue()
  q.enQueue([n, 0])
  let visited = new Array(100001).fill(false)
  visited[n] = true

  while (q) {
    // let [soobin, seconds] = q.deQueue()
    // 위의 경우 for문 바깥에 soobin이 있기 때문에 for문을 돌때마다 값이 누적돼서 변경이 되므로 for문 안에서 soobin을 선언했다
    const item = q.deQueue()
    
    for (let i = 0; i < 3; i++) {
      let soobin = item[0]
      let seconds = item[1]
    
      if (soobin - 1 === sister || soobin + 1 === sister || soobin * 2 === sister) {
        return seconds + 1
      }

      // 이렇게 하면 안 된다. 이렇게 하면 for문 돌때마다 seconds값이 올라간다.
      // seconds += 1

      if (i === 0) {
        soobin -= 1
      } else if (i === 1) {
        soobin += 1
      } else {
        soobin *= 2
      }

      if (0 <= soobin && soobin <= 100000 && visited[soobin] === false) {
        visited[soobin] = true
        q.enQueue([soobin, seconds + 1])
      }
    }
  }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ')

const N = parseInt(input[0])
const K = parseInt(input[1])

if (N > K) {
  console.log(N - K)
} else if (N === K) {
  console.log(0)
} else {
  const answer = bfs(N, K)
  console.log(answer)
}
