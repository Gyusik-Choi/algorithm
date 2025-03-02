import java.util.Arrays;

public class ArrayPartition561 {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int sums = 0;
        for (int i = 0; i < nums.length - 1; i += 2)sums += nums[i];
        return sums;
    }
}
