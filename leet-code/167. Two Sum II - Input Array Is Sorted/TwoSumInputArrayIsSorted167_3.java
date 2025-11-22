package com.example;

public class TwoSumInputArrayIsSorted167_3 {
    public int[] twoSum(int[] numbers, int target) {
        for (int i = 0; i < numbers.length - 1; i++) {
            int num = target - numbers[i];
            int left = i + 1;
            int right = numbers.length - 1;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (numbers[mid] == num) {
                    return new int[]{i + 1, mid + 1};
                }
                if (numbers[mid] < num) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return null;
    }
}
