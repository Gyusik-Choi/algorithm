const Node = function(value, next = null) {
    this.value = value;
    this.next = next;
}

const Queue = function() {
    this.head = new Node(null);
    this.tail = this.head;
}

Queue.prototype.isEmpty = function() {
    return this.head.value === null;
}

Queue.prototype.enQueue = function(value) {
    if (this.isEmpty()) {
        this.head = new Node(value);
        this.tail = this.head;
    } else {
        const tail = this.tail;
        this.tail = new Node(value);
        tail.next = this.tail;
    }
}

Queue.prototype.deQueue = function() {
    if (this.isEmpty() === false) {
        const popItem = this.head.value;

        if (this.head === this.tail) {
            this.head = new Node(null);
            this.tail = this.head;    
        } else {
            this.head = this.head.next;
        }

        return popItem;
    }
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const T = parseInt(input[0]);
let idx = 1;
for (let i = 0; i < T; i++) {
    const isValidRange = function(y, x) {
        if (0 <= y && y < chessBoardLength && 0 <= x && x < chessBoardLength) {
            return true;
        }

        return false;
    }

    const bfs = function(yStart, xStart) {
        const q = new Queue();
        q.enQueue([yStart, xStart]);

        chessBoard[yStart][xStart] = 1;

        const yDirection = [-2, -1, 1, 2, 2, 1, -1, -2];
        const xDirection = [1, 2, 2, 1, -1, -2, -2, -1];

        while (q.isEmpty() === false) {
            const [y, x] = q.deQueue();

            if (y === yTo && x === xTo) {
                return chessBoard[y][x] - 1;
            }

            for (let j = 0; j < 8; j++) {
                const yIdx = y + yDirection[j];
                const xIdx = x + xDirection[j];

                if (isValidRange(yIdx, xIdx)) {
                    if (chessBoard[yIdx][xIdx] === 0) {
                        chessBoard[yIdx][xIdx] = chessBoard[y][x] + 1;
                        q.enQueue([yIdx, xIdx]);
                    }
                }
            }

        }
        
    }

    const chessBoardLength = parseInt(input[idx]);
    const departure = input[idx + 1].split(' ').map(v => parseInt(v));
    const destination = input[idx + 2].split(' ').map(v => parseInt(v));

    let chessBoard = new Array(chessBoardLength).fill(0).map(v => new Array(chessBoardLength).fill(0));
    const [yFrom, xFrom] = departure;
    const [yTo, xTo] = destination;

    if (yFrom === yTo && xFrom === xTo) {
        console.log(0);
    } else {
        console.log(bfs(yFrom, xFrom));
    }

    idx += 3;
}