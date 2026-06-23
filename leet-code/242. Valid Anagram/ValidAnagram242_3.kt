package com.example

class ValidAnagram242_3 {
    fun isAnagram(s: String, t: String): Boolean {
        val arr1 = IntArray(26)
        val arr2 = IntArray(26)
        for (w in s) arr1[w.code - 'a'.code]++
        for (w in t) arr2[w.code - 'a'.code]++
        for (i in 0 until 26) if (arr1[i] != arr2[i]) return false
        return true
    }
}
