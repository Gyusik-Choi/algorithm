package com.example

import kotlin.math.ceil

class Programmers92341 {

    fun solution(fees: IntArray, records: Array<String>): IntArray {
        val carRecords = mutableMapOf<String, MutableList<String>>()
        for (record in records) {
            val r = record.split(" ")
            val carTime = r[0]
            val carNum = r[1]
            val list = carRecords.getOrDefault(carNum, mutableListOf())
            list.add(carTime)
            carRecords[carNum] = list
        }

        val carFee = mutableMapOf<String, Int>()
        for (entry in carRecords.entries.iterator()) {
            carFee[entry.key] = getFee(fees, entry.value)
        }

        val carNumbers = carFee.keys.sorted()

        val answer = IntArray(carNumbers.size)
        for (i in carNumbers.indices) {
            answer[i] = carFee[carNumbers[i]]!!
        }
        return answer
    }

    private fun getFee(fees: IntArray, record: List<String>): Int {
        val defaultTime = fees[0]
        val defaultFee = fees[1]
        val unitTime = fees[2]
        val unitFee = fees[3]
        val carParkTime = getTime(record)

        if (defaultTime >= carParkTime) {
            return defaultFee
        }
        return defaultFee + (ceil((carParkTime - defaultTime) / unitTime.toDouble())).toInt() * unitFee
    }

    private fun getTime(record: List<String>): Int {
        var time = 0
        for (i in 0..record.lastIndex step 2) {
            time += if (i == record.lastIndex) {
                convertToMinute("23:59") - convertToMinute(record[i])
            } else {
                convertToMinute(record[i + 1]) - convertToMinute(record[i])
            }
        }
        return time
    }

    private fun convertToMinute(time: String): Int {
        val t = time.split(":")
        return t[0].toInt() * 60 + t[1].toInt()
    }
}
// [기본 시간, 기본 요금, 단위 시간, 단위 요금]
// [시간, 차량번호, 내역]
// 차량번호별 시간 정보 갖는 해시맵
// 올바른 입력만 주어지기 때문에 입출차 내역은 없어도 된다
// 차량번호별 요금 정보 갖는 해시맵
// 시간을 분으로 변환
// 요금 계산

