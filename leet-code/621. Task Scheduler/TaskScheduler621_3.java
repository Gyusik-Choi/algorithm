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
                node.minusCount();
                if (node.count > 0) {
                    pq.add(node);
                }
            } else {
                nodeList.add(node);
                if (!pq.isEmpty()) {
                    continue;
                }
                node = new Node('i', 1);
            }
            count += 1;
            list.add(node);
            window.put(node.character, window.getOrDefault(node.character, 0) + 1);
            clearNodeList(pq, nodeList);
            checkWindow(list, window, n);
        }
        return count;
    }

    private boolean canAdd(Map<Character, Integer> map, char c) {
        return !map.containsKey(c) || map.get(c) <= 0;
    }

    private void clearNodeList(PriorityQueue<Node> pq, List<Node> nodeList) {
        pq.addAll(nodeList);
        nodeList.clear();
    }

    private void checkWindow(List<Node> list, Map<Character, Integer> window, int n) {
        if (list.size() > n) {
            Node pop = list.removeFirst();
            window.put(pop.character, window.get(pop.character) - 1);
        }
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
//        Map<Character, Integer> map = new HashMap<>();
//        for (char t : tasks) {
//            map.put(t, map.getOrDefault(t, 0) + 1);
//        }
//        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
//            pq.add(new Node(entry.getKey(), entry.getValue()));
//        }
//        int count = 0;
//        Map<Character, Integer> window = new HashMap<>();
//        List<Node> list = new ArrayList<>();
//        List<Node> nodeList = new ArrayList<>();
//        while (!pq.isEmpty()) {
//            Node node = pq.poll();
//            if (canAdd(window, node.character)) {
//                count += 1;
//                node.minusCount();
//                if (node.count > 0) {
//                    pq.add(node);
//                }
//                list.add(node);
//                window.put(node.character, window.getOrDefault(node.character, 0) + 1);
//                pq.addAll(nodeList);
//                nodeList.clear();
//                if (list.size() > n) {
//                    Node pop = list.removeFirst();
//                    window.put(pop.character, window.get(pop.character) - 1);
//                }
//            } else {
//                nodeList.add(node);
//                if (pq.isEmpty()) {
//                    // idle
//                    count += 1;
//                    list.add(new Node('i', 1));
//                    window.put('i', window.getOrDefault('i', 0) + 1);
//                    if (list.size() > n) {
//                        Node pop = list.removeFirst();
//                        window.put(pop.character, window.get(pop.character) - 1);
//                    }
//                    pq.addAll(nodeList);
//                    nodeList.clear();
//                }
//            }
//        }
//        return count;
//    }
//
//    private boolean canAdd(Map<Character, Integer> map, char c) {
//        return !map.containsKey(c) || map.get(c) <= 0;
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
