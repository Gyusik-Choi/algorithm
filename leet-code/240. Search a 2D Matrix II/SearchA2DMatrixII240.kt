package com.example

class SearchA2DMatrixII240 {
    // 우측 맨 상단에서 출발
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        var y = 0
        var x = matrix[0].size - 1
        while (y <= matrix.size - 1 && x >= 0) {
            when {
                matrix[y][x] == target -> return true
                matrix[y][x] < target -> y += 1
                else -> x -= 1
            }
        }
        return false
    }

//    좌측 맨 하단에서 출발
//    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
//        var y = matrix.size - 1
//        var x = 0
//        while (y >= 0 && x <= matrix[0].size - 1) {
//            when {
//                matrix[y][x] == target -> return true
//                matrix[y][x] < target -> x += 1
//                else -> y -= 1
//            }
//        }
//        return false
//    }
}
