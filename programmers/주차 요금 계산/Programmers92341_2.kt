package com.example

import kotlin.math.ceil

class Programmers92341_2 {
    //[180, 5000, 10, 600]	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	[14600, 34400, 5000]
    //[120, 0, 60, 591]	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	[0, 591]
    //[1, 461, 1, 10]	["00:00 1234 IN"]	[14841]
    fun solution(fees: IntArray, records: Array<String>): IntArray {
        val park = mutableMapOf<String, MutableList<Int>>()
        for (r in records) {
            val info = r.split(" ")
            park.putIfAbsent(info[1], mutableListOf())
            park[info[1]]!!.add(convertToMinute(info[0]))
        }
        fillParkOutTime(park)
        val fee = mutableMapOf<String, Int>()
        for (car in park.keys) fee[car] = calculateParkFee(fees, park[car]!!)
        return park.keys.sorted().map { fee[it]!! }.toIntArray()
    }

    private fun convertToMinute(timeStr: String): Int {
        return timeStr.split(":")[0].toInt() * 60 + timeStr.split(":")[1].toInt()
    }

    private fun fillParkOutTime(parkMap: MutableMap<String, MutableList<Int>>) {
        for (entry in parkMap) {
            if (entry.value.size % 2 == 0) continue
            parkMap[entry.key]!!.add(convertToMinute("23:59"))
        }
    }

    private fun calculateParkFee(feeInfo: IntArray, parkTime: List<Int>): Int {
        var totalTime = 0
        for (i in parkTime.indices step 2) totalTime += parkTime[i + 1] - parkTime[i]
        if (feeInfo[0] >= totalTime) return feeInfo[1]
        return feeInfo[1] + ceil((totalTime - feeInfo[0]).toDouble() / feeInfo[2]).toInt() * feeInfo[3]
    }
}
