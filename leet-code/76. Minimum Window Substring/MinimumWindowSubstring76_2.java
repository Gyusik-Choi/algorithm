package com.example;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MinimumWindowSubstring76_2 {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) {
            return "";
        }
        // 오른쪽으로 이동하고
        // 왼쪽도 이동할 수 있으면 최대한 이동한다
        // 왼쪽을 이동하려면
        // 이동했을 때 최소로 맞춰야할 각 문자별 갯수를 모두 충족해야 한다
        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();
        for (char tChar : t.toCharArray()) {
            tMap.put(tChar, tMap.getOrDefault(tChar, 0) + 1);
        }
        boolean isModified = false;
        int start = 0, end = s.length() - 1;
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            char sCharRight = s.charAt(right);
            if (!tMap.containsKey(sCharRight)) {
                continue;
            }
            sMap.put(sCharRight, sMap.getOrDefault(sCharRight, 0) + 1);
            if (containsAll(sMap, tMap)) {
                while (left < right) {
                    char sCharLeft = s.charAt(left);
                    if (!sMap.containsKey(sCharLeft)) {
                        left += 1;
                        continue;
                    }
                    if (sMap.get(sCharLeft) > tMap.get(sCharLeft)) {
                        sMap.put(sCharLeft, sMap.get(sCharLeft) - 1);
                        left += 1;
                        continue;
                    }
                    break;
                }
                if (end - start >= right - left) {
                    start = left;
                    end = right;
                    isModified = true;
                }
            }
        }
        return isModified ? s.substring(start, end + 1) : "";
    }

    private boolean containsAll(Map<Character, Integer> sMap, Map<Character, Integer> tMap) {
        Set<Character> sKeys = sMap.keySet();
        if (sKeys.isEmpty()) {
            return false;
        }
        Set<Character> tKeys = tMap.keySet();
        for (Character key : tKeys) {
            if (!sMap.containsKey(key)) {
                return false;
            }
            if (sMap.get(key) < tMap.get(key)) {
                return false;
            }
        }
        return true;
    }

//    통과 코드 2)
//    public String minWindow(String s, String t) {
//        if (s.length() < t.length()) {
//            return "";
//        }
//        if (s.equals(t)) {
//            return s;
//        }
//        Map<Character, Integer> sMap = new HashMap<>();
//        Map<Character, Integer> tMap = new HashMap<>();
//        for (char tChar : t.toCharArray()) {
//            tMap.put(tChar, tMap.getOrDefault(tChar, 0) + 1);
//        }
//        boolean isModified = false;
//        int start = 0, end = s.length() - 1;
//        int left = 0;
//        for (int right = 0; right < s.length(); right++) {
//            char c = s.charAt(right);
//            if (!tMap.containsKey(c)) {
//                continue;
//            }
//            sMap.put(c, sMap.getOrDefault(c, 0) + 1);
//            if (containsAll(sMap, tMap)) {
//                while (left < right) {
//                    char sCharLeft = s.charAt(left);
//                    if (!sMap.containsKey(sCharLeft)) {
//                        left += 1;
//                        continue;
//                    }
//                    if (sMap.get(sCharLeft) > tMap.get(sCharLeft)) {
//                        sMap.put(sCharLeft, sMap.get(sCharLeft) - 1);
//                        left += 1;
//                        continue;
//                    }
//                    break;
//                }
//                if (end - start >= right - left) {
//                    start = left;
//                    end = right;
//                    isModified = true;
//                }
//            }
//        }
//        if (!isModified) {
//            return "";
//        }
//        return s.substring(start, end + 1);
//    }
//
//    private boolean containsAll(Map<Character, Integer> sMap, Map<Character, Integer> tMap) {
//        Set<Character> sKeys = sMap.keySet();
//        if (sKeys.isEmpty()) {
//            return false;
//        }
//        Set<Character> tKeys = tMap.keySet();
//        for (Character key : tKeys) {
//            if (!sMap.containsKey(key)) {
//                return false;
//            }
//            if (sMap.get(key) < tMap.get(key)) {
//                return false;
//            }
//        }
//        return true;
//    }

//    통과 코드 1)
//    public String minWindow(String s, String t) {
//        if (s.length() < t.length()) {
//            return "";
//        }
//        if (s.length() == 1 && t.length() == 1 && !s.equals(t)) {
//            return "";
//        }
//        if (s.equals(t)) {
//            return s;
//        }
//        Map<Character, Integer> sMap = new HashMap<>();
//        Map<Character, Integer> tMap = new HashMap<>();
//        for (char tChar : t.toCharArray()) {
//            tMap.put(tChar, tMap.getOrDefault(tChar, 0) + 1);
//        }
//        int start = 0, end = s.length() - 1;
//        boolean isModified = false;
//        int left = 0;
//        for (int right = 0; right < s.length(); right++) {
//            char c = s.charAt(right);
//            if (!tMap.containsKey(c)) {
//                continue;
//            }
//            sMap.put(c, sMap.getOrDefault(c, 0) + 1);
//            if (containsAll(sMap, tMap)) {
//                while (left < right && (!sMap.containsKey(s.charAt(left)) || sMap.get(s.charAt(left)) > tMap.get(s.charAt(left)))) {
//                    if (!sMap.containsKey(s.charAt(left))) {
//                        left += 1;
//                        continue;
//                    }
//                    if (sMap.get(s.charAt(left)) > tMap.get(s.charAt(left))) {
//                        sMap.put(s.charAt(left), sMap.get(s.charAt(left)) - 1);
//                        left += 1;
//                    }
//                }
//                if (end - start >= right - left) {
//                    start = left;
//                    end = right;
//                    isModified = true;
//                }
//            }
//        }
//        if (!isModified) {
//            return "";
//        }
//        return s.substring(start, end + 1);
//    }
//
//    private boolean containsAll(Map<Character, Integer> sMap, Map<Character, Integer> tMap) {
//        Set<Character> sKeys = sMap.keySet();
//        if (sKeys.isEmpty()) {
//            return false;
//        }
//        Set<Character> tKeys = tMap.keySet();
//        for (Character key : tKeys) {
//            if (!sMap.containsKey(key)) {
//                return false;
//            }
//            if (sMap.get(key) < tMap.get(key)) {
//                return false;
//            }
//        }
//        return true;
//    }
}
