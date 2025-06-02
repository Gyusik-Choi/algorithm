package com.example

import org.assertj.core.api.Assertions
import kotlin.test.Test

class MaxHeapTest {
    @Test
    fun test_1() {
        val maxHeap = MaxHeap()
        maxHeap.add(0)
        maxHeap.add(1)
        maxHeap.add(2)
        maxHeap.add(3)
        maxHeap.add(4)
        Assertions.assertThat(maxHeap.poll()).isEqualTo(4)
    }

    @Test
    fun test_2() {
        val maxHeap = MaxHeap()
        maxHeap.add(5)
        maxHeap.add(1)
        maxHeap.add(2)
        maxHeap.add(3)
        maxHeap.add(4)
        Assertions.assertThat(maxHeap.poll()).isEqualTo(5)
    }

    @Test
    fun test_3() {
        val maxHeap = MaxHeap()
        Assertions
            .assertThatThrownBy { maxHeap.poll() }
            .isInstanceOf(IndexOutOfBoundsException::class.java)
    }

    @Test
    fun test_4() {
        val maxHeap = MaxHeap()
        maxHeap.add(0)
        maxHeap.add(1)
        maxHeap.add(2)
        maxHeap.add(3)
        maxHeap.add(4)

        maxHeap.poll()

        Assertions.assertThat(maxHeap.poll()).isEqualTo(3)
    }
}