package com.example.algorithm;

import java.util.*;

public class CourseSchedule207_3 {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        int[] inDegree = new int[numCourses];
        Arrays.stream(prerequisites).forEach(prerequisite -> {
            map.putIfAbsent(prerequisite[1], new ArrayList<>());
            map.get(prerequisite[1]).add(prerequisite[0]);
            inDegree[prerequisite[0]] += 1;
        });

        Deque<Integer> deq = new ArrayDeque<>(getStartPoints(inDegree));
        while (!deq.isEmpty()) {
            Integer start = deq.poll();
            if (!map.containsKey(start)) {
                continue;
            }
            map.get(start).forEach(end -> {
                inDegree[end] -= 1;
                if (inDegree[end] == 0) {
                    deq.add(end);
                }
            });
        }
        return !isCycle(inDegree);
    }

    private List<Integer> getStartPoints(int[] indegree) {
        List<Integer> startPoints = new ArrayList<>();
        for (int i = 0; i < indegree.length; i++) {
            if (indegree[i] == 0) {
                startPoints.add(i);
            }
        }
        return startPoints;
    }

    private boolean isCycle(int[] indegree) {
        return Arrays.stream(indegree)
                .filter(num -> num > 0)
                .findAny()
                .isPresent();
    }
}
