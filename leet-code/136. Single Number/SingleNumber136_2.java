package com.example;

import java.util.Arrays;

public class SingleNumber136_2 {
    public int singleNumber(int[] nums) {
        return Arrays
                .stream(nums)
                .reduce((x, y) -> x ^ y)
                .getAsInt();
    }
}
