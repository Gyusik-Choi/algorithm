package com.example

class MaxHeap {
    private val elements = mutableListOf(-1)

    fun add(element: Int) {
        elements.add(element)
        shiftUp()
    }

    private fun shiftUp() {
        var idx = elements.size - 1
        while (idx > 1) {
            val parentIdx = idx / 2
            if (elements[parentIdx] < elements[idx]) {
                switch(parentIdx, idx)
                idx = parentIdx
            } else {
                break
            }
        }
    }

    private fun switch(parentIdx: Int, childIdx: Int) {
        val element = elements[parentIdx]
        elements[parentIdx] = elements[childIdx]
        elements[childIdx] = element
    }

    fun poll(): Int {
        if (elements.size <= 1) {
            throw IndexOutOfBoundsException()
        }
        switch(1, elements.size - 1)
        val maxElement = elements[elements.size - 1]
        maxHeapify(1)
        return maxElement
    }

    private fun maxHeapify(idx: Int) {
        var parentIdx = idx
        val leftChildIdx = idx * 2
        val rightChildIdx = idx * 2 + 1

        if (elements.size > leftChildIdx && elements[parentIdx] < elements[leftChildIdx]) {
            parentIdx = leftChildIdx
        }

        if (elements.size > rightChildIdx && elements[parentIdx] < elements[rightChildIdx]) {
            parentIdx = rightChildIdx
        }

        if (idx != parentIdx) {
            switch(idx, parentIdx)
            return maxHeapify(parentIdx)
        }
    }
}
