package com.example;

import java.util.*;

public class Programmers43164_2 {
    public String[] solution(String[][] tickets) {
        Map<String, PriorityQueue<String>> map = new HashMap<>();
        Arrays.stream(tickets).forEach(ticket -> {
           map.putIfAbsent(ticket[0], new PriorityQueue<>());
           map.get(ticket[0]).add(ticket[1]);
        });
        List<String> answer = new LinkedList<>();
        traverse(map, answer, "ICN");
        return answer.toArray(new String[0]);
    }

    private void traverse(Map<String, PriorityQueue<String>> map, List<String> course, String departure) {
        while (map.containsKey(departure) && !map.get(departure).isEmpty()) {
            traverse(map, course, map.get(departure).poll());
        }
        course.add(0, departure);
    }
}
