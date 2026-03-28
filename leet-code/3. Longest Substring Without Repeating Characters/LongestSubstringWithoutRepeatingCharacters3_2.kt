package com.example

class LongestSubstringWithoutRepeatingCharacters3_2 {
    fun lengthOfLongestSubstring(s: String): Int {
        val map = mutableMapOf<Char, Int>()
        var left = 0
        var maxLength = 0
        for (right in s.indices) {
            if (map[s[right]] != null && map[s[right]]!! >= left) {
                left = map[s[right]]!! + 1
            } else {
                maxLength = maxLength.coerceAtLeast(right - left + 1)
            }
            map[s[right]] = right
        }
        return maxLength
    }
}
