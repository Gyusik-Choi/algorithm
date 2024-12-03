package com.example;

import java.util.Arrays;

public class LargestNumber179 {
    public String largestNumber(int[] nums) {
        for (int idx = 0; idx < nums.length; idx++) {
            int i = idx;
            int num = nums[idx];

            while (i > 0 && toSwap(nums[i - 1], num)) {
                nums[i] = nums[i - 1];
                i -= 1;
            }
            nums[i] = num;
        }

        return nums[0] == 0
                ? "0"
                // https://denodo1.tistory.com/216
                // https://zhfvkq.tistory.com/5
                : Arrays.toString(nums).replaceAll("[\\[\\]\\s,]", "");
    }

    private boolean toSwap(int a, int b) {
        return Double.parseDouble(Integer.toString(a).concat(Integer.toString(b))) <
                Double.parseDouble(Integer.toString(b).concat(Integer.toString(a)));
    }
}
