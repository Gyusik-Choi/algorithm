package com.example;

import java.util.Arrays;

public class SingleNumber136_4 {
    public int singleNumber(int[] nums) {
        return Arrays.stream(nums)
                .reduce((acc, cur) -> acc ^ cur)
                .getAsInt();
    }
}
