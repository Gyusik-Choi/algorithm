package com.example

class GasStation134_2 {
    fun canCompleteCircuit(gas: IntArray, cost: IntArray): Int {
        var idx = 0
        var startIdx = 0
        var sum = 0
        while (idx <= gas.lastIndex) {
            var tempSum = 0
            while (idx <= gas.lastIndex && tempSum >= 0) {
                tempSum += gas[idx] - cost[idx]
                idx += 1
            }
            sum += tempSum
            if (idx > gas.lastIndex && sum >= 0) {
                return startIdx
            }
            startIdx = idx
        }
        return -1
    }
}
