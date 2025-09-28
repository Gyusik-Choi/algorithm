package com.example;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Programmers42576_3 {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> athletes = new HashMap<>();
        Arrays.stream(participant).forEach(p -> athletes.put(p, athletes.getOrDefault(p, 0) + 1));
        Arrays.stream(completion).forEach(c -> {
            if (athletes.containsKey(c) && athletes.get(c) > 1) {
                athletes.put(c, athletes.get(c) - 1);
            } else {
                athletes.remove(c);
            }
        });
        return new ArrayList<>(athletes.keySet()).get(0);
    }
}
