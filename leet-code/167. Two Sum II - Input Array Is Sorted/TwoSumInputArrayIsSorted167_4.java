package com.example;

public class TwoSumInputArrayIsSorted167_4 {
    public int[] twoSum(int[] numbers, int target) {
        int[] answer = new int[2];
        for (int i = 0; i < numbers.length - 1; i++) {
            int idx = getIdx(numbers, target - numbers[i], i + 1);
            if (idx != -1) {
                answer[0] = i + 1;
                answer[1] = idx + 1;
                break;
            }
        }
        return answer;
    }

    private int getIdx(int[] arr, int num, int low) {
        int left = low;
        int right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == num) {
                return mid;
            }
            if (arr[mid] < num) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
}
