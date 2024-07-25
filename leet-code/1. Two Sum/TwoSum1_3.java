import java.util.HashMap;

public class TwoSum1_3 {
    public int[] twoSum(int[] nums, int target) {
        // 숫자, 인덱스
        HashMap<Integer, Integer> maps = new HashMap<>();
        int first = -1;
        int second = -1;
        for (int i = 0; i < nums.length; i++) {
            // 키 확인 && 값 확인
            // 자신은 아직 maps 에 없는 상태에서 상대를 maps 에서 조회하므로
            // 인덱스가 자신인지 확인할 필요가 없다
            if (maps.containsKey(target - nums[i])) {
                first = maps.get(target - nums[i]);
                second = i;
                break;
            }
            // if 문을 만족하지 않으면 HashMap 에 키, 값 넣음
            maps.put(nums[i], i);
        }
        return new int[]{first, second};
    }
}
