package com.example;

import java.util.HashMap;
import java.util.Map;

public class ValidAnagram242_3 {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();
        for (char c : s.toCharArray()) sMap.put(c, sMap.getOrDefault(c, 0) + 1);
        for (char c : t.toCharArray()) tMap.put(c, tMap.getOrDefault(c, 0) + 1);
        for (Map.Entry<Character, Integer> entry : sMap.entrySet()) {
            // 키가 없는 경우
            if (!tMap.containsKey(entry.getKey())) return false;
            // 키는 있지만 값이 다른 경우
            if (!tMap.get(entry.getKey()).equals(entry.getValue())) return false;
        }
        // sMap 에는 없는데 tMap 에만 키가 있는 경우
        // (위에서 sMap 을 loop 를 돌면서 tMap 과 비교했다
        // sMap 에 있는 키가 모두 tMap 에 있으면서
        // sMap 의 각 값이 모두 tMap 의 값과 일치한다 하더라도
        // sMap 에는 없는 키가 tMap 에만 있을 수도 있다)
        return sMap.size() == tMap.size();
    }
}
