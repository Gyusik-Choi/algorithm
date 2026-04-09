package com.example

class Permutations46_2 {
    fun permute(nums: IntArray): List<List<Int>> {
        return recursion(nums, BooleanArray(nums.size), mutableListOf(), mutableListOf())
    }

    private fun recursion(
        nums: IntArray,
        used: BooleanArray,
        perms: MutableList<List<Int>>,
        perm: MutableList<Int>
    ): List<List<Int>> {
        if (nums.size == perm.size) {
            perms.add(perm.toList())
            return perms
        }
        for (i in nums.indices) {
            if (used[i]) {
                continue
            }
            perm.add(nums[i])
            used[i] = true
            recursion(nums, used, perms, perm)
            perm.removeLast()
            used[i] = false
        }
        return perms
    }
}
