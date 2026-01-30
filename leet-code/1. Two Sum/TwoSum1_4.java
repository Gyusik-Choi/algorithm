package com.example.algorithm;

import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.IntStream;

public class TwoSum1_4 {
    public int[] twoSum(int[] nums, int target) {
        int[][] arr = IntStream
                .range(0, nums.length)
                .mapToObj(i -> new int[]{nums[i], i})
                .toArray(int[][]::new);
        Arrays.sort(arr, Comparator.comparingInt(o -> o[0]));
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int sums = arr[left][0] + arr[right][0];
            if (sums == target) {
                break;
            }
            if (sums < target) {
                left += 1;
            } else {
                right -= 1;
            }
        }
        return new int[]{arr[left][1], arr[right][1]};
    }
}
