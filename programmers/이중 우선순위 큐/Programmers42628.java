import java.util.*;

public class Programmers42628 {
    public int[] solution(String[] operations) {
        Queue<Integer> maxQueue = new PriorityQueue<>(Collections.reverseOrder());
        Queue<Integer> minQueue = new PriorityQueue<>();
        Map<Integer, Integer> map = new HashMap<>();

        for (String operation : operations) {
            String[] o = operation.split(" ");
            String command = o[0];
            int data = Integer.parseInt(o[1]);

            // Insert
            if (command.equals("I")) {
                map.put(data, map.getOrDefault(data, 0) + 1);
                maxQueue.add(data);
                minQueue.add(data);
                continue;
            }

            // Delete Max
            if (command.equals("D") && data > 0) {
                while (isInvalidQueue(maxQueue, map)) {
                    maxQueue.poll();
                }

                if (!maxQueue.isEmpty()) {
                    Integer maxValue = maxQueue.poll();
                    map.put(maxValue, map.getOrDefault(maxValue, 0) - 1);
                }
                continue;
            }

            // Delete Min
            while (isInvalidQueue(minQueue, map)) {
                minQueue.poll();
            }

            if (!minQueue.isEmpty()) {
                Integer minValue = minQueue.poll();
                map.put(minValue, map.getOrDefault(minValue, 0) - 1);
            }
        }

        // 제거되지 못한 요소들 제거
        while (isInvalidQueue(maxQueue, map)) {
            maxQueue.poll();
        }

        while (isInvalidQueue(minQueue, map)) {
            minQueue.poll();
        }

        return maxQueue.isEmpty() || minQueue.isEmpty()
                ? new int[]{0, 0}
                : new int[]{maxQueue.peek(), minQueue.peek()};
    }

    private boolean isInvalidQueue(Queue<Integer> maxQueue, Map<Integer, Integer> map) {
        return !maxQueue.isEmpty() && map.get(maxQueue.peek()) == 0;
    }
}
