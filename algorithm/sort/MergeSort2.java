package com.example;

public class MergeSort2 {
    /**
     * 원본 배열은 수정하지 않고 새로운 배열을 반환
     */
    public int[] sort(int[] arr) {
        if (arr.length < 2) {
            return arr;
        }

        int left = 0;
        int right = arr.length - 1;
        int mid = left + (right - left) / 2;
        int[] low = sort(slice(arr, left, mid));
        int[] high = sort(slice(arr, mid + 1, right));

        int[] sortedArr = new int[low.length + high.length];
        int idx = 0;
        int l = 0;
        int h = 0;
        while (l <= low.length - 1 && h <= high.length - 1) {
            if (low[l] <= high[h]) {
                sortedArr[idx] = low[l];
                l += 1;
            } else {
                sortedArr[idx] = high[h];
                h += 1;
            }
            idx += 1;
        }
        while (l <= low.length - 1) {
            sortedArr[idx] = low[l];
            l += 1;
            idx += 1;
        }
        while (h <= high.length - 1) {
            sortedArr[idx] = high[h];
            h += 1;
            idx += 1;
        }
        return sortedArr;
    }

    private int[] slice(int[] arr, int start, int endInclusive) {
        int size = endInclusive - start + 1;
        int[] result = new int[size];
        for (int i = 0; i < size; i++) {
            result[i] = arr[start + i];
        }
        return result;
    }
}
