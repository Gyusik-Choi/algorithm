package com.example

import kotlin.math.max

class LongestRepeatingCharacterReplacement424 {
    fun characterReplacement(s: String, k: Int): Int {
        val count = mutableMapOf<Char, Int>()
        var left = 0
        var answer = 0
        for (right in s.indices) {
            count[s[right]] = count.getOrDefault(s[right], 0) + 1
            // 해시맵에서 가장 큰 갯수 + k >= 윈도우 크기
            val maxEntry = count.maxBy { it.value }
            if (maxEntry.value + k >= right - left + 1) {
                answer = max(answer, right - left + 1)
            } else {
                count[s[left]] = count.getOrDefault(s[left], 0) - 1
                left += 1
            }
        }
        return answer
    }
}
