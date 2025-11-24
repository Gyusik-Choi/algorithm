package com.example;

public class SearchA2DMatrixII240_3 {
    public boolean searchMatrix(int[][] matrix, int target) {
        int y = 0, x = matrix[0].length - 1;
        while (0 <= y && y < matrix.length && 0 <= x && x < matrix[0].length) {
            if (matrix[y][x] == target) {
                return true;
            }
            if (matrix[y][x] > target) {
                x -= 1;
            } else {
                y += 1;
            }
        }
        return false;
    }
}
