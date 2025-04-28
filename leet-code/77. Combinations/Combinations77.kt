class Combinations77_3 {
    fun combine(n: Int, k: Int): List<List<Int>> {
        val combs: MutableList<List<Int>> = mutableListOf()
        val comb: MutableList<Int> = mutableListOf()

        fun dfs(start: Int) {
            if (comb.size == k) {
                combs.add(ArrayList(comb))
                return
            }

            for (s in start..n) {
                comb.add(s)
                dfs(s + 1)
                comb.removeLast()
            }
        }

        dfs(1)
        return combs
    }
}
