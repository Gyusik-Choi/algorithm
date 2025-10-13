package com.example;

import java.util.*;

public class CourseSchedule207_4 {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        Arrays.stream(prerequisites).forEach(prerequisite -> {
            map.putIfAbsent(prerequisite[1], new ArrayList<>());
            map.get(prerequisite[1]).add(prerequisite[0]);
        });
        boolean[] toVisit = new boolean[numCourses];
        boolean[] visited = new boolean[numCourses];
        for (int start : map.keySet()) {
            if (!dfs(map, start, toVisit, visited)) {
                return false;
            }
        }
        return true;
    }

    private boolean dfs(Map<Integer, List<Integer>> map,
                        int departure,
                        boolean[] toVisit,
                        boolean[] visited) {
        if (toVisit[departure]) {
            return false;
        }

        if (visited[departure]) {
            return true;
        }

        if (map.containsKey(departure)) {
            toVisit[departure] = true;
            for (int destination : map.get(departure)) {
                if (!dfs(map, destination, toVisit, visited)) {
                    return false;
                }
            }
            toVisit[departure] = false;
            visited[departure] = true;
        }
        return true;
    }
}
