package com.example

class ValidPalindrome125_2 {
    fun isPalindrome(s: String): Boolean {
        val str = s.replace(Regex("[^a-zA-Z0-9]"), "").lowercase()
        var left = 0
        var right = str.length - 1
        while (left < right) {
            if (str[left] != str[right]) {
                return false
            }
            left += 1
            right -= 1
        }
        return true
    }
}
