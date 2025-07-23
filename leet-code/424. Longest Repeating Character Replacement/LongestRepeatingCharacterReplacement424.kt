package com.example

import kotlin.math.max

class LongestRepeatingCharacterReplacement424 {
    fun characterReplacement(s: String, k: Int): Int {
        val count = mutableMapOf<Char, Int>()
        var left = 0
        var answer = 0
        for (right in s.indices) {
            count[s[right]] = count.getOrDefault(s[right], 0) + 1
            // 해시맵에서 가장 큰 갯수 + k >= 윈도우 크기
            val maxEntry = count.maxBy { it.value }
            if (maxEntry.value + k >= right - left + 1) {
                answer = max(answer, right - left + 1)
            } else {
                count[s[left]] = count.getOrDefault(s[left], 0) - 1
                left += 1
            }
        }
        return answer
    }

//    아래의 풀이도 가능하다
//    (교재는 아래처럼 정답 변수를 따로 두지 않으면서 마지막에 한번만 구하는 방식을 사용했다)
//    fun characterReplacement(s: String, k: Int): Int {
//        val count = mutableMapOf<Char, Int>()
//        var left = 0
//        for (right in s.indices) {
//            count[s[right]] = count.getOrDefault(s[right], 0) + 1
//            // 해시맵에서 가장 큰 갯수 + k >= 윈도우 크기
//            val maxEntry = count.maxBy { it.value }
//            if (maxEntry.value + k < right - left + 1) {
//                count[s[left]] = count.getOrDefault(s[left], 0) - 1
//                left += 1
//            }
//        }
//        return s.length - left
//    }
}
