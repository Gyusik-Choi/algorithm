package com.example;

import java.util.HashMap;
import java.util.Map;

public class LongestSubstringWithoutRepeatingCharacters3_5 {
    public int lengthOfLongestSubstring(String s) {
        // 문자 해시맵
        Map<Character, Integer> charMap = new HashMap<>();
        // 인덱스 해시맵
        Map<Integer, Character> indexMap = new HashMap<>();
        int maxLength = 0;
        int minIdx = 0;
        for (int i = 0; i < s.length(); i++) {
            char charKey = s.charAt(i);
            if (charMap.containsKey(charKey)) {
                int idx = charMap.get(charKey);
                minIdx = idx + 1;
                while (idx >= 0 && indexMap.containsKey(idx)) {
                    Character cKey = indexMap.get(idx);
                    indexMap.remove(idx);
                    charMap.remove(cKey);
                    idx -= 1;
                }
            }
            charMap.put(charKey, i);
            indexMap.put(i, charKey);
            maxLength = Math.max(maxLength, i - minIdx + 1);
        }
        return maxLength;
    }
}
