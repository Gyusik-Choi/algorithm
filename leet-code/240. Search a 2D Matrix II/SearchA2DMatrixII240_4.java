package com.example;

public class SearchA2DMatrixII240_4 {
    public boolean searchMatrix(int[][] matrix, int target) {
        // 우측 상단에서 출발
        // 좌측 하단에서 출발도 가능
        int i = 0, j = matrix[0].length - 1;
        while (i < matrix.length && j >= 0) {
            if (matrix[i][j] == target) return true;
            if (matrix[i][j] < target) i++;
            else j--;
        }
        return false;
    }
}
