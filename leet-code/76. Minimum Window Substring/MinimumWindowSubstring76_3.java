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
            while (!deq.isEmpty() && !tMap.containsKey(s.charAt(deq.getFirst()))) {
                deq.pollFirst();
            }
            while (!deq.isEmpty() && canRemove(sMap, tMap, s.charAt(deq.getFirst()))) {
                Integer idx = deq.pollFirst();
                sMap.put(s.charAt(idx), sMap.getOrDefault(s.charAt(idx), 0) - 1);
            }
            if (containsSubstring(sMap, tMap) && minLength > deq.size()) {
                minLength = deq.size();
                start = deq.getFirst();
            }
        }
        return minLength == Integer.MAX_VALUE ? "" : s.substring(start, start + minLength);
    }

    private boolean canRemove(Map<Character, Integer> sMap, Map<Character, Integer> tMap, char c) {
        if (containsSubstring(sMap, tMap) && (!tMap.containsKey(c) || sMap.containsKey(c) && sMap.get(c) > tMap.get(c))) {
            return true;
        }
        return false;
    }

    private boolean containsSubstring(Map<Character, Integer> sMap, Map<Character, Integer> tMap) {
        for (Map.Entry<Character, Integer> entry : tMap.entrySet()) {
            if (!sMap.containsKey(entry.getKey()) || sMap.get(entry.getKey()) < entry.getValue()) {
                return false;
            }
        }
        return true;
    }
}

//package com.example;
//
//import java.util.ArrayDeque;
//import java.util.Deque;
//import java.util.HashMap;
//import java.util.Map;
//
//public class MinimumWindowSubstring76_3 {
//    public String minWindow(String s, String t) {
//        if (s.length() < t.length()) {
//            return "";
//        }
//        Map<Character, Integer> tMap = new HashMap<>();
//        for (char c : t.toCharArray()) {
//            tMap.put(c, tMap.getOrDefault(c, 0) + 1);
//        }
//        int minLength = Integer.MAX_VALUE;
//        int start = 0;
//        Map<Character, Integer> sMap = new HashMap<>();
//        Deque<Integer> deq = new ArrayDeque<>();
//        for (int i = 0; i < s.length(); i++) {
//            while (!deq.isEmpty() && !tMap.containsKey(s.charAt(deq.getFirst()))) {
//                deq.pollFirst();
//            }
//            while (!deq.isEmpty() && canRemove(sMap, tMap, s.charAt(deq.getFirst()))) {
//                Integer idx = deq.pollFirst();
//                sMap.put(s.charAt(idx), sMap.getOrDefault(s.charAt(idx), 0) - 1);
//            }
//            deq.addLast(i);
//            sMap.put(s.charAt(i), sMap.getOrDefault(s.charAt(i), 0) + 1);
//            if (containsSubstring(sMap, tMap) && minLength > deq.size()) {
//                minLength = deq.size();
//                start = deq.getFirst();
//            }
//        }
//        while (!deq.isEmpty() && !tMap.containsKey(s.charAt(deq.getFirst()))) {
//            deq.pollFirst();
//        }
//        while (!deq.isEmpty() && canRemove(sMap, tMap, s.charAt(deq.getFirst()))) {
//            Integer idx = deq.pollFirst();
//            sMap.put(s.charAt(idx), sMap.getOrDefault(s.charAt(idx), 0) - 1);
//        }
//        if (containsSubstring(sMap, tMap) && minLength > deq.size()) {
//            minLength = deq.size();
//            start = deq.getFirst();
//        }
//        return minLength == Integer.MAX_VALUE ? "" : s.substring(start, start + minLength);
//    }
//
//    private boolean canRemove(Map<Character, Integer> sMap, Map<Character, Integer> tMap, char c) {
//        if (containsSubstring(sMap, tMap) && (!tMap.containsKey(c) || sMap.containsKey(c) && sMap.get(c) > tMap.get(c))) {
//            return true;
//        }
//        return false;
//    }
//
//    private boolean containsSubstring(Map<Character, Integer> sMap, Map<Character, Integer> tMap) {
//        for (Map.Entry<Character, Integer> entry : tMap.entrySet()) {
//            if (!sMap.containsKey(entry.getKey()) || sMap.get(entry.getKey()) < entry.getValue()) {
//                return false;
//            }
//        }
//        return true;
//    }
//}

//package com.example;
//
//import java.util.ArrayDeque;
//import java.util.Deque;
//import java.util.HashMap;
//import java.util.Map;
//
//public class MinimumWindowSubstring76_3 {
//    public String minWindow(String s, String t) {
//        // "ADOBECODEBANC", "ABC"
//        // "BANC"
//        if (s.length() < t.length()) {
//            return "";
//        }
//        Map<Character, Integer> tMap = new HashMap<>();
//        for (char c : t.toCharArray()) {
//            tMap.put(c, tMap.getOrDefault(c, 0) + 1);
//        }
//        int minLength = Integer.MAX_VALUE;
//        int start = 0;
//        Map<Character, Integer> sMap = new HashMap<>();
//        Deque<Character> deq = new ArrayDeque<>();
//        for (char c : s.toCharArray()) {
//            while (!deq.isEmpty()) {
//                deq.pollLast();
//            }
//            deq.addLast(c);
//            sMap.put(c, sMap.getOrDefault(c, 0) + 1);
//            if (containsSubstring(sMap, tMap)) {
//                if (deq.size() < minLength) {
//                    minLength = deq.size();
//                }
//            }
//        }
//        return "";
//    }
//
//    private boolean containsSubstring(Map<Character, Integer> sMap, Map<Character, Integer> tMap) {
//        for (Map.Entry<Character, Integer> entry : tMap.entrySet()) {
//            if (!sMap.containsKey(entry.getKey()) || !sMap.get(entry.getKey()).equals(entry.getValue())) {
//                return false;
//            }
//        }
//        return true;
//    }
//
//    private boolean canRemove(Map<Character, Integer> map, char c) {
//        if (!map.containsKey(c) || map.get(c) > 0) {
//            return true;
//        }
//        return false;
//    }
//}
