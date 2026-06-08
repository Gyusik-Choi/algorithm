package com.example;

import java.util.Arrays;

public class SelectionSort2 {
    /**
     * 원본 배열은 수정하지 않고 새로운 배열 반환
     */
    public int[] sort(int[] arr) {
        int[] copiedArr = Arrays.copyOf(arr, arr.length);
        for (int i = 0; i < copiedArr.length - 1; i++) {
            int idx = i;
            for (int j = i + 1; j < copiedArr.length; j++) {
                if (copiedArr[idx] > copiedArr[j]) {
                    idx = j;
                }
            }
            if (i != idx) {
                switchElements(copiedArr, i, idx);
            }
        }
        return copiedArr;
    }

    private void switchElements(int[] arr, int idx1, int idx2) {
        int temp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = temp;
    }
}
