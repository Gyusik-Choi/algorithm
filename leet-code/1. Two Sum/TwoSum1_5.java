package com.example;

import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.IntStream;

public class TwoSum1_5 {
    public int[] twoSum(int[] nums, int target) {
        int[][] numsWithIndex = IntStream.range(0, nums.length)
                .mapToObj(i -> new int[]{nums[i], i})
                .toArray(int[][]::new);
        Arrays.sort(numsWithIndex, Comparator.comparingInt(a -> a[0]));
        int left = 0, right = numsWithIndex.length - 1;
        while (left < right) {
            int sum = numsWithIndex[left][0] + numsWithIndex[right][0];
            if (sum == target) return new int[]{numsWithIndex[left][1], numsWithIndex[right][1]};
            if (sum > target) right--;
            else left++;
        }
        return new int[]{-1, -1};
    }
}
