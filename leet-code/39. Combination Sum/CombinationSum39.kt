class CombinationSum39_2 {
    fun combinationSum(candidates: IntArray, target: Int): List<List<Int>> {
        val combs: MutableList<List<Int>> = mutableListOf()
        val comb: MutableList<Int> = mutableListOf()

        fun dfs(idx: Int) {
            if (comb.sum() > target) {
                return
            }

            if (comb.sum() == target) {
                combs.add(ArrayList(comb))
                return
            }

            for (i in idx..<candidates.size) {
                comb.add(candidates[i])
                dfs(i)
                comb.removeLast()
            }
        }

        dfs(0)
        return combs
    }
}
