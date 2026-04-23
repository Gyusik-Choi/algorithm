package com.example;

import java.util.*;

public class Programmers43164_3 {
    public String[] solution(String[][] tickets) {
        Map<String, PriorityQueue<String>> map = new HashMap<>();
        for (String[] ticket : tickets) {
            map.putIfAbsent(ticket[0], new PriorityQueue<>());
            map.get(ticket[0]).add(ticket[1]);
        }
        List<String> path = traverse(map, "ICN", new ArrayList<>());
        return path.toArray(new String[0]);
    }

    private List<String> traverse(Map<String, PriorityQueue<String>> route, String departure, List<String> itinerary) {
        while (route.containsKey(departure) && !route.get(departure).isEmpty()) {
            traverse(route, route.get(departure).poll(), itinerary);
        }
        itinerary.add(0, departure);
        return itinerary;
    }
}
