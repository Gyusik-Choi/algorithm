package com.example;

import java.util.*;

public class GroupAnagrams49_4 {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String str : strs) {
            char[] arr = str.toCharArray();
            Arrays.sort(arr);
            String s = Arrays.toString(arr);
            map.putIfAbsent(s, new ArrayList<>());
            map.get(s).add(str);
        }
        return map.values().stream().toList();
    }
}
