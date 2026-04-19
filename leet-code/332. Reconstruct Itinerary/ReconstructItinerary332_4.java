package com.example;

import java.util.*;

public class ReconstructItinerary332_4 {
    // 오일러 경로
    // Hierholzer 알고리즘
    //
    //  막다른 노드 = 경로의 끝입니다 (모든 간선을 써야 하므로)
    //  - add(0, from) = 나중에 처리될수록 앞에 위치
    //  - 먼저 막힌 노드일수록 add(0,...)이 먼저 호출 → 뒤로 밀려남
    //
    //  처리 순서:  B → A → C → A  (add 호출 순서)
    //  결과 위치:  [A, C, A, B]   (앞에 삽입이므로 역순)
    //
    //  즉, "순서가 틀렸을 때 뒤로 보내는" 것이 아니라, "막다른 곳은 경로의 끝이다" 라는 성질을 이용해 처음부터
    //  올바른 위치에 놓는 것입니다.
    //
    //   정리하면:
    //  - "모든 간선을 한 번씩" → 오일러 경로의 정의
    //  - "막다른 곳이 경로의 끝" → Hierholzer 알고리즘의 핵심 통찰
    //
    // 한번에 올바른 경로를 찾는게 아니라 잘못된 경로를 갔다가 올바른 경로를 찾는 예시 입력
    // ->  [["A","B"], ["A","C"], ["C","A"]]
    // ->  [["A","B"], ["A","C"], ["B","D"], ["C","A"], ["D","B"]]
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, PriorityQueue<String>> map = new HashMap<>();
        for (List<String> ticket : tickets) {
            map.putIfAbsent(ticket.getFirst(), new PriorityQueue<>());
            map.get(ticket.getFirst()).add(ticket.getLast());
        }
        return traverse(map, new ArrayList<>(), "JFK");
    }

    private List<String> traverse(Map<String, PriorityQueue<String>> route, List<String> itinerary, String departure) {
        while (route.containsKey(departure) && !route.get(departure).isEmpty()) {
            traverse(route, itinerary, route.get(departure).poll());
        }
        itinerary.addFirst(departure);
        return itinerary;
    }
}
