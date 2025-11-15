package com.example.algorithm

class ValidAnagram242_2 {
    fun isAnagram(s: String, t: String): Boolean {
        return s.toCharArray().sorted().joinToString() ==
                t.toCharArray().sorted().joinToString()
    }
}
