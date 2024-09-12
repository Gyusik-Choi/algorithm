import java.util.*;

public class TopKFrequentElements347 {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        List<Integer> keys = new ArrayList<>(map.keySet());
        // https://velog.io/@dev-easy/Java-Map%EC%9D%84-Key-Value%EB%A1%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0
        // value 를 기준으로 내림차순 정렬
        keys.sort(((o1, o2) -> map.get(o2) - map.get(o1)));
        int[] answer = new int[k];
        for (int i = 0; i < k; i++) {
            answer[i] = keys.get(i);
        }
        return answer;
    }
}
