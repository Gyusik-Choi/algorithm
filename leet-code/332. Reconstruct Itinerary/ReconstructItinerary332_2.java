package com.example;

import java.util.*;

public class ReconstructItinerary332_2 {
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, List<String>> routes = new HashMap<>();
        for (List<String> ticket : tickets) {
            String from = ticket.get(0);
            String to = ticket.get(1);
            List<String> values = routes.getOrDefault(from, new ArrayList<>());
            values.add(to);
            routes.put(from, values);
        }
        for (List<String> value : routes.values()) {
            value.sort(String::compareTo);
        }

        List<String> answer = new ArrayList<>();
        dfs(routes, answer, "JFK");
        return answer;
    }

    private void dfs(Map<String, List<String>> routes,
                     List<String> history,
                     String departure) {
        while (routes.containsKey(departure) && !routes.get(departure).isEmpty()) {
            String arrival = routes.get(departure).remove(0);
            dfs(routes, history, arrival);
        }
        history.add(0, departure);
    }
}
