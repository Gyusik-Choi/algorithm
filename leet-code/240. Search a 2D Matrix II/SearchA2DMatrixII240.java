package com.example;

public class SearchA2DMatrixII240 {

    public boolean searchMatrix(int[][] matrix, int target) {
        for (int[] m : matrix) if (findTarget(m, target)) return true;
        return false;
    }

    private boolean findTarget(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) return true;
            if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return false;
    }
}
