class Permutations46_2 {
    fun permute(nums: IntArray): List<List<Int>> {
        val perms: MutableList<List<Int>> = mutableListOf()
        val perm: MutableList<Int> = mutableListOf()

        fun dfs(): List<List<Int>> {
            if (perm.size == nums.size) {
                perms.add(ArrayList(perm))
                return perms.toList()
            }

            for (i in nums.indices) {
                if (perm.contains(nums[i])) continue

                perm.add(nums[i])
                dfs()
                perm.removeLast()
            }
            return perms.toList()
        }

        return dfs()
    }
}
