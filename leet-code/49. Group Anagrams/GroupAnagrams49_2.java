package com.example.algorithm;

import java.util.*;

public class GroupAnagrams49_2 {

    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> wordMap = new HashMap<>();
        for (String str : strs) {
            char[] strCharArray = str.toCharArray();
            Arrays.sort(strCharArray);
            String sortedStr = Arrays.toString(strCharArray);
            List<String> words = wordMap.getOrDefault(sortedStr, new ArrayList<>());
            words.add(str);
            wordMap.put(sortedStr, words);
        }
        return new ArrayList<>(wordMap.values());
    }
}
