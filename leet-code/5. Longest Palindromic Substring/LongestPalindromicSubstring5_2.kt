package com.example.algorithm

class LongestPalindromicSubstring5_2 {
    fun longestPalindrome(s: String): String {
        var longest = ""
        for (i in s.indices) {
            val leftLongest = recursion(s, i, i, longest)
            val rightLongest = recursion(s, i, i + 1, longest)
            if (longest.length < leftLongest.length) {
                longest = leftLongest
            }
            if (longest.length < rightLongest.length) {
                longest = rightLongest
            }
        }
        return longest
    }

    private fun recursion(s: String, l: Int, r: Int, longest: String): String {
        var left = l
        var right = r
        var longestWord = longest
        var maximumLength = longest.length
        while (0 <= left && right < s.length && s[left] == s[right]) {
            if (right - left + 1 > maximumLength) {
                maximumLength = right - left + 1
                longestWord = s.substring(left, right + 1)
            }
            left -= 1
            right += 1
        }
        return longestWord
    }
}

//package com.example.algorithm
//
//class LongestPalindromicSubstring5_2 {
//    fun longestPalindrome(s: String): String {
//        var longest = s[0].toString()
//        var maxLength = 1
//        for (i in 1..<s.length) {
//            var left = i - 1
//            var right = i + 1
//            while (0 <= left && right < s.length && s[left] == s[right]) {
//                if (right - left + 1 > maxLength) {
//                    longest = s.substring(left, right + 1)
//                    maxLength = right - left + 1
//                }
//                left -= 1
//                right += 1
//            }
//        }
//        for (i in 0..<s.length) {
//            var left = i
//            var right = i + 1
//            while (0 <= left && right < s.length && s[left] == s[right]) {
//                if (right - left + 1 > maxLength) {
//                    longest = s.substring(left, right + 1)
//                    maxLength = right - left + 1
//                }
//                left -= 1
//                right += 1
//            }
//
//            var left2 = i - 1
//            var right2 = i + 2
//            while (0 <= left2 && right2 < s.length && s[left2] == s[right2]) {
//                if (right2 - left2 + 1 > maxLength) {
//                    longest = s.substring(left2, right2 + 1)
//                    maxLength = right2 - left2 + 1
//                }
//                left2 -= 1
//                right2 += 1
//            }
//        }
//        return longest
//    }
//}
