const Node = function(value, next = null) {
    this.value = value
    this.next = next
}

const Queue = function() {
    this.head = new Node(null)
    this.tail = this.head
}

Queue.prototype.isEmpty = function() {
    return this.head.value === null
}

Queue.prototype.enQueue = function(item) {
    if (this.isEmpty()) {
        this.head = new Node(item)
        this.tail = this.head
    } else {
        const tail = this.tail
        this.tail = new Node(item)
        tail.next = this.tail
    }
}

Queue.prototype.deQueue = function() {
    if (this.isEmpty() === false) {
        const popItem = this.head.value

        if (this.head === this.tail) {
            this.head = new Node(null)
            this.tail = this.head
        } else {
            this.head = this.head.next
        }

        return popItem
    }
}

const bfs = function(n, sister) {
    const queue = new Queue()
    queue.enQueue([n, 0])

    let visited = new Array(sister + 2).fill(false)
    visited[n] = true

    while (queue.isEmpty() === false) {
        // let [soobin, seconds] = queue.deQueue()
        // 위처럼 하면 안 된다
        // 아래 반복문을 돌때 값이 위의 soobin에서 계산되는게 아니라
        // 누적된 값으로 계산된다
        // i === 1 일때 soobin += 1이 
        // 실제로는 soobin -= 1 이 수행된 값에서 1이 더해지게 된다
        
        // 또 한가지 주의할점은 ReferenceError 가 나지 않도록
        // const item = queue.deQueue()
        // if (soobin === sister) {
        //     return seconds
        // }
        // 이렇게 되면 안 된다
        // soobin, seconds 는 디스트럭처링을 이 보다 아래의 반복문에서 수행하므로
        // 값을 찾을 수 없다

        const item = queue.deQueue()
        if (item[0] === sister) {
            return item[1]
        }

        for (let i = 0; i < 3; i++) {
            let [soobin, seconds] = item

            if (i === 0) {
                soobin -= 1
            } else if (i === 1) {
                soobin += 1
            } else {
                soobin *= 2
            }

            if (0 <= soobin && soobin <= sister + 1) {
                if (visited[soobin] === false) {
                    visited[soobin] = true
                    queue.enQueue([soobin, seconds + 1])
                }
            }
        }
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ')
const [N, K] = input.map(v => Number(v))

if (N === K) {
    console.log(0)
} else if (N > K) {
    console.log(N - K)
} else {
    console.log(bfs(N, K))
}
