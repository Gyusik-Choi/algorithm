class JewelsAndStones771_4 {
    fun numJewelsInStones(jewels: String, stones: String): Int {
        val set: MutableSet<Char> = HashSet()
        for (j in jewels) {
            set.add(j)
        }
        var cnt: Int = 0;
        for (s in stones) {
            if (set.contains(s)) {
                cnt += 1
            }
        }
        return cnt
    }
}