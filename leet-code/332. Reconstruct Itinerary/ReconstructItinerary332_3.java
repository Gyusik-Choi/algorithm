package com.example;

import java.util.*;

public class ReconstructItinerary332_3 {
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, PriorityQueue<String>> map = new HashMap<>();
        tickets.forEach(ticket -> {
           map.putIfAbsent(ticket.get(0), new PriorityQueue<>());
           map.get(ticket.get(0)).add(ticket.get(1));
        });
        List<String> result = new LinkedList<>();
        Deque<String> stack = new LinkedList<>();
        stack.push("JFK");
        while (!stack.isEmpty()) {
            // while 문을 돌 때마다 새로 스택의 최상단 요소를 구한다
            // 스택에 채울 수 있는 요소들을 다 구한 이후에
            // 스택에서 요소를 꺼내서 result 의 첫번째 인덱스에 넣는다
            while (map.containsKey(stack.getFirst()) && !map.get(stack.getFirst()).isEmpty()) {
                stack.push(map.get(stack.getFirst()).poll());
            }
            result.add(0, stack.pop());
        }
        return result;
    }
}
