import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class TopKFrequentElements347_3 {
    public int[] topKFrequent(int[] nums, int k) {
        // 숫자별 갯수를 센다
        Map<Integer, Integer> elements = new HashMap<>();
        for (int num : nums) {
            elements.put(num, elements.getOrDefault(num, 0) + 1);
        }

        // 갯수별 숫자를 구한다
        // 갯수가 동일한 숫자가 있을 수 있어서 숫자는 리스트로 구한다
        // nums 를 for 문을 돌면서
        // elements 에서 nums 의 값을 가져온다
        // frequencyInfo 에 값이 있으면 ArrayList 에 nums 의 요소를 추가한다
        // frequencyInfo 에 값이 없으면 빈 ArrayList 를 추가한다
        Map<Integer, ArrayList<Integer>> frequencyInfo = new HashMap<>();
        for (int num : elements.keySet()) {
            int frequency = elements.get(num);
            ArrayList<Integer> elementList = frequencyInfo.getOrDefault(frequency, new ArrayList<>());
            elementList.add(num);
            frequencyInfo.put(frequency, elementList);
        }

        // nlogn 이 소요되는 정렬을 하지 않고
        // n 으로 수행할 수 있도록 k 의 최대값을 기준으로 for 문 탐색한다
        // 정답을 이미 구했을 수 있어서 정답을 구하는 배열의 인덱스 정보를 갖는 idx 가 k 미만 조건을 추가한다
        int[] answer = new int[k];
        int idx = 0;
        for (int frequency = nums.length; frequency > 0 && idx < k; frequency -= 1) {
            if (frequencyInfo.containsKey(frequency)) {
                for (int element : frequencyInfo.get(frequency)) {
                    answer[idx] = element;
                    idx += 1;
                }
            }
        }
        return answer;
    }
}
