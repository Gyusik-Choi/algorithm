// Queue 는 Singly Linked List 형태로 구현

const Node = function(value, next = null) {
  this.value = value
  this.next = next
}

const Queue = function() {
  this.head = new Node(null)
  this.tail = this.head
}

Queue.prototype.isEmpty = function() {
  if (this.head.value === null && this.tail.value === null) {
      return true
  }
  return false
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
  if (!this.isEmpty()) {
    const popNumber = this.head.value
    if (this.head === this.tail) {
      this.head = new Node(null)
      this.tail = this.head
    } else {
    // 요소가 하나만 있을 경우 이때 this.head가 this.head.next가 되면서 아예 this.head가 null이 되버린다
    // 그렇게 되면 isEmpty 메서드에서 this.head.value를 조회할 수 없다
    // 아예 null이라 value나 next 프로퍼티가 없다
    // 그러면 해결할 수 있는 방법 중 하나는 요소가 하나만 있을 경우와 그것보다 많은 경우로 분기하는 것이다
    // this.head와 this.tail을 비교한다(this.head.value와 this.tail.value를 비교하는게 아니다)
    // 요소 하나일때만 this.head와 this.tail이 같을 수 있다
    // this.head.value와 this.tail.value는 같을 수 있더라도 
    // next 프로퍼티의 값이 this.head.next는 이 다음 요소를 가리키고 있고, this.tail.next는 null인 상태다
      this.head = this.head.next
    }

    return popNumber
  }
}

const isZero = function() {
  for (let i = 0; i < H; i++) {
    for (let j = 0; j < N; j++) {
      for (let k = 0; k < M; k++) {
        if (fullBoxes[i][j][k] === 0) {
          return true
        }
      }
    }
  }
  return false
}

const bfs = function(z, y, x) {
  let q = new Queue()
  q.enQueue([z, y, x])

  const zDirection = [-1, 1, 0, 0, 0, 0]
  const yDirection = [0, 0, -1, 0, 1, 0]
  const xDirection = [0, 0, 0, 1, 0, -1]

  while (q.isEmpty() === false) {
      const [zAxis, yAxis, xAxis] = q.deQueue()

      for (let m = 0; m < 6; m++) {
          const zWay = zDirection[m] + zAxis
          const yWay = yDirection[m] + yAxis
          const xWay = xDirection[m] + xAxis

          if (0 <= zWay && zWay < H && 0 <= yWay && yWay < N && 0 <= xWay && xWay < M) {
              if (fullBoxes[zWay][yWay][xWay] === 0) {
                  fullBoxes[zWay][yWay][xWay] = fullBoxes[zAxis][yAxis][xAxis] + 1
                  maxDays = Math.max(maxDays, fullBoxes[zWay][yWay][xWay])
                  q.enQueue([zWay, yWay, xWay])
              }
          }
      }

  }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
const [M, N, H] = input[0].split(' ').map(v => Number(v))

let fullBoxes = []
let idx = 0
for (let i = 0; i < H; i++) {
  let oneBox = []

  for (let j = 0; j < N; j++) {
      const box = input[idx + 1 + j].split(' ').map(v => Number(v))
      oneBox.push(box) 
  }

  idx += 3
  fullBoxes.push(oneBox)
}

let maxDays = 0
for (let i = 0; i < H; i++) {
  for (let j = 0; j < N; j++) {
      for (let k = 0; k < M; k++) {
          if (fullBoxes[i][j][k] === 1) {
              bfs(i, j, k)
          }
      }
  }
}

console.log(isZero() ? -1 : maxDays - 1)

