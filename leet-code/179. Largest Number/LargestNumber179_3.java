package com.example;

import java.util.Arrays;
import java.util.stream.Collectors;

public class LargestNumber179_3 {
    public String largestNumber(int[] nums) {
        quickSort(nums, 0, nums.length - 1);
        return nums[0] == 0
                ? "0"
                : Arrays.stream(nums)
                .mapToObj(Integer::toString)
                .collect(Collectors.joining());
    }

    private void quickSort(int[] arr, int low, int high) {
        if (low >= high) return;
        int p = partition(arr, low, high);
        quickSort(arr, low, p - 1);
        quickSort(arr, p + 1, high);
    }

    private int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int left = low;
        for (int right = low; right < high; right++) {
            if (isBigger(arr[right], pivot)) {
                swap(arr, left, right);
                left += 1;
            }
        }
        swap(arr, left, high);
        return left;
    }

    private boolean isBigger(int a, int b) {
        return Double.parseDouble(Integer.toString(a) + Integer.toString(b)) >
                Double.parseDouble(Integer.toString(b) + Integer.toString(a));
    }

    private void swap(int[] arr, int idx1, int idx2) {
        int temp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = temp;
    }
}
