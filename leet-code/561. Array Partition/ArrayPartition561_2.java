package com.example.algorithm;

import java.util.Arrays;
import java.util.stream.IntStream;

public class ArrayPartition561_3 {

    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        return IntStream
                .range(0, nums.length - 1)
                .filter(i -> i % 2 == 0)
                .map(i -> nums[i])
                .sum();
    }
}
