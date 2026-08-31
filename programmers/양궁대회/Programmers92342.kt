package com.example

import kotlin.math.min

class Programmers92342 {
    companion object {
        var maxDiff = 0
        var maxDiffArray = intArrayOf(-1)
    }

    fun solution(n: Int, info: IntArray): IntArray {
        recursion(n, info, IntArray(info.size), 0)
        return maxDiffArray
    }

    private fun recursion(n: Int, apeach: IntArray, lion: IntArray, curIdx: Int) {
        if (n == 0) {
            val diff = getPointDiff(apeach, lion)
            if (maxDiff < diff) {
                maxDiff = diff
                maxDiffArray = lion.clone()
                return
            }
            if (maxDiff > 0 && maxDiff == diff && containsMoreLowerPoints(lion)) maxDiffArray = lion.clone()
            return
        }
        for (i in curIdx until apeach.size) {
            val maxAdditionNum = min(apeach[i] + 1, n)
            lion[i] = maxAdditionNum
            recursion(n - maxAdditionNum, apeach, lion, i + 1)
            lion[i] = 0
        }
    }

    private fun getPointDiff(apeach: IntArray, lion: IntArray): Int {
        var apeachSum = 0
        var lionSum = 0
        for (i in apeach.indices) {
            when {
                apeach[i] == 0 && lion[i] == 0 -> continue
                apeach[i] >= lion[i] -> apeachSum += 10 - i
                else -> lionSum += 10 - i
            }
        }
        return lionSum - apeachSum
    }

    private fun containsMoreLowerPoints(lion: IntArray): Boolean {
        // maxDiffArray 가 더 큰게 나오기 전에 lion 이 더 큰게 나와야 한다
        for (i in lion.indices.reversed()) {
            if (lion[i] > maxDiffArray[i]) return true
            if (lion[i] < maxDiffArray[i]) return false
        }
        return false
    }
}
