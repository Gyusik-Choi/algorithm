package com.example.algorithm;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class MostCommonWord819_4 {
    public String mostCommonWord(String paragraph, String[] banned) {
        String[] words = paragraph
                .replaceAll("\\W+", " ")
                .toLowerCase()
                .split(" ");
        Map<String, Integer> count = new HashMap<>();
        for (String word : words) {
            if (contains(word, banned)) {
                continue;
            }
            count.putIfAbsent(word, 0);
            count.put(word, count.get(word) + 1);
        }
        return Collections
                .max(count.entrySet(), Map.Entry.comparingByValue())
                .getKey();
    }

    private boolean contains(String word, String[] banned) {
        for (String bannedWord : banned) {
            if (bannedWord.equals(word)) {
                return true;
            }
        }
        return false;
    }
}
