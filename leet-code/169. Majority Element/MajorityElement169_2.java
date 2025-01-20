package com.example;

public class MajorityElement169_2 {

    public int majorityElement(int[] nums) {
        return majorityElement(nums, 0, nums.length - 1);
    }

    private int majorityElement(int[] nums, int low, int high) {
        if (low == high) return nums[low];
        int mid = (low + high) / 2;
        int left = majorityElement(nums, low, mid);
        int right = majorityElement(nums, mid + 1, high);
        int leftCnt = 0;
        for (int i = low; i <= high; i++) if (nums[i] == left) leftCnt++;
        return leftCnt > (high - low + 1) / 2 ? left : right;
    }
}

// [2, 2, 1, 1, 1, 2, 2]
// (0, 6)
// (0, 3) | (4, 6)
// (0, 1), (2, 3) | (4, 5), (6, 6)
// (0, 0), (1, 1), (2, 2), (3, 3) | (4, 4), (5, 5), 6