package com.example

class Programmers92334_2 {
    fun solution(idList: Array<String>, report: Array<String>, k: Int): IntArray {
        // report 를 set 으로 중복 제거
        // report 를 루프 돌면서 공백을 기준으로 문자열 분리한 뒤
        // 두번째 인덱스인 신고당한 사람을 키로하고 신고한 사람을 값으로 하는
        // 해시맵에 신고 정보를 저장 -> 해시맵의 타입은 String, MutableList<String>
        // 해시맵을 루프 돌면서 값의 길이가 k 이상인 키 목록을 구한다
        // 해당 키의 값에 있는 사람들의 숫자를 세서 한 사람당 몇 번이나 메일을 받을지 구한다
        // 한 사람당 횟수를 구하는 해시맵을 만들고 idList 의 루프를 돌면서
        // idList 요소에 해당하는 사람의 횟수를
        // idList 와 동일한 크기의 배열의 만들고 동일한 인덱스에 넣는다
        val filteredReport = mutableSetOf<String>()
        filteredReport.addAll(report)
        val reportMap = mutableMapOf<String, MutableList<String>>()
        filteredReport.forEach { r ->
            val users = r.split(' ')
            reportMap[users[1]] = reportMap.getOrDefault(users[1], mutableListOf())
            reportMap[users[1]]!!.add(users[0])
        }
        val filteredReportMap = reportMap.filter { entry -> entry.value.size >= k }
        val reportCntPerUser = mutableMapOf<String, Int>()
        filteredReportMap.forEach { entry ->
            entry.value.forEach { user ->
                reportCntPerUser[user] = reportCntPerUser.getOrDefault(user, 0) + 1
            }
        }
        return idList.map { reportCntPerUser[it] ?: 0 }.toIntArray()
    }
}
