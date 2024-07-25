import java.util.Arrays;
import java.util.HashMap;

public class TwoSum1_2 {
    public int[] twoSum(int[] nums, int target) {
        // 숫자, 인덱스
        HashMap<Integer, Integer> maps = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            maps.put(nums[i], i);
        }
        int first = -1;
        int second = -1;
        for (int i = 0; i < nums.length; i++) {
            // 키 확인 && 값 확인
            if (maps.containsKey(target - nums[i]) && i != maps.get(target - nums[i])) {
                first = i;
                second = maps.get(target - nums[i]);
                break;
            }
        }
        return new int[]{first, second};
    }
}
