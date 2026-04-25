package com.example;

import java.util.*;

public class CourseSchedule207_5 {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // 순환의 조건 ->
        // 1. 처음부터 출발할 곳이 없음
        // 2. 다 안 돌았는데 나중에 출발할 곳이 없음
        // 결국, 실제로는 완료를 안했는데 출발할 곳이 없으면 순환이다
        // 완료 판단 방법 -> 더 이상 출발할 곳이 없으면 완료
        // 출발 판단 방법 -> level 이 0 (여러개일 수 있고, 큐에 넣어서 BFS 탐색)
        Map<Integer, List<Integer>> priority = new HashMap<>();
        int[] levels = new int[numCourses];
        Queue<Integer> queue = new LinkedList<>();
        for (int[] prerequisite : prerequisites) {
            priority.putIfAbsent(prerequisite[0], new ArrayList<>());
            priority.get(prerequisite[0]).add(prerequisite[1]);
            levels[prerequisite[1]] += 1;
        }
        for (int i = 0; i < numCourses; i++) {
            if (levels[i] == 0) {
                queue.add(i);
            }
        }
        while (!queue.isEmpty()) {
            Integer start = queue.poll();
            if (!priority.containsKey(start)) {
                continue;
            }
            for (Integer end : priority.get(start)) {
                levels[end] -= 1;
                if (levels[end] == 0) {
                    queue.add(end);
                }
            }
        }
        for (int i = 0; i < numCourses; i++) {
            if (levels[i] > 0) {
                return false;
            }
        }
        return true;
        // There are a total of numCourses courses you have to take,
        // labeled from 0 to numCourses - 1.
        // You are given an array prerequisites where prerequisites[i] = [ai, bi]
        // indicates that you must take course bi first if you want to take course ai.
        //
        // For example,
        // the pair [0, 1], indicates that to take course 0 you have to first take course 1.
        // Return true if you can finish all courses. Otherwise, return false.
        //
        // Example 1:
        // Input: numCourses = 2, prerequisites = [[1,0]]
        // Output: true
        // Explanation: There are a total of 2 courses to take.
        // To take course 1 you should have finished course 0. So it is possible.
        //
        // Example 2:
        // Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
        // Output: false
        // Explanation: There are a total of 2 courses to take.
        // To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
        //
        // Constraints:
        // 1 <= numCourses <= 2000
        // 0 <= prerequisites.length <= 5000
        // prerequisites[i].length == 2
        // 0 <= ai, bi < numCourses
        // All the pairs prerequisites[i] are unique.
    }
}
