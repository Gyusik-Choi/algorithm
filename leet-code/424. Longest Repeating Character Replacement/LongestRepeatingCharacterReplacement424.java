package com.example;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class LongestRepeatingCharacterReplacement424 {
    public int characterReplacement(String s, int k) {
        int left = 0;
        Map<Character, Integer> map = new HashMap<>();
        for (int right = 0; right < s.length(); right++) {
            map.put(s.charAt(right), map.getOrDefault(s.charAt(right), 0) + 1);
            int maxCharCnt = Collections.max(map.values());
            if (maxCharCnt + k < right - left + 1) {
                map.put(s.charAt(left), map.getOrDefault(s.charAt(left), 0) - 1);
                left += 1;
            }
        }
        return s.length() - left;
    }
}
