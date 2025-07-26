package com.example

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

class TaskScheduler621_WrongTest {
    private val t = TaskScheduler621_Wrong()

    @Test
    fun leastInterval_1() {
        Assertions
            .assertThat(
                t.leastInterval(
                    charArrayOf('A', 'A', 'A', 'B', 'B', 'B'),
                    2
                )
            )
            .isEqualTo(8)

    }

    @Test
    fun leastInterval_2() {
        Assertions
            .assertThat(
                t.leastInterval(
                    charArrayOf('A', 'C', 'A', 'B', 'D', 'B'),
                    1
                )
            )
            .isEqualTo(6)

    }

    @Test
    fun leastInterval_3() {
        Assertions
            .assertThat(
                t.leastInterval(
                    charArrayOf('A', 'A', 'A', 'B', 'B', 'B'),
                    3
                )
            )
            .isEqualTo(10)

    }

    @Test
    fun leastInterval_4() {
        Assertions
            .assertThat(
                t.leastInterval(
                    charArrayOf('A', 'A'),
                    2
                )
            )
            .isEqualTo(4)

    }

    @Test
    fun leastInterval_5() {
        Assertions
            .assertThat(
                t.leastInterval(
                    charArrayOf('A', 'B', 'A'),
                    2
                )
            )
            .isEqualTo(4)
    }

    @Test
    fun leastInterval_6() {
        Assertions
            .assertThat(
                t.leastInterval(
                    charArrayOf('B', 'A', 'B'),
                    2
                )
            )
            .isEqualTo(4)
    }

    @Test
    fun leastInterval_7() {
        t.leastInterval(
            charArrayOf('B', 'C', 'D', 'A', 'A', 'A', 'A', 'G'),
            1
        )
        Assertions
            .assertThat(
                t.leastInterval(
                    charArrayOf('B', 'C', 'D', 'A', 'A', 'A', 'A', 'G'),
                    1
                )
            )
            .isEqualTo(8)
    }
}
