import java.util.*;

public class TopKFrequentElements347_2 {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o2[1] - o1[1]);
        for (Integer i : map.keySet()) {
            pq.add(new int[]{i, map.get(i)});
        }
        int[] answer = new int[k];
        for (int i = 0; i < k; i++) {
            answer[i] = Objects.requireNonNull(pq.poll())[0];
        }
        return answer;
    }
}
