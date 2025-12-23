package com.example;

import java.util.*;

public class TaskScheduler621_2 {
//    풀이 2) - 교재 참고 이후
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> map = new HashMap<>();
        for (char task : tasks) {
            map.put(task, map.getOrDefault(task, 0) + 1);
        }
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(Node::count).reversed());
        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
            pq.add(new Node(entry.getKey(), entry.getValue()));
        }
        List<Character> schedule = new ArrayList<>();
        while (!pq.isEmpty()) {
            List<Node> toAdd = new ArrayList<>();
            int interval = 0;
            while (!pq.isEmpty()) {
                // 한번 꺼낸 node 를 내부 while 문이 종료되기 전까지는
                // 다시 넣지 않기 때문에 인터벌 사이에
                // 이미 꺼낸 node 를 다시 꺼낼 수 없다
                Node node = pq.poll();
                // n 이 아닌 n + 1 로 설정해서
                // 특정 노드로 부터 n 만큼의 간격 사이에
                // idle 이 아닌 나올 수 있는 노드를 채우도록 한다
                if (interval < n + 1) {
                    interval += 1;
                    schedule.add(node.value);
                    if (node.count > 1) {
                        toAdd.add(new Node(node.value, node.count - 1));
                    }
                } else {
                    toAdd.add(node);
                }
            }
            if (!toAdd.isEmpty()) {
                for (int i = 0; i < n + 1 - interval; i++) {
                    // 대문자만 입력으로 주어지기 때문에
                    // 겹치지 않는 임의의 소문자 a 를 idle 처럼 넣는다
                    schedule.add('a');
                }
                pq.addAll(toAdd);
            }
        }
        return schedule.size();
    }

    private record Node(Character value, int count) {}

//    풀이 1) - 교재 참고 이전
//    public int leastInterval(char[] tasks, int n) {
//        Map<Character, Integer> map = new HashMap<>();
//        for (char task : tasks) {
//            map.put(task, map.getOrDefault(task, 0) + 1);
//        }
//        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> b.count - a.count);
//        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
//            pq.add(new Node(entry.getKey(), entry.getValue()));
//        }
//        List<Character> schedule = new ArrayList<>();
//        while (!pq.isEmpty()) {
//            List<Node> toAdd = new ArrayList<>();
//            boolean isInsert = false;
//            while (!pq.isEmpty()) {
//                if (schedule.isEmpty() || isPossibleToAdd(pq, schedule, Math.min(schedule.size(), n))) {
//                    isInsert = true;
//                    Node node = pq.poll();
//                    if (node.count > 0) {
//                        schedule.add(node.value);
//                        if (node.count - 1 > 0) {
//                            pq.add(node.minusCount());
//                        }
//                    }
//                    break;
//                }
//                Node node = pq.poll();
//                toAdd.add(node);
//            }
//            if (!isInsert) {
//                schedule.add('a');
//            }
//            pq.addAll(toAdd);
//        }
//        return schedule.size();
//    }
//
//    private boolean isPossibleToAdd(PriorityQueue<Node> pq, List<Character> schedule, int minLength) {
//        for (int i = schedule.size() - 1; i > schedule.size() - 1 - minLength; i--) {
//            if (schedule.get(i) == pq.peek().value) {
//                return false;
//            }
//        }
//        return true;
//    }
//
//    private static class Node {
//        public final Character value;
//        public final int count;
//
//        Node(Character value, int count) {
//            this.value = value;
//            this.count = count;
//        }
//
//        public Node minusCount() {
//            return new Node(value, count - 1);
//        }
//    }
}
