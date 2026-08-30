package com.example

import kotlin.math.min

class Programmers92342 {
    companion object {
        var maxDiff = 0
        var maxDiffArray: IntArray = intArrayOf(-1)
    }

    fun solution(n: Int, info: IntArray): IntArray {
        maxDiff = 0
        maxDiffArray = intArrayOf(-1)
        recursion(n, info, IntArray(info.size), 0)
        return maxDiffArray
    }

    private fun recursion(n: Int, apeach: IntArray, lion: IntArray, curIdx: Int) {
        if (n < 0) {
            return
        }
        if (n == 0) {
            // 점수 차이 계산
            val diff = getPointDiff(apeach, lion)
            if (maxDiff < diff) {
                maxDiff = diff
                maxDiffArray = lion.clone()
                return
            }
            if (maxDiff > 0 && maxDiff == diff && isArrayContainsMoreLowerPoints(lion)) {
                maxDiffArray = lion.clone()
            }
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
            if (apeach[i] == 0 && lion[i] == 0) {
                continue
            }
            if (apeach[i] >= lion[i]) {
                apeachSum += 10 - i
            } else {
                lionSum += 10 - i
            }
        }
        return lionSum - apeachSum
    }

    private fun isArrayContainsMoreLowerPoints(lion: IntArray): Boolean {
        // maxDiffArray 가 더 큰게 나오기 전에 lion 이 더 큰게 나와야 한다
        for (i in lion.indices.reversed()) {
            if (lion[i] > maxDiffArray[i]) {
                return true
            }
            if (lion[i] < maxDiffArray[i]) {
                return false
            }
        }
        return false
    }
}

//package com.example
//
//class Programmers92342 {
//    // 화살의 개수를 담은 자연수 n,
//    // 어피치가 맞힌 과녁 점수의 개수를 10점부터 0점까지 순서대로 담은 정수 배열 info가 매개변수로 주어집니다.
//    // 이때, 라이언이 가장 큰 점수 차이로 우승하기 위해
//    // n발의 화살을 어떤 과녁 점수에 맞혀야 하는지를
//    // 10점부터 0점까지 순서대로 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요.
//    // 만약, 라이언이 우승할 수 없는 경우(무조건 지거나 비기는 경우)는 [-1]을 return 해주세요.
//    // 제한사항
//    // 1 ≤ n ≤ 10
//    // info의 길이 = 11
//    // 0 ≤ info의 원소 ≤ n
//    // info의 원소 총합 = n
//    // info의 i번째 원소는 과녁의 10 - i 점을 맞힌 화살 개수입니다. (i는 0~10 사이의 정수입니다.)
//    // 라이언이 우승할 방법이 있는 경우, return 할 정수 배열의 길이는 11입니다.
//    // 0 ≤ return할 정수 배열의 원소 ≤ n
//    // return할 정수 배열의 원소 총합 = n (꼭 n발을 다 쏴야 합니다.)
//    // return할 정수 배열의 i번째 원소는 과녁의 10 - i 점을 맞힌 화살 개수입니다. (i는 0~10 사이의 정수입니다.)
//    // 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우,
//    // 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.
//    // 가장 낮은 점수를 맞힌 개수가 같을 경우 계속해서 그다음으로 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.
//    // 예를 들어, [2,3,1,0,0,0,0,1,3,0,0]과 [2,1,0,2,0,0,0,2,3,0,0]를 비교하면
//    // [2,1,0,2,0,0,0,2,3,0,0]를 return 해야 합니다.
//    // 다른 예로, [0,0,2,3,4,1,0,0,0,0,0]과 [9,0,0,0,0,0,0,0,1,0,0]를 비교하면
//    // [9,0,0,0,0,0,0,0,1,0,0]를 return 해야 합니다.
//    // 라이언이 우승할 방법이 없는 경우, return 할 정수 배열의 길이는 1입니다.
//    // 라이언이 어떻게 화살을 쏘든 라이언의 점수가 어피치의 점수보다 낮거나 같으면 [-1]을 return 해야 합니다.
//    //
//    // n	info	                result
//    // 5	[2,1,1,1,0,0,0,0,0,0,0]	[0,2,2,0,1,0,0,0,0,0,0]
//    // 1	[1,0,0,0,0,0,0,0,0,0,0]	[-1]
//    // 9	[0,0,1,2,0,1,1,1,1,1,1]	[1,1,2,0,1,2,2,0,0,0,0]
//    // 10	[0,0,0,0,0,0,0,0,3,4,3]	[1,1,1,1,1,1,1,1,0,0,2]
//    //
//    // 5	[2,1,1,1,0,0,0,0,0,0,0]	[0,2,2,0,1,0,0,0,0,0,0]
//    // 10/0 - 10/9 - 10/18 - 17/18 - 17/24
//    //
//    // 완탐가능?
//    // 조합 구해서 최대 점수차를 구해야 할듯 한데
//    // 다 구하고 비교하는게 아니라 가망이 없으면 그만 조회하거나
//    // 이미 정답이 구해졌으면 그만 조회하는 방법이 있으면 좋을듯
//    // 백트래킹
//    //
//    // 최대 점수차가 나는 조합을 구하되 가능한 낮은 점수가 많아야 한다
//    //
//    companion object {
//        var maxDiff = 0
//        var maxDiffArray: IntArray = intArrayOf(-1)
//    }
//
//    fun solution(n: Int, info: IntArray): IntArray {
//        maxDiff = 0
//        maxDiffArray = intArrayOf(-1)
//        recursion(n, info, IntArray(info.size), 0)
//        return maxDiffArray
//    }
//
//    private fun recursion(n: Int, apeach: IntArray, lion: IntArray, curIdx: Int) {
//        if (n == 0) {
//            // 점수 차이 계산
//            val diff = getPointDiff(apeach, lion)
//            if (maxDiff < diff) {
//                maxDiff = diff
//                maxDiffArray = lion.clone()
//                return
//            }
//            if (maxDiff > 0 && maxDiff == diff && isArrayContainsMoreLowerPoints(lion)) {
//                maxDiffArray = lion.clone()
//            }
//            return
//        }
//        for (i in curIdx until apeach.size) {
//            if (apeach[i] + 1 > n) {
//                continue
//            }
//            lion[i] = apeach[i] + 1
//            recursion(n - (apeach[i] + 1), apeach, lion, i + 1)
//            lion[i] = 0
//        }
//    }
//
//    private fun getPointDiff(apeach: IntArray, lion: IntArray): Int {
//        var apeachSum = 0
//        var lionSum = 0
//        for (i in apeach.indices) {
//            if (apeach[i] == 0 && lion[i] == 0) {
//                continue
//            }
//            if (apeach[i] >= lion[i]) {
//                apeachSum += 10 - i
//            } else {
//                lionSum += 10 - i
//            }
//        }
//        return lionSum - apeachSum
//    }
//
//    private fun isArrayContainsMoreLowerPoints(lion: IntArray): Boolean {
//        // maxDiffArray 가 더 큰게 나오기 전에 lion 이 더 큰게 나와야 한다
//        for (i in lion.indices.reversed()) {
//            if (lion[i] > maxDiffArray[i]) {
//                return true
//            }
//            if (lion[i] < maxDiffArray[i]) {
//                return false
//            }
//        }
//        return false
//    }
//}
