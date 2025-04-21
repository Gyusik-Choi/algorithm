package com.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LongestSubstringWithoutRepeatingCharacters3_3 {
    /**
     * lengthOfLongestSubstringOld 를 개선한 버전
     */
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        int prev = 0;
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char character = s.charAt(i);
            if (map.containsKey(character) && map.get(character) >= prev) {
                prev = map.get(character) + 1;
            } else {
                maxLength = Math.max(maxLength, i - prev + 1);
            }
            map.put(character, i);
        }
        return maxLength;
    }

    /**
     * 주의할 반례 -> tmmzuxt(5), aabaab!bb(3)
     */
    public int lengthOfLongestSubstringOld(String s) {
        int maxLength = 0;
        int prev = 0;
        Map<Character, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char character = s.charAt(i);
            if (map.containsKey(character)) {
                // prev 의 범위 내에 있는 문자가 중복된 경우 prev 갱신
                if (map.get(character).get(0) >= prev) {
                    prev = map.get(character).get(0) + 1;
                }
                // map 에서 첫번째 값에 접근 하기 때문에
                // prev 바깥에 있는 문자에 접근하지 않도록 기존 첫번째 문자를 제거
                map.get(character).remove(0);
            }
            // map 에 중복된 문자가 있더라도 prev 이전 범위에 있는 문자인 경우
            // maxLength 를 갱신할 수 있기 때문에 항상 갱신 시도
            maxLength = Math.max(maxLength, i - prev + 1);
            List<Integer> value = map.getOrDefault(character, new ArrayList<>());
            value.add(i);
            map.put(character, value);
        }
        return maxLength;
    }
}
