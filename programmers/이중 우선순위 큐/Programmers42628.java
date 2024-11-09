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

            if (command.equals("I")) {
                map.put(data, map.getOrDefault(data, 0) + 1);
                maxQueue.add(data);
                minQueue.add(data);
                continue;
            }

            if (command.equals("D") && data > 0) {
                while (!maxQueue.isEmpty() && map.get(maxQueue.peek()) == 0) {
                    maxQueue.poll();
                }
                if (!maxQueue.isEmpty()) {
                    Integer maxValue = maxQueue.poll();
                    map.put(maxValue, map.getOrDefault(maxValue, 0) - 1);
                }
                continue;
            }

            while (!minQueue.isEmpty() && map.get(minQueue.peek()) == 0) {
                minQueue.poll();
            }

            if (!minQueue.isEmpty()) {
                Integer minValue = minQueue.poll();
                map.put(minValue, map.getOrDefault(minValue, 0) - 1);
            }
        }

        while (!maxQueue.isEmpty() && map.get(maxQueue.peek()) == 0) {
            maxQueue.poll();
        }

        while (!minQueue.isEmpty() && map.get(minQueue.peek()) == 0) {
            minQueue.poll();
        }

        if (maxQueue.isEmpty() || minQueue.isEmpty()) {
            return new int[]{0, 0};
        }

        return new int[]{maxQueue.peek(), minQueue.peek()};
    }
}
