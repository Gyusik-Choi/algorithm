package com.example.algorithm;

import java.util.Arrays;
import java.util.stream.IntStream;

public class ArrayPartition561_4 {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        return IntStream
                .range(0, nums.length)
                .filter(i -> i % 2 == 0)
                .reduce(0, (acc, cur) -> acc + nums[cur]);
    }
}
