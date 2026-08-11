package com.example;

public class MajorityElement169_4 {
    public int majorityElement(int[] nums) {
        return majorityElement(nums, 0, nums.length - 1);
    }

    private int majorityElement(int[] nums, int left, int right) {
        if (left == right) {
            return nums[left];
        }
        int mid = left + (right - left) / 2;
        int a = majorityElement(nums, left, mid);
        int b = majorityElement(nums, mid + 1, right);
        int countA = 0;
        for (int i = left; i <= right; i++) {
            if (nums[i] == a) {
                countA++;
            }
        }
        return (right - left + 1) / 2 < countA ? a : b;
    }
}
