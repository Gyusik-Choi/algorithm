package com.example;

public class SearchInRotatedSortedArray33_3 {
    public int search(int[] nums, int target) {
        int pivot = getMinIdx(nums);
        int low = 0;
        int high = nums.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int midPivot = (mid + pivot) % nums.length;
            if (nums[midPivot] == target) {
                return midPivot;
            }
            if (nums[midPivot] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }

    private int getMinIdx(int[] nums) {
        int low = 0;
        int high = nums.length - 1;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] <= nums[high]) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}
