import java.util.*;

public class CourseSchedule207 {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] level = new int[numCourses];
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int[] prerequisite : prerequisites) {
            level[prerequisite[0]] += 1;
            List<Integer> value = map.getOrDefault(prerequisite[1], new ArrayList<>());
            value.add(prerequisite[0]);
            map.put(prerequisite[1], value);
        }

        Deque<Integer> deq = new ArrayDeque<>();
        for (int i = 0; i < level.length; i++) {
            if (level[i] == 0) {
                deq.add(i);
            }
        }

        if (deq.isEmpty()) {
            return false;
        }

        return bfs(map, deq, level);
    }

    private boolean bfs(Map<Integer, List<Integer>> map, Deque<Integer> deq, int[] level) {
        while (!deq.isEmpty()) {
            Integer start = deq.pollFirst();
            if (!map.containsKey(start)) {
                continue;
            }

            for (Integer end : map.get(start)) {
                level[end] -= 1;
                if (level[end] == 0) {
                    deq.add(end);
                }
            }
        }

        return !isCycle(level);
    }

    private boolean isCycle(int[] level) {
        for (int i : level) {
            if (i > 0) {
                return true;
            }
        }
        return false;
    }
}
