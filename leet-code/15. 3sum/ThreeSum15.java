import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class ThreeSum15 {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> answer = new HashSet<>();

        for (int i = 0; i < nums.length - 2; i++) {
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
                    left++;
                    right--;
                }
            }
        }

        System.out.println(answer.stream().toList());
        return answer
                .stream()
                .toList();
    }
}
