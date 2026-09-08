package com.example;

import java.util.*;

public class MostCommonWord819_5 {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> ban = new HashSet<>(List.of(banned));
        Map<String, Integer> count = new HashMap<>();
        String[] words = paragraph
                .toLowerCase()
                .replaceAll("[\\s!?',;.]+", " ")
                .trim()
                .split(" ");
        for (String word : words) {
            if (!ban.contains(word)) {
                count.merge(word, 1, Integer::sum);
            }
        }
        return Collections.max(count.entrySet(), Map.Entry.comparingByValue()).getKey();
    }
}
