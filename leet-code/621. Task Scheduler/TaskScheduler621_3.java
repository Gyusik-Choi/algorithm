package com.example;

import java.util.*;

public class TaskScheduler621_3 {
    public int leastInterval(char[] tasks, int n) {
        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> b.count - a.count);
        Map<Character, Integer> map = new HashMap<>();
        for (char t : tasks) {
            map.put(t, map.getOrDefault(t, 0) + 1);
        }
        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
            pq.add(new Node(entry.getKey(), entry.getValue()));
        }
        int count = 0;
        Map<Character, Integer> window = new HashMap<>();
        List<Node> list = new ArrayList<>();
        List<Node> nodeList = new ArrayList<>();
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            if (canAdd(window, node.character)) {
                count += 1;
                node.minusCount();
                if (node.count > 0) {
                    pq.add(node);
                }
                list.add(node);
                window.put(node.character, window.getOrDefault(node.character, 0) + 1);
                pq.addAll(nodeList);
                nodeList.clear();
                if (list.size() > n) {
                    Node pop = list.removeFirst();
                    window.put(pop.character, window.get(pop.character) - 1);
                }
            } else {
                nodeList.add(node);
                if (pq.isEmpty()) {
                    // idle
                    count += 1;
                    list.add(new Node('i', 1));
                    window.put('i', window.getOrDefault('i', 0) + 1);
                    if (list.size() > n) {
                        Node pop = list.removeFirst();
                        window.put(pop.character, window.get(pop.character) - 1);
                    }
                    pq.addAll(nodeList);
                    nodeList.clear();
                }
            }
        }
        return count;
    }

    private boolean canAdd(Map<Character, Integer> map, char c) {
        return !map.containsKey(c) || map.get(c) <= 0;
    }

    static class Node {
        final char character;
        int count;

        Node(char character, int count) {
            this.character = character;
            this.count = count;
        }

        void minusCount() {
            count -= 1;
        }
    }
}

//package com.example;
//
//import java.util.*;
//
//public class TaskScheduler621_3 {
//    public int leastInterval(char[] tasks, int n) {
//        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> b.count - a.count);
//        HashMap<Character, Integer> map = new HashMap<>();
//        for (char t : tasks) {
//            map.put(t, map.getOrDefault(t, 0) + 1);
//        }
//        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
//            pq.add(new Node(entry.getKey(), entry.getValue()));
//        }
//        List<Character> answer = new ArrayList<>();
//        List<Node> nodeList = new ArrayList<>();
//        while (!pq.isEmpty()) {
//            Node node = pq.poll();
//            if (canAdd(answer, node.character, Math.max(answer.size() - n, 0), answer.size() - 1)) {
//                answer.add(node.character);
//                node.minusCount();
//                if (node.count > 0) {
//                    pq.add(node);
//                }
//                pq.addAll(nodeList);
//                nodeList.clear();
//            } else {
//                nodeList.add(node);
//                if (pq.isEmpty()) {
//                    answer.add('i');
//                    pq.addAll(nodeList);
//                    nodeList.clear();
//                }
//            }
//        }
//        return answer.size();
//    }
//
//    private boolean canAdd(List<Character> list, char ch, int start, int end) {
//        for (int i = start; i <= end; i++) {
//            if (list.get(i).equals(ch)) {
//                return false;
//            }
//        }
//        return true;
//    }
//
//    static class Node {
//        final char character;
//        int count;
//
//        Node(char character, int count) {
//            this.character = character;
//            this.count = count;
//        }
//
//        void minusCount() {
//            count -= 1;
//        }
//    }
//}
