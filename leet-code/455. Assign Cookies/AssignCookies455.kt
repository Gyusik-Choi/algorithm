package com.example

class AssignCookies455 {
    fun findContentChildren(g: IntArray, s: IntArray): Int {
        // g 와 s 를 정렬한다
        // s 의 for 문을 돌면서
        // g 에 만족하는 요소를 찾는다
        // 만약에 현재 s 가 g 에 만족하는 요소를 못 찾으면
        // 더 이상 만족하는 요소를 찾을 수 없기 때문에
        // s 의 for 문을 종료한다
        g.sort()
        s.sort()
        var maxNumber = 0
        var idx = 0
        for (size in s) {
            if (idx >= g.size) {
                break
            }
            if (size >= g[idx]) {
                maxNumber += 1
                idx += 1
            }
        }
        return maxNumber
    }
}
