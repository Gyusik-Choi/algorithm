package com.example;

import java.util.Arrays;

public class QuickSort3 {
    public int[] sort(int[] arr) {
        int[] copiedArr = Arrays.copyOf(arr, arr.length);
        quickSort(copiedArr, 0, copiedArr.length - 1);
        return copiedArr;
    }

    private void quickSort(int[] arr, int low, int high) {
        if (low >= high) {
            return;
        }
        int p = partition(arr, low, high);
        quickSort(arr, low, p - 1);
        quickSort(arr, p + 1, high);
    }

    private int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int left = low;
        for (int right = low; right < high; right++) {
            if (arr[right] < pivot) {
                switchElement(arr, left, right);
                left++;
            }
        }
        switchElement(arr, left, high);
        return left;
    }

    private void switchElement(int[] arr, int idx1, int idx2) {
        int temp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = temp;
    }
}
