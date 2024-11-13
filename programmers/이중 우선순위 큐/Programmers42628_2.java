package com.example;

import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Queue;

public class Programmers42628_2 {
    public int[] solution(String[] operations) {
        Queue<Integer> maxQueue = new PriorityQueue<>(Collections.reverseOrder());
        Queue<Integer> minQueue = new PriorityQueue<>();

        for (String operation : operations) {
            String[] o = operation.split(" ");
            String command = o[0];
            int data = Integer.parseInt(o[1]);

            if (command.equals("I")) {
                maxQueue.add(data);
                minQueue.add(data);
            } else {
                if (data == 1) {
                    minQueue.remove(maxQueue.poll());
                } else {
                    maxQueue.remove(minQueue.poll());
                }
            }
        }

        return minQueue.isEmpty() || maxQueue.isEmpty()
                ? new int[]{0, 0}
                : new int[]{maxQueue.peek(), minQueue.peek()};
    }
}
