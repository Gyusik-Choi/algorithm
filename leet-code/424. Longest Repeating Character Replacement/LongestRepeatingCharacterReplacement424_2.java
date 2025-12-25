package com.example;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class LongestRepeatingCharacterReplacement424_2 {
    public int characterReplacement(String s, int k) {
        int left = 0;
        Map<Character, Integer> map = new HashMap<>();
        for (int right = 0; right < s.length(); right++) {
            map.put(s.charAt(right), map.getOrDefault(s.charAt(right), 0) + 1);
            int maxCount = Collections.max(map.values());
            // right 부터 left 까지의 길이는
            // right - left 가 아니라
            // right - left + 1 이다
            // 교재는 이 풀이와 달리
            // + 1 을 하지 않고 아예 for 문의 right 를 1부터 시작하여
            // charAt 접근시 right - 1 로 하고
            // 아래의 if 문에서 길이 비교를 할 때는
            // right - left - maxCount > k 로 비교한다
            if (right - left + 1 - maxCount > k) {
                map.put(s.charAt(left), map.get(s.charAt(left)) - 1);
                left += 1;
                // AABBA
            }
        }
        return s.length() - left;
    }
}
