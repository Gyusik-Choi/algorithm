package com.example

class LongestPalindromicSubstring5 {
    fun longestPalindrome(s: String): String {
        var start = 0
        var maxLength = 1
        for (i in 0..s.length - 2) {
            // getPalindromeIdx 의 while 문을 만족하지 않고 바로 리턴되는 경우도 있을 수 있다
            // 이때의 리턴값은 호출하면서 인자로 넣은 left, right 값과 동일하다
            // 한가지 혼동됐던게 해당 리턴값이 팰린드롬이 아닐 수도 있는데
            // 이 값을 바탕으로 갱신 여부를 바로 검증해서 갱신을 하는게 맞을까라는 생각이 들었다
            // 사실 이를 걱정할 필요가 없었다
            // getPalindromeIdx 의 내부에서 while 문을 만족해서 left, right 가 변경됐다면
            // 실제 팰린드롬의 범위보다 left 는 1이 더 작고 right 는 1이 더 크게 리턴된다
            // 그래서 getPalindromeIdx 의 리턴값을 가지고 사용할 때 이를 감안해서 사용하게 된다
            // 즉 while 문을 돌지 않고 바로 리턴되더라도 문제가 없다
            val evenIdx = getPalindromeIdx(s, i, i + 1)
            if (evenIdx[1] - evenIdx[0] - 1 > maxLength) {
                start = evenIdx[0] + 1
                maxLength = evenIdx[1] - evenIdx[0] - 1
            }

            val oddIdx = getPalindromeIdx(s, i, i + 2)
            if (oddIdx[1] - oddIdx[0] - 1 > maxLength) {
                start = oddIdx[0] + 1
                maxLength = oddIdx[1] - oddIdx[0] - 1
            }
        }
        return s.substring(start, start + maxLength)
    }

    private fun getPalindromeIdx(s: String, left: Int, right: Int): IntArray {
        var l = left
        var r = right
        while (l >= 0 && r <= s.length - 1 && s[l] == s[r]) {
            l -= 1
            r += 1
        }
        return intArrayOf(l, r)
    }
}
