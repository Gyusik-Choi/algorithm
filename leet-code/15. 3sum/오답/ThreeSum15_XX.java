import java.util.*;

public class ThreeSum15_XX {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> answer = new HashSet<>();

        int left = 0;
        int right = nums.length - 1;
        while (left < right - 1) {
            int sums = nums[left] + nums[right];
            int l = left;
            int r = right;
            while (l < r - 1) {
                if (sums < 0) {
                    l++;
                    if (sums + nums[l] == 0) {
                        answer.add(List.of(nums[left], nums[l], nums[right]));
                    }
                } else {
                    r--;
                    if (sums + nums[r] == 0) {
                        answer.add(List.of(nums[left], nums[r], nums[right]));
                    }
                }
            }

            if (sums < 0) {
                left++;
            } else {
                right--;
            }
        }
        System.out.println(answer.stream().toList());
        return answer.stream().toList();
    }
}
