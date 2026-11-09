package com.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Programmers42576_5 {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();
        for (String p : participant) {
            map.put(p, map.getOrDefault(p, 0) + 1);
        }
        for (String c : completion) {
            if (!map.containsKey(c)) {
                return c;
            }
            if (map.get(c) == 1) {
                map.remove(c);
            } else {
                map.put(c, map.get(c) - 1);
            }
        }
        return new ArrayList<>(map.keySet()).getFirst();
    }
}
