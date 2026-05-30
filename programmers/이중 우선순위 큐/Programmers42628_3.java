package com.example;

import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class Programmers42628_3 {
    // 제거하기 전에 최대힙 혹은 최소힙의 peek 의 값이 map 에 존재하는지 확인한다
    // 만약에 map 에 해당 key 값이 0이면 다른 힙에서 이미 제거된 상태다
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> minPQ = new PriorityQueue<>();
        PriorityQueue<Integer> maxPQ = new PriorityQueue<>(Comparator.reverseOrder());
        Map<Integer, Integer> map = new HashMap<>();
        for (String o : operations) {
            String[] operation = o.split(" ");
            String action = operation[0];
            int num = Integer.parseInt(operation[1]);
            if (action.equals("I")) {
                minPQ.add(num);
                maxPQ.add(num);
                map.put(num, map.getOrDefault(num, 0) + 1);
            } else {
                if (num == 1) {
                    removeInvalidNumFromPQ(maxPQ, map);
                    removeAndMinusNum(maxPQ, map);
                } else {
                    removeInvalidNumFromPQ(minPQ, map);
                    removeAndMinusNum(minPQ, map);
                }
            }
        }
        removeInvalidNumFromPQ(maxPQ, map);
        removeInvalidNumFromPQ(minPQ, map);
        return minPQ.isEmpty() || maxPQ.isEmpty()
                ? new int[]{0, 0}
                : new int[]{maxPQ.peek(), minPQ.peek()};
    }

    // 다른 PriorityQueue 에서 제거된 숫자를 해당 PriorityQueue 에서도 제거
    private void removeInvalidNumFromPQ(PriorityQueue<Integer> pq, Map<Integer, Integer> map) {
        while (!pq.isEmpty() && map.containsKey(pq.peek()) && map.get(pq.peek()) == 0) {
            pq.poll();
        }
    }

    // 유효한 숫자인 경우 PriorityQueue 에서 제거하고 Map 에서 값을 1 뺀다
    private void removeAndMinusNum(PriorityQueue<Integer> pq, Map<Integer, Integer> map) {
        if (!pq.isEmpty() && map.containsKey(pq.peek()) && map.get(pq.peek()) > 0) {
            Integer maxNum = pq.poll();
            map.put(maxNum, map.get(maxNum) - 1);
        }
    }

//    아래의 코드를 위의 코드로 리팩토링 했다
//    public int[] solution(String[] operations) {
//        PriorityQueue<Integer> minPQ = new PriorityQueue<>();
//        PriorityQueue<Integer> maxPQ = new PriorityQueue<>(Comparator.reverseOrder());
//        Map<Integer, Integer> map = new HashMap<>();
//        for (String o : operations) {
//            String[] operation = o.split(" ");
//            String action = operation[0];
//            int num = Integer.parseInt(operation[1]);
//            if (action.equals("I")) {
//                minPQ.add(num);
//                maxPQ.add(num);
//                map.put(num, map.getOrDefault(num, 0) + 1);
//            } else {
//                if (num == -1) {
//                    while (!minPQ.isEmpty() && map.containsKey(minPQ.peek()) && map.get(minPQ.peek()) == 0) {
//                        minPQ.poll();
//                    }
//                    if (!minPQ.isEmpty() && map.containsKey(minPQ.peek()) && map.get(minPQ.peek()) > 0) {
//                        Integer minNum = minPQ.poll();
//                        map.put(minNum, map.get(minNum) - 1);
//                    }
//                } else {
//                    while (!maxPQ.isEmpty() && map.containsKey(maxPQ.peek()) && map.get(maxPQ.peek()) == 0) {
//                        maxPQ.poll();
//                    }
//                    if (!maxPQ.isEmpty() && map.containsKey(maxPQ.peek()) && map.get(maxPQ.peek()) > 0) {
//                        Integer maxNum = maxPQ.poll();
//                        map.put(maxNum, map.get(maxNum) - 1);
//                    }
//                }
//            }
//        }
//        while (!maxPQ.isEmpty() && map.containsKey(maxPQ.peek()) && map.get(maxPQ.peek()) == 0) {
//            maxPQ.poll();
//        }
//        while (!minPQ.isEmpty() && map.containsKey(minPQ.peek()) && map.get(minPQ.peek()) == 0) {
//            minPQ.poll();
//        }
//        if (minPQ.isEmpty() || maxPQ.isEmpty()) {
//            return new int[]{0, 0};
//        }
//        return new int[]{maxPQ.peek(), minPQ.peek()};
//    }
}
