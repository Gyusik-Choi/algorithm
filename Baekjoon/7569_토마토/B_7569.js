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
  if (this.isEmpty() === false) {
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

const bfs = function(candidates) {
  let q = new Queue()
  candidates.forEach((candidate) => q.enQueue(candidate))

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

  idx += N
  fullBoxes.push(oneBox)
}

let maxDays = 1
let bfsCandidates = []
for (let i = 0; i < H; i++) {
  for (let j = 0; j < N; j++) {
      for (let k = 0; k < M; k++) {
          if (fullBoxes[i][j][k] === 1) {
              bfsCandidates.push([i, j, k])
          }
      }
  }
}

// dfs가 아니라 bfs다
// 1인 숫자가 나올때마다 bfs를 바로 실행시키면 너비 우선 탐색인 bfs가 제대로 동작하지 못한다
// 1인 숫자들을 모아서 한번에 bfs를 실행해야 먼저 들어간 1인 숫자들이 하나씩 큐에서 나오면서 bfs를 제대로 실행시킬 수 있다
// 이 문제에서 오답이 나왔던 이유 중 하나가 위의 bfsCandidates.push([i, j, k]) 코드 부분을 bfs(i, j, k)로 수행했기 때문이다
// 현재는 위와 같이 수정하여 1인 정보들을 모아서 bfs를 실행할때 인자로 넣어준다
bfs(bfsCandidates)
const result = isZero()
console.log(result === true ? -1 : maxDays - 1)
