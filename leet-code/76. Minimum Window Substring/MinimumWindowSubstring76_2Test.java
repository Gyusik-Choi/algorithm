package com.example;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.*;

class MinimumWindowSubstring76_2Test {
    private final MinimumWindowSubstring76_2 m = new MinimumWindowSubstring76_2();

    @Test
    void minWindow_1() {
        assertThat(m.minWindow("ADOBECODEBANC", "ABC")).isEqualTo("BANC");
    }

    @Test
    void minWindow_2() {
        assertThat(m.minWindow("a", "aa")).isEqualTo("");
    }

    @Test
    void minWindow_3() {
        assertThat(m.minWindow("aa", "a")).isEqualTo("a");
    }

    @Test
    void minWindow_4() {
        assertThat(m.minWindow("AGFOWEBCCA", "ABC")).isEqualTo("BCCA");
    }

    @Test
    void minWindow_5() {
        assertThat(m.minWindow("AGCDEBAACGGGGGGABC", "ABC")).isEqualTo("ABC");
    }

    @Test
    void minWindow_6() {
        assertThat(m.minWindow("a", "b")).isEqualTo("");
    }

    @Test
    void minWindow_7() {
        assertThat(m.minWindow("ab", "a")).isEqualTo("a");
    }

    @Test
    void minWindow_8() {
        assertThat(m.minWindow("abc", "ab")).isEqualTo("ab");
    }

    @Test
    void minWindow_9() {
        assertThat(m.minWindow("abc", "bc")).isEqualTo("bc");
    }

    @Test
    void minWindow_10() {
        assertThat(m.minWindow("bba", "ab")).isEqualTo("ba");
    }

    @Test
    void minWindow_11() {
        assertThat(m.minWindow("bbaa", "aba")).isEqualTo("baa");
    }

    @Test
    void minWindow_12() {
        assertThat(m.minWindow("ab", "A")).isEqualTo("");
    }

    @Test
    void minWindow_13() {
        assertThat(m.minWindow("abc", "ac")).isEqualTo("abc");
    }
}
