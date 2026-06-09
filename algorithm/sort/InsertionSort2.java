package com.example;

import java.util.Arrays;

public class InsertionSort2 {
    /**
     * 원본 배열은 수정하지 않고 새로운 배열 반환
     */
    public int[] sort(int[] arr) {
        int[] copiedArr = Arrays.copyOf(arr, arr.length);
        for (int i = 1; i < copiedArr.length; i++) {
            int idx = i;
            int originNum = copiedArr[i];
            while (idx > 0 && copiedArr[idx - 1] > originNum) {
                copiedArr[idx] = copiedArr[idx - 1];
                idx -= 1;
            }
            copiedArr[idx] = originNum;
        }
        return copiedArr;
    }
}
