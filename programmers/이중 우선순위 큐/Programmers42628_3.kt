package com.example

class Programmers42628_3 {
    fun solution(operations: Array<String>): IntArray {
        val heap = IntervalHeap()
        for (o in operations) {
            val operation = o.split(" ")
            val action = operation[0]
            if (action == "I") {
                heap.add(operation[1].toInt())
            } else {
                if (heap.isEmpty()) {
                    continue
                }
                if (operation[1] == "-1") {
                    heap.pollMin()
                } else {
                    heap.pollMax()
                }
            }
        }
        if (heap.isEmpty()) {
            return intArrayOf(0, 0)
        }
        return intArrayOf(heap.getMax(), heap.getMin())
    }

    private class IntervalHeap {
        private val heap = mutableListOf(mutableListOf(-1, -1))

        fun isEmpty(): Boolean {
            return heap.size == 1
        }

        fun add(num: Int) {
            if (shouldAddArray()) {
                heap.add(mutableListOf(num))
            } else {
                heap[heap.lastIndex].add(num)
                if (isMinBiggerThanMax(heap.lastIndex)) {
                    switchElement(heap.lastIndex, 0, heap.lastIndex, 1)
                }
            }
            shiftUp()
        }

        private fun shouldAddArray(): Boolean {
            return heap.size == 1 || heap.last().size == 2
        }

        private fun shiftUp() {
            var curIdx = heap.lastIndex
            while (curIdx > 1) {
                val parentIdx = curIdx / 2
                if (heap[parentIdx].first() > heap[curIdx].first()) {
                    switchElement(parentIdx, 0, curIdx, 0)
                    curIdx = parentIdx
                } else if (heap[parentIdx].last() < heap[curIdx].last()) {
                    switchElement(parentIdx, 1, curIdx, heap[curIdx].lastIndex)
                    curIdx = parentIdx
                } else {
                    break
                }
            }
        }

        fun pollMin(): Int {
            // 첫번째와 마지막 인덱스의 첫번째 요소를 교환하고 마지막 인덱스의 첫번째 요소를 제거
            // 첫번째 인덱스의 첫번째 요소 위치 조정
            switchElement(1, 0, heap.lastIndex, 0)
            val num = heap.last().removeFirst()
            if (heap.last().isEmpty()) {
                heap.removeLast()
            }
            shiftDownMin(1)
            return num
        }

        private fun shiftDownMin(idx: Int) {
            var parentIdx = idx
            val leftChildIdx = parentIdx * 2
            val rightChildIdx = parentIdx * 2 + 1
            if (heap.size > leftChildIdx && heap[parentIdx].first() > heap[leftChildIdx].first()) {
                parentIdx = leftChildIdx
            }
            if (heap.size > rightChildIdx && heap[parentIdx].first() > heap[rightChildIdx].first()) {
                parentIdx = rightChildIdx
            }
            if (idx != parentIdx) {
                switchElement(idx, 0, parentIdx, 0)
                shiftDownMin(parentIdx)
            }
        }

        fun pollMax(): Int {
            switchElement(1, heap[1].lastIndex, heap.lastIndex, heap.last().lastIndex)
            val num = heap.last().removeLast()
            if (heap.last().isEmpty()) {
                heap.removeLast()
            }
            shiftDownMax(1)
            return num
        }

        private fun shiftDownMax(idx: Int) {
            var parentIdx = idx
            val leftChildIdx = parentIdx * 2
            val rightChildIdx = parentIdx * 2 + 1
            if (heap.size > leftChildIdx && heap[parentIdx].last() < heap[leftChildIdx].last()) {
                parentIdx = leftChildIdx
            }
            if (heap.size > rightChildIdx && heap[parentIdx].last() < heap[rightChildIdx].last()) {
                parentIdx = rightChildIdx
            }
            if (idx != parentIdx) {
                switchElement(idx, 1, parentIdx, heap[parentIdx].lastIndex)
                shiftDownMax(parentIdx)
            }
        }

        private fun isMinBiggerThanMax(idx: Int): Boolean {
            return heap.size > idx && heap[idx].size == 2 && heap[idx][0] > heap[idx][1]
        }

        private fun switchElement(idx1: Int, elementIdx1: Int, idx2: Int, elementIdx2: Int) {
            val temp = heap[idx1][elementIdx1]
            heap[idx1][elementIdx1] = heap[idx2][elementIdx2]
            heap[idx2][elementIdx2] = temp
        }

        fun getMin(): Int {
            return heap[1][0]
        }

        fun getMax(): Int {
            return heap[1].last()
        }
    }
}
