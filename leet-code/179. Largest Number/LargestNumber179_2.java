package com.example;

import java.util.Arrays;
import java.util.stream.Collectors;

public class LargestNumber179_2 {
    public String largestNumber(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            int insertNum = nums[i];
            int idx = i;
            while (idx > 0 && compare(nums[idx - 1], insertNum)) {
                nums[idx] = nums[idx - 1];
                idx -= 1;
            }
            nums[idx] = insertNum;
        }

        return nums[0] == 0
                ? "0"
                : Arrays.stream(nums)
                    .mapToObj(String::valueOf)
                    .collect(Collectors.joining());
    }

    private boolean compare(int num1, int num2) {
        return Double.parseDouble(String.valueOf(num1) + String.valueOf(num2)) <
                Double.parseDouble(String.valueOf(num2) + String.valueOf(num1));
    }
}
