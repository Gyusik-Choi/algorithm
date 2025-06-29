package com.example

class ValidAnagram242 {
    fun isAnagram(s: String, t: String): Boolean {
        // counting 정렬 활용
        val sCount = IntArray(26)
        val tCount = IntArray(26)
        for (sChar in s) {
            sCount[sChar - 'a'] += 1
        }
        for (tChar in t) {
            tCount[tChar - 'a'] += 1
        }
        for (i in 0..25) {
            if (sCount[i] != tCount[i]) {
                return false
            }
        }
        return true
    }
}