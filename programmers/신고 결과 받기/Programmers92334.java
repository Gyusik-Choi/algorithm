package com.example;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Programmers92334 {

    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Map<String, Set<String>> map = new HashMap<>();
        for (String r : report) {
            String[] names = r.split(" ");
            String caller = names[0];
            String callee = names[1];
            Set<String> set = map.getOrDefault(callee, new HashSet<>());
            set.add(caller);
            map.put(callee, set);
        }

        for (Map.Entry<String, Set<String>> entry : map.entrySet()) {
            if (entry.getValue().size() >= k) {
                for (String reporter : entry.getValue()) {
                    answer[getIdx(id_list, reporter)] += 1;
                }
            }
        }
        return answer;
    }

    private int getIdx(String[] idList, String caller) {
        for (int i = 0; i < idList.length; i++) {
            if (idList[i].equals(caller)) {
                return i;
            }
        }
        return -1;
    }
}
