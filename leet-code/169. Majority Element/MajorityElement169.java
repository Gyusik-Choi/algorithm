package com.example;

import java.util.HashMap;
import java.util.Map;

public class MajorityElement169 {

    public int majorityElement(int[] nums) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int num : nums) cnt.put(num, cnt.getOrDefault(num, 0) + 1);
        int majority = 0;
        for (int num : nums) {
            if (cnt.get(num) >= (nums.length + 1) / 2) {
                majority = num;
                break;
            }
        }
        return majority;
    }
}
