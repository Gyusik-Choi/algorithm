package com.example;

import java.util.*;

public class ReconstructItinerary332_2 {
    public List<String> findItinerary(List<List<String>> tickets) {
        // 올바른 경로가 아니라서
        // 다른 경로를 탐색해야 할 수 있다
        // 재귀적으로 탐색하면서
        // 올바른 경로가 나오는
        // 가장 첫번째 경로가 정답이 된다
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

        Map<String, Map<String, Boolean>> visit = new HashMap<>();
        for (String key : routes.keySet()) {
            visit.put(key, new HashMap<>());
            for (String value : routes.get(key)) {
                visit.get(key).put(value, false);
            }
        }

        List<String> answer = new ArrayList<>();
        answer.add("JFK");
        dfs(routes, visit, answer, "JFK");
        return answer;
    }

    private boolean dfs(Map<String, List<String>> routes,
                     Map<String, Map<String, Boolean>> visited,
                     List<String> history,
                     String departure) {
        if (useEveryTicket(visited)) {
            return true;
        }

        for (String arrival : routes.get(departure)) {
            if (visited.get(departure).get(arrival)) {
                continue;
            }
            visited.get(departure).put(arrival, true);
            history.add(arrival);
            if (dfs(routes, visited, history, arrival)) {
                return true;
            }
            visited.get(departure).put(arrival, false);
            history.remove(history.size() - 1);
        }
        return false;
    }

    private boolean useEveryTicket(Map<String, Map<String, Boolean>> visited) {
        List<List<Boolean>> list = visited.values()
                .stream()
                .map(item -> item.values().stream().toList())
                .toList();

        return list
                .stream()
                .flatMap(item -> item.stream())
                .noneMatch(item -> item == false);
    }
}
