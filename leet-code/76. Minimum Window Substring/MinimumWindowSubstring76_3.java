package com.example;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

public class MinimumWindowSubstring76_3 {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) {
            return "";
        }
        Map<Character, Integer> tMap = new HashMap<>();
        for (char c : t.toCharArray()) {
            tMap.put(c, tMap.getOrDefault(c, 0) + 1);
        }
        int minLength = Integer.MAX_VALUE;
        int start = 0;
        Map<Character, Integer> sMap = new HashMap<>();
        Deque<Integer> deq = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            deq.addLast(i);
            sMap.put(s.charAt(i), sMap.getOrDefault(s.charAt(i), 0) + 1);
            while (!deq.isEmpty() && canRemoveFront(sMap, tMap, s.charAt(deq.getFirst()))) {
                Integer idx = deq.pollFirst();
                sMap.put(s.charAt(idx), sMap.getOrDefault(s.charAt(idx), 0) - 1);
            }
            if (isValidWindow(sMap, tMap) && minLength > deq.size()) {
                minLength = deq.size();
                start = deq.getFirst();
            }
        }
        return minLength == Integer.MAX_VALUE ? "" : s.substring(start, start + minLength);
    }

    private boolean canRemoveFront(Map<Character, Integer> sMap, Map<Character, Integer> tMap, char c) {
        return !tMap.containsKey(c) || sMap.containsKey(c) && sMap.get(c) > tMap.get(c);
    }

    private boolean isValidWindow(Map<Character, Integer> sMap, Map<Character, Integer> tMap) {
        return tMap.entrySet().stream()
                .allMatch(entry -> sMap.getOrDefault(entry.getKey(), 0) >= entry.getValue());
    }
}
