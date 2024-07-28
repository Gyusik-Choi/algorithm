import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum15_X {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();
        Arrays.sort(nums);
        int left = 0;
        int right = nums.length - 1;
        int sums = nums[left] + nums[right];

        while (left < right - 1) {
            ArrayList<Integer> temp = new ArrayList<>();
            temp.add(nums[left]);
            temp.add(nums[right]);

            if (sums >= 0) {
                left += 1;
                if (sums + nums[left] == 0) {
                    temp.add(nums[left]);
                    answer.add(temp);
                }
            } else {
                right -= 1;
                if (sums + nums[right] == 0) {
                    temp.add(nums[right]);
                    answer.add(temp);
                }
            }
        }
        System.out.println(answer);
        return answer;
    }
}
