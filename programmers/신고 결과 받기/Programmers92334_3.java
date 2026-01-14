package com.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Programmers92334_3 {
    public int[] solution(String[] id_list, String[] report, int k) {
        Map<String, List<String>> reported = new HashMap<>();
        Map<String, Integer> mailCount = new HashMap<>();
        for (String id : id_list) {
            mailCount.putIfAbsent(id, 0);
        }
        for (String reportInfo : report) {
            String[] info = reportInfo.split(" ");
            List<String> value = reported.getOrDefault(info[1], new ArrayList<>());
            if (!value.contains(info[0])) {
                value.add(info[0]);
            }
            reported.put(info[1], value);
        }
        for (Map.Entry<String, List<String>> entry : reported.entrySet()) {
            if (entry.getValue().size() >= k) {
                for (String name : entry.getValue()) {
                    mailCount.put(name, mailCount.get(name) + 1);
                }
            }
        }
        int[] answer = new int[id_list.length];
        for (int i = 0; i < id_list.length; i++) {
            answer[i] = mailCount.get(id_list[i]);
        }
        return answer;
    }
}
