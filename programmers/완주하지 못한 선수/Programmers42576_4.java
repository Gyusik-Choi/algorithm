package com.example;

import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;

public class Programmers42576_4 {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> cnt = new HashMap<>();
        Arrays.stream(participant)
                .forEach(p -> cnt.put(p, cnt.getOrDefault(p, 0) + 1));
        Arrays.stream(completion)
                .forEach(c -> cnt.put(c, cnt.getOrDefault(c, 1) - 1));
        return cnt.entrySet().stream()
                .filter(e -> e.getValue() > 0)
                .map(Map.Entry::getKey)
                .findFirst()
                .orElseThrow();
    }
}
