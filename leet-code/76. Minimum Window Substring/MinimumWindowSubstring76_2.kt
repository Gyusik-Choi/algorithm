package com.example

class MinimumWindowSubstring76_2 {
    // left < right 조건이 없으면
    // t 에 포함되지 않는 문자가 계속 나오면 right 보다 left 가 커질 수 있고
    // 그렇게 되면 sMap 에 접근시 sMap 에 포함되지 않는 문자일 수 있어서
    // null pointer exception 이 발생할 수 있다
    //
    // 현재 구현상 tCount 가 t 길이까지 증가하면 tCount 가 유지되기 때문에
    // tCount 를 감소 시키는 로직이 없지만
    // 증가 시키는 로직만 있고 감소 시키는 로직이 없는게 다소 부자연스럽게 느껴진다
    fun minWindow(s: String, t: String): String {
        var tCount = 0
        val tMap = mutableMapOf<Char, Int>()
        for (c in t) tMap[c] = tMap.getOrDefault(c, 0) + 1
        val sMap = mutableMapOf<Char, Int>()
        var minLength = Int.MAX_VALUE
        var start = 0
        var end = 0
        var left = 0
        for (right in 0..s.lastIndex) {
            if (sMap.getOrDefault(s[right], 0) < tMap.getOrDefault(s[right], 0)) tCount += 1
            sMap.putIfAbsent(s[right], 0)
            sMap[s[right]] = sMap[s[right]]!! + 1
            while (left < right && (!t.contains(s[left]) || sMap[s[left]]!! > tMap[s[left]]!!)) {
                sMap[s[left]] = sMap[s[left]]!! - 1
                left += 1
            }
            if (tCount == t.length && minLength > right - left + 1) {
                start = left
                end = right
                minLength = right - left + 1
            }
        }
        return if (minLength == Int.MAX_VALUE) "" else s.substring(start, end + 1)
    }
}
