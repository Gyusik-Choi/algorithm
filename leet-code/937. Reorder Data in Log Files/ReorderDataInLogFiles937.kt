package com.example

class ReorderDataInLogFiles937 {
    fun reorderLogFiles(logs: Array<String>): Array<String> {
        val digits = mutableListOf<String>()
        val letters = mutableListOf<String>()
        for (log in logs) {
            if (Character.isDigit(log.split(" ")[1][0])) {
                digits.add(log)
            } else {
                letters.add(log)
            }
        }
        letters.sortWith { a, b ->
            val aLog = a.split(" ", limit = 2)
            val bLog = b.split(" ", limit = 2)
            if (aLog[1] == bLog[1]) {
                aLog[0].compareTo(bLog[0])
            } else {
                aLog[1].compareTo(bLog[1])
            }
        }
        letters.addAll(digits)
        return letters.toTypedArray()
    }
}
