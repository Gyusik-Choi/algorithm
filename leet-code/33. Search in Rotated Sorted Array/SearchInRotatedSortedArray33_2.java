package com.example;

public class SearchInRotatedSortedArray33_2 {
    public int search(int[] nums, int target) {
        int pivot = findPivot(nums);
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int midPivot = (mid + pivot) % nums.length;
            if (nums[midPivot] == target) {
                return midPivot;
            }
            if (nums[midPivot] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    private int findPivot(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] <= nums[right]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
