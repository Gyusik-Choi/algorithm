package com.example;

public class SearchInRotatedSortedArray33 {
    public int search(int[] nums, int target) {
        int maxIdx = getMaxNumIndex(nums);
        if (isTargetIncludedInLeft(nums, maxIdx, target))
            return findTarget(nums, 0, maxIdx, target);
        return findTarget(nums, maxIdx + 1, nums.length - 1, target);
    }

    private int getMaxNumIndex(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            // 아래는 ChatGPT 설명
            // Bias mid to the right.
            // The +1 ensures that when there is an even number of elements,
            // the mid value is pushed to the right instead of defaulting to the left. For example:
            // If left = 0 and right = 1 (two elements):
            // Normally: mid = 0 + (1 - 0) / 2 = 0 → points to the first element.
            // With bias: mid = 0 + (1 - 0 + 1) / 2 = 1 → points to the second element.
            // This guarantees that in a range of two elements, the second element (right) is evaluated first.
            int mid = left + (right - left + 1) / 2;
            if (nums[left] < nums[mid]) left = mid;
            else right = mid - 1;
        }
        return left;
    }

    private boolean isTargetIncludedInLeft(int[] nums, int maxIdx, int target) {
        return nums[0] <= target && target <= nums[maxIdx];
    }

    private int findTarget(int[] nums, int left, int right, int target) {
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }
}

// 최대값을 구하고
// 최대값을 기준으로 왼쪽, 오른쪽으로 나뉜다
// target 이 왼쪽, 오른쪽 중에서 어디에 속하는지 찾는다
// 맨 왼쪽에서 최대값이 위치한 인덱스 사이에 target 이 들어간다면 target 은 왼쪽에 속하고
// 그렇지 않다면 target 은 오른쪽에 속한다
// 왼쪽, 오른쪽 중에서 target 이 속하는 쪽에서 이진탐색을 수행하고
// target 이 있으면 해당 인덱스를 리턴하고 없으면 -1을 리턴한다
