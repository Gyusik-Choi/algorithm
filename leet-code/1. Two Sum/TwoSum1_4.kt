class TwoSums1_4 {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val maps: MutableMap<Int, Int> = mutableMapOf()
        var first = -1
        var second = -1
        for ((i, num) in nums.withIndex()) {
            if (maps.containsKey(target - num)) {
                first = maps[target - num]!!
                second = i
                break
            }
            maps[num] = i
        }
        return intArrayOf(first, second)
    }
}