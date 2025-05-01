package com.example.algorithm;

import java.util.*;

public class ReconstructItinerary332_3 {
//     테스트 케이스
//    List<String> itinerary = r.findItinerary(List.of(
//            List.of("JFK", "SFO"),
//            List.of("JFK", "ATL"),
//            List.of("SFO", "JFK"),
//            List.of("ATL", "AAA"),
//            List.of("AAA", "ATL"),
//            List.of("ATL", "BBB"),
//            List.of("BBB", "ATL"),
//            List.of("ATL", "CCC"),
//            List.of("CCC", "ATL"),
//            List.of("ATL", "DDD"),
//            List.of("DDD", "ATL"),
//            List.of("ATL", "EEE"),
//            List.of("EEE", "ATL"),
//            List.of("ATL", "FFF"),
//            List.of("FFF", "ATL"),
//            List.of("ATL", "GGG"),
//            List.of("GGG", "ATL"),
//            List.of("ATL", "HHH"),
//            List.of("HHH", "ATL"),
//            List.of("ATL", "III"),
//            List.of("III", "ATL"),
//            List.of("ATL", "JJJ"),
//            List.of("JJJ", "ATL"),
//            List.of("ATL", "KKK"),
//            List.of("KKK", "ATL"),
//            List.of("ATL", "LLL"),
//            List.of("LLL", "ATL"),
//            List.of("ATL", "MMM"),
//            List.of("MMM", "ATL"),
//            List.of("ATL", "NNN"),
//            List.of("NNN", "ATL"))
//    );
    public List<String> findItinerary(List<List<String>> tickets) {
        // 올바른 경로가 아니라서 다른 경로를 탐색해야 할 수 있다
        // 재귀적으로 탐색하면서 올바른 경로가 나오는 가장 첫번째 경로가 정답이 된다
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
        dfs(routes, visit, answer, "JFK");
        return answer;
    }

    private void dfs(Map<String, List<String>> routes,
                        Map<String, Map<String, Boolean>> visited,
                        List<String> history,
                        String departure) {
        if (useEveryTicket(visited)) {
            return;
        }

        for (String arrival : routes.get(departure)) {
            if (visited.get(departure).get(arrival)) {
                continue;
            }
            visited.get(departure).put(arrival, true);
            dfs(routes, visited, history, arrival);
            history.add(0, departure);
        }
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
