package com.example

class MinimumWindowSubstring76 {
    fun minWindow(s: String, t: String): String {
        val map = mutableMapOf<Char, Int>()
        for (c in t) {
            map[c] = map.getOrDefault(c, 0) + 1
        }
        var missing = t.length
        var answer = ""
        var minLength = Int.MAX_VALUE
        var left = 0
        var right = 0

        for (c in s) {
            right += 1

            if (map.containsKey(c) && map[c]!! > 0) {
                missing -= 1
            }

            map[c] = map.getOrDefault(c, 0) - 1

            if (missing > 0) {
                continue
            }

            // s 가 "ADOBECODEBANC" 일 때
            // left 와 right 가 "BECODEBA" 구간에 있다고 가정하면
            // map 의 containsKey 로 판단하는게 아니라
            // map 의 값이 음수 여부로 판단해야
            // 제대로 left 를 이동시킬 수 있다
            // containsKey 로 하면 B 가 map 에 포함되어 있어서
            // left 를 이동할 수 없다
            while (left < right && map[s[left]]!! < 0) {
                map[s[left]] = map.getOrDefault(s[left], 0) + 1
                left += 1
            }

            if (minLength > right - left + 1) {
                minLength = right - left + 1
                answer = s.slice(IntRange(left, right - 1))
            }

            map[s[left]] = map.getOrDefault(s[left], 0) + 1
            missing += 1
            left += 1
        }

        return answer
    }
}
