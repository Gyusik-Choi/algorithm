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

const bfs = function(n, k) {
  const q = new Queue()
  q.enQueue([n, k, 0])

  while (q) {
    const [soobin, sister, seconds] = q.deQueue()
    for (let i = 0; i < 3; i++) {
      if (soobin - 1 === sister || soobin + 1 === sister || soobin * 2 === sister) {
        return seconds + 1
      }

      // 이렇게 하면 안 된다. 이렇게 하면 for문 돌때마다 seconds값이 올라간다.
      // seconds += 1

      if (i === 0) {
        q.enQueue([soobin - 1, sister, seconds + 1])
      } else if (i === 1) {
        q.enQueue([soobin + 1, sister, seconds + 1])
      } else {
        q.enQueue([soobin * 2, sister, seconds + 1])
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
