package com.example

class UTF8Validation393_2 {
    fun validUtf8(data: IntArray): Boolean {
        var idx = 0
        while (idx < data.size) {
            idx += when {
                data[idx] shr 3 == 0b11110 && idx + 3 < data.size && isValid(data, idx + 1, idx + 3) -> 4
                data[idx] shr 4 == 0b1110 && idx + 2 < data.size && isValid(data, idx + 1, idx + 2) -> 3
                data[idx] shr 5 == 0b110 && idx + 1 < data.size && isValid(data, idx + 1, idx + 1) -> 2
                data[idx] shr 6 == 0b10 -> return false
                data[idx] shr 7 == 0 -> 1
                else -> return false
            }
        }
        return true
    }

    private fun isValid(data: IntArray, start: Int, end: Int): Boolean {
        for (i in start..end) {
            if (data[i] shr 6 != 0b10) {
                return false
            }
        }
        return true
    }
}

// 시프트 연산 참고
// https://codedragon.tistory.com/7998
