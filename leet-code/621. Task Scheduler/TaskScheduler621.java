package com.example;

import java.util.*;

public class TaskScheduler621_3 {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> map = new HashMap<>();
        for (char c : tasks) map.put(c, map.getOrDefault(c, 0) + 1);
        // 갯수 내림차순, 알파벳(아스키 코드값) 오름차순
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] == b[1] ? a[0] - b[0] : b[1] - a[1]);
        for (Map.Entry<Character, Integer> entry : map.entrySet())
            pq.offer(new int[]{entry.getKey(), entry.getValue()});

        List<Integer> taskList = new ArrayList<>();
        while (!pq.isEmpty()) {
            int[] item = pq.poll();
            taskList.add(item[0]);

            List<int[]> temp = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (!pq.isEmpty()) {
                    int[] it = pq.poll();
                    temp.add(it);
                    taskList.add(it[0]);
                } else {
                    taskList.add(-1);
                }
            }

            item[1] -= 1;
            if (item[1] != 0) pq.add(item);
            for (int[] i : temp) {
                i[1] -= 1;
                if (i[1] != 0) pq.add(i);
            }
        }

        // List 뒤에 idle 이 들어간 경우를 제거
        while (taskList.get(taskList.size() - 1) == -1) taskList.remove(taskList.size() - 1);
        return taskList.size();
    }
}
