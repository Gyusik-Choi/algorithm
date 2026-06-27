package com.example;

public class SortColors75_3 {
    public void sortColors(int[] nums) {
        int i = 0;
        int j = 0;
        int k = nums.length - 1;
        while (j <= k) {
            if (nums[j] < 1) {
                switchElements(nums, i, j);
                i++;
                j++;
            } else if (nums[j] > 1) {
                switchElements(nums, j, k);
                k--;
            } else {
                j++;
            }
        }
    }

    private void switchElements(int[] nums, int idx1, int idx2) {
        int temp = nums[idx1];
        nums[idx1] = nums[idx2];
        nums[idx2] = temp;
    }
}
