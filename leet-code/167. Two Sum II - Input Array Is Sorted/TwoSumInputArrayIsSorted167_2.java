 package com.example;

public class TwoSumInputArrayIsSorted167_2 {
    public int[] twoSum(int[] numbers, int target) {
        int[] answer = new int[2];
        for (int i = 0; i < numbers.length - 1; i++) {
            int num = numbers[i];
            int targetIdx = getTargetIdx(numbers, i + 1, numbers.length - 1, target - num);
            if (targetIdx == -1) continue;
            answer[0] = i + 1;
            answer[1] = targetIdx + 1;
        }
        return answer;
    }

    private int getTargetIdx(int[] numbers, int left, int right, int target) {
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (numbers[mid] == target) return mid;
            if (numbers[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }
}
