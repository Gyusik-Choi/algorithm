package com.example

class UTF8Validation393 {
    fun validUtf8(data: IntArray): Boolean {
        val binaryList = data.map { it -> convertToBinary(it) }
        println(binaryList)
        var idx = 0
        while (idx < binaryList.size) {
            val length = getLengthOfOne(binaryList[idx])
            if (length > 4 || length == 1) {
                return false
            }
            if (length == 0) {
                idx += 1
                continue
            }
            for (i in 1 until length) {
                // idx + i 가 배열 범위를 벗어났을 수 있다
                if (idx + i >= binaryList.size || binaryList[idx + i][0] != '1' || binaryList[idx + i][1] != '0') {
                    return false
                }
            }
            idx += length
        }
        return true
    }

    private fun convertToBinary(num: Int): String {
        val sb = StringBuilder()
        var number = num
        while (number > 0) {
            val remainder = number % 2
            sb.insert(0, remainder)
            number /= 2
        }
        return sb.toString().padStart(8, '0')
    }

    private fun getLengthOfOne(binary: String): Int {
        var length = 0
        var idx = 0
        while (idx < binary.length) {
            if (binary[idx] != '1') {
                break
            }
            length += 1
            idx += 1
        }
        return length
    }
}
