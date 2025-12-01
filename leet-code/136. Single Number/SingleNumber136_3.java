package com.example;

import java.util.Arrays;

public class SingleNumber136_3 {
    public int singleNumber(int[] nums) {
        return Arrays.stream(nums).reduce((a, b) -> a ^ b).getAsInt();
    }
}
