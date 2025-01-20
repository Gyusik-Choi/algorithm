package com.example;

import java.util.Arrays;

public class MajorityElement169_3 {

    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }
}
