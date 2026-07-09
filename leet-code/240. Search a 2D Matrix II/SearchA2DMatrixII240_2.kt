package com.example

class SearchA2DMatrixII240_2 {
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        // 좌측 하단에서 출발
        var i = matrix.lastIndex
        var j = 0
        while (i >= 0 && j <= matrix[0].lastIndex) {
            when {
                matrix[i][j] < target -> j++
                matrix[i][j] > target -> i--
                else -> return true
            }
        }
        return false
    }
}
