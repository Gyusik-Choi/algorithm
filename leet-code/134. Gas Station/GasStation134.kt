package com.example

import kotlin.collections.set

class GasStation134 {
    fun canCompleteCircuit(gas: IntArray, cost: IntArray): Int {
        // 총합이 음수면 안 된다
        //
        // 출발이 가능한 지점(gas 와 cost 의 차이가 0 이상)에서 출발하여
        // 어느 지점에서 실패하면
        // 해당 지점 앞까지는 가능함
        // 그러나 해당 지점 앞까지의 출발이 가능한 지점은
        // 어차피 실패하기 때문에
        // 그 이후의 출발 가능 지점에서 출발해야 한다
        //
        // 어느 출발점에서 어느 도착점(실패지점)까지 범위의 합을 보관한다 -> Map? {출발점: [실패지점, 합]}
        // 계속 실패해서 출발점이 Map 에 있거나 Map 의 어떤 출발점과 실패지점 안에 있으면 -1
        //
        // 실패 범위 안에 있는 candidate 는 건너 뛰도록 한다
        val candidates = gas.mapIndexed { idx, _ -> idx }.filter { gas[it] >= cost[it] }
        val fail = mutableMapOf<Int, IntArray>()
        var lastFail = intArrayOf(-1, -1)
        for (candidate in candidates) {
            if (invalidRange(lastFail, candidate)) {
                continue
            }
            var sums = 0
            for (i in 0 until gas.size) {
                val idx = (candidate + i) % gas.size
                if (fail.containsKey(idx) && sums < fail[idx]!![1]) {
                    fail[candidate] = intArrayOf(idx, sums + fail[idx]!![1])
                    lastFail = intArrayOf(candidate, idx)
                    break
                }
                sums += gas[idx] - cost[idx]
                if (sums < 0) {
                    fail[candidate] = intArrayOf(idx, sums)
                    lastFail = intArrayOf(candidate, idx)
                    break
                }
            }
            if (sums >= 0) {
                return candidate
            }
        }
        return -1
    }

    private fun invalidRange(lastFail: IntArray, candidate: Int): Boolean {
        if (lastFail[0] < lastFail[1]) {
            if (lastFail[0] < candidate && candidate <= lastFail[1]) {
                return true
            }
        }
        if (lastFail[0] > lastFail[1]) {
            if (lastFail[0] < candidate || lastFail[1] > candidate) {
                return true
            }
        }
        return false
    }
}
