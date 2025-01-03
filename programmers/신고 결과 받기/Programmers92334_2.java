package com.example;

import java.util.*;

public class Programmers92334_2 {

    public int[] solution(String[] id_list, String[] report, int k) {
        Map<String, Set<String>> map = new HashMap<>();
        for (String r : report) {
            String[] names = r.split(" ");
            String caller = names[0];
            String callee = names[1];
            Set<String> set = map.getOrDefault(callee, new HashSet<>());
            set.add(caller);
            map.put(callee, set);
        }

        Map<String, Integer> counts = new HashMap<>();
        for (Set<String> set : map.values()) {
            if (set.size() >= k) {
                for (String caller : set) {
                    counts.put(caller, counts.getOrDefault(caller, 0) + 1);
                }
            }
        }

        return Arrays
                .stream(id_list)
                // counts 에 해당하는 key 가 없을 수 있어서
                // get 이 아닌 getOrDefault 로 가져와야 한다
                .map(id -> counts.getOrDefault(id, 0))
                .mapToInt(Integer::valueOf)
                .toArray();
    }
}
