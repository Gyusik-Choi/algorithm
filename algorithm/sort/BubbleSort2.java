package com.example;

import java.util.Arrays;

public class BubbleSort2 {
    /**
     * 원본 수정없이 새로운 배열 반환
     */
    public int[] bubbleSort(int[] arr) {
        int[] copiedArr = Arrays.copyOf(arr, arr.length);
        for (int i = arr.length - 1; i > 0; i--) {
            for (int j = 0; j < i; j++) {
                if (copiedArr[j] > copiedArr[j + 1]) {
                    switchElements(copiedArr, j, j + 1);
                }
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
