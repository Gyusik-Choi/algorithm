package com.example

class ReorderDataInLogFiles937_2 {
    fun reorderLogFiles(logs: Array<String>): Array<String> {
        val letterLogs = mutableListOf<String>()
        val digitLogs = mutableListOf<String>()
        for (log in logs) {
            if (log.split(" ")[1][0].isDigit()) {
                digitLogs.add(log)
            } else {
                letterLogs.add(log)
            }
        }
        letterLogs.sortWith { o1, o2 ->
            val o1Sliced = o1.split(" ", limit = 2)
            val o2Sliced = o2.split(" ", limit = 2)
            if (o1Sliced[1] == o2Sliced[1]) {
                o1Sliced[0].compareTo(o2Sliced[0])
            } else {
                o1Sliced[1].compareTo(o2Sliced[1])
            }
        }
        letterLogs.addAll(digitLogs)
        return letterLogs.toTypedArray()
    }
}
