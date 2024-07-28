import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class ThreeSum15_2 {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> answer = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i - 1] == nums[i]) {
                continue;
            }

            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int sums = nums[i] + nums[left] + nums[right];

                if (sums < 0) {
                    left++;
                } else if (sums > 0) {
                    right--;
                } else {
                    answer.add(List.of(nums[i], nums[left], nums[right]));

                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }

                    while (left < right && nums[right - 1] == nums[right]) {
                        right--;
                    }

                    left++;
                    right--;
                }
            }
        }

        return answer;
    }
}
