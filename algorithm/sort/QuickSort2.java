package com.example;

import java.util.Arrays;

public class QuickSort2 {
    /**
     * 원본 배열을 수정하지 않고 새로운 배열 반환
     */
    public int[] sort(int[] arr) {
        int[] newArr = Arrays.copyOfRange(arr, 0, arr.length);
        return sort(newArr, 0, newArr.length - 1);
    }

    private int[] sort(int[] arr, int low, int high) {
        if (low >= high) {
            return arr;
        }
        int pivot = partition(arr, low, high);
        sort(arr, low, pivot - 1);
        sort(arr, pivot + 1, high);
        return arr;
    }

    private int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int left = low;
        for (int right = low; right < high; right++) {
            if (arr[right] < pivot) {
                swap(arr, left, right);
                left += 1;
            }
        }
        swap(arr, left, high);
        return left;
    }

    private void swap(int[] arr, int i1, int i2) {
        int temp = arr[i1];
        arr[i1] = arr[i2];
        arr[i2] = temp;
    }
}
