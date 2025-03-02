class ArrayPartition561_2 {
    fun arrayPairSum(nums: IntArray): Int {
        nums.sort();
        var sums = 0;
        for (i in nums.indices step 2) sums += nums[i];
        return sums;
    }
}
