package com.example

class AssignCookies455_3 {
    fun findContentChildren(g: IntArray, s: IntArray): Int {
        g.sort()
        s.sort()
        var i = 0
        var j = 0
        var count = 0
        while (i <= g.lastIndex && j <= s.lastIndex) {
            if (g[i] <= s[j]) {
                count += 1
                i += 1
            }
            j += 1
        }
        return count
    }
}
