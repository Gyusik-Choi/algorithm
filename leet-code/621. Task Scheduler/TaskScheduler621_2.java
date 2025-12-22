package com.example;

import java.util.*;

public class TaskScheduler621_2 {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> map = new HashMap<>();
        for (char task : tasks) {
            map.put(task, map.getOrDefault(task, 0) + 1);
        }
        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> b.count - a.count);
        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
            pq.add(new Node(entry.getKey(), entry.getValue()));
        }
        List<Character> schedule = new ArrayList<>();
        while (!pq.isEmpty()) {
            List<Node> toAdd = new ArrayList<>();
            boolean isInsert = false;
            while (!pq.isEmpty()) {
                if (schedule.isEmpty() || isPossibleToAdd(pq, schedule, Math.min(schedule.size(), n))) {
                    Node node = pq.poll();
                    if (node.count > 0) {
                        schedule.add(node.value);
                        if (node.count - 1 > 0) {
                            pq.add(node.minusCount());
                        }
                    }
                    isInsert = true;
                    break;
                }
                Node node = pq.poll();
                toAdd.add(node);
            }
            if (!isInsert) {
                schedule.add('a');
            }
            pq.addAll(toAdd);
        }
        return schedule.size();
    }

    private boolean isPossibleToAdd(PriorityQueue<Node> pq, List<Character> schedule, int minLength) {
        for (int i = schedule.size() - 1; i > schedule.size() - 1 - minLength; i--) {
            if (schedule.get(i) == pq.peek().value) {
                return false;
            }
        }
        return true;
    }

    private static class Node {
        public final Character value;
        public final int count;

        Node(Character value, int count) {
            this.value = value;
            this.count = count;
        }

        public Node minusCount() {
            return new Node(value, count - 1);
        }
    }
}
