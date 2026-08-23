package com.example;

import java.util.*;

public class Programmers92334_4 {
    public int[] solution(String[] id_list, String[] report, int k) {
        // ["muzi", "frodo", "apeach", "neo"]
        // ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
        // 2
        // -> [2,1,1,0]
        // 피신고자: [신고자]
        // 신고자: 횟수
        Map<String, Set<String>> reportee = new HashMap<>();
        for (String r : report) {
            String[] users = r.split(" ");
            reportee.putIfAbsent(users[1], new HashSet<>());
            reportee.get(users[1]).add(users[0]);
        }
        Map<String, Integer> reporter = new HashMap<>();
        for (Map.Entry<String, Set<String>> entry : reportee.entrySet()) {
            if (entry.getValue().size() >= k) {
                for (String r : entry.getValue()) {
                    reporter.put(r, reporter.getOrDefault(r, 0) + 1);
                }
            }
        }
        return Arrays.stream(id_list)
                .mapToInt(id -> reporter.getOrDefault(id, 0))
                .toArray();
    }
}
