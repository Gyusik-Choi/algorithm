package com.example.algorithm;

import java.util.HashMap;
import java.util.Map;

public class LongestRepeatingCharacterReplacement424_3 {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> map = new HashMap<>();
        int maxLength = 1;
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            map.put(s.charAt(right), map.getOrDefault(s.charAt(right), 0) + 1);
            if (getMaxLength(map) + k >= right - left + 1) {
                maxLength = Math.max(maxLength, right - left + 1);
            }
            while (getMaxLength(map) + k < right - left + 1) {
                map.put(s.charAt(left), map.get(s.charAt(left)) - 1);
                left += 1;
            }
        }
        return maxLength;
    }

    private int getMaxLength(Map<Character, Integer> map) {
        return map.values().stream()
                .max(Integer::compareTo)
                .get();
    }
}
