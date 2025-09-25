package com.example;

import java.util.HashMap;
import java.util.Map;

public class LongestSubstringWithoutRepeatingCharacters3_4 {
    // 해시맵에는 문자마다 가장 마지막에 나타나는 인덱스 저장
    // left 가 처음에는 0이다가 겹치는 문자가 나타나면
    // (단, 겹치는 문자가 left 보다 크거나 같아야 한다)
    // 겹치는 문자의 value + 1 로 left 를 갱신
    // 최대 길이는 Math.max(기존 최대 길이, 현재 인덱스 - left + 1)
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int maxLength = 0;
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (map.containsKey(c) && map.get(c) >= left) {
                left = map.get(c) + 1;
            } else {
                maxLength = Math.max(maxLength, right - left + 1);
            }
            map.put(c, right);
        }
        return maxLength;
    }
}
