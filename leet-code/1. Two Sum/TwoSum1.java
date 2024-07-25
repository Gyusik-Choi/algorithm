import java.util.Arrays;

public class TwoSum1 {
    public int[] twoSum(int[] nums, int target) {
        int[][] numsWithIdx = new int[nums.length][2];
        for (int i = 0; i < nums.length; i++) {
            numsWithIdx[i] = new int[]{nums[i], i};
        }
        Arrays.sort(numsWithIdx, (num1, num2) -> {
            if (num1[0] == num2[0]) {
                return num1[1] - num2[1];
            }
            return num1[0] - num2[0];
        });

        int left = 0;
        int right = numsWithIdx.length - 1;
        while (left < right) {
            int sums = numsWithIdx[left][0] + numsWithIdx[right][0];
            if (sums == target) {
                break;
            }

            if (sums > target) {
                right -= 1;
            } else {
                left += 1;
            }
        }

        return new int[]{numsWithIdx[left][1], numsWithIdx[right][1]};
    }
}
