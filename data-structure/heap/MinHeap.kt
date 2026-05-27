package com.example

class MinHeap {
    private val list = mutableListOf(-1)

    fun add(num: Int) {
        list.add(num)
        shiftUp()
    }

    private fun shiftUp() {
        var childIdx = list.size - 1
        while (childIdx > 1) {
            val parentIdx = childIdx / 2
            if (list[parentIdx] > list[childIdx]) {
                val temp = list[parentIdx]
                list[parentIdx] = list[childIdx]
                list[childIdx] = temp
                childIdx = parentIdx
            } else {
                break
            }
        }
    }

    fun poll(): Int {
        if (list.size == 1) {
            throw NoSuchElementException("Heap is empty")
        }
        val temp = list[list.size - 1]
        list[list.size - 1] = list[1]
        list[1] = temp
        val pollItem = list.removeLast()
        shiftDown(1)
        return pollItem
    }

    private fun shiftDown(idx: Int) {
        var parentIdx = idx
        val leftIdx = parentIdx * 2
        val rightIdx = parentIdx * 2 + 1
        if (leftIdx < list.size && list[parentIdx] > list[leftIdx]) {
            parentIdx = leftIdx
        }
        if (rightIdx < list.size && list[parentIdx] > list[rightIdx]) {
            parentIdx = rightIdx
        }
        if (idx != parentIdx) {
            val temp = list[idx]
            list[idx] = list[parentIdx]
            list[parentIdx] = temp
            return shiftDown(parentIdx)
        }
    }
}