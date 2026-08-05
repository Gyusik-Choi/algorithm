package com.example

import kotlin.math.max

class LongestRepeatingCharacterReplacement424_2 {
    fun characterReplacement(s: String, k: Int): Int {
        val count = IntArray(26)
        var maxCount = 0
        var left = 0
        for (right in 0..s.lastIndex) {
            count[s[right] - 'A']++
            maxCount = max(maxCount, count[s[right] - 'A'])
            if (right - left + 1 > maxCount + k) {
                count[s[left] - 'A']--
                left++
            }
        }
        // 한번 늘어난 window 는 줄어들지 않는다
        return s.length - left
    }
}
