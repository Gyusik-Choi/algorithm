class LetterCombinationOfAPhoneNumber17_2 {
    fun letterCombinations(digits: String): List<String> {
        val map = initMap()
        if (digits.isEmpty()) return mutableListOf()
        return dfsRecursive(map, mutableListOf(), "", digits)
    }

    private fun initMap(): Map<String, Array<String>> {
        return mapOf(
            "0" to arrayOf(),
            "1" to arrayOf(),
            "2" to arrayOf("a", "b", "c"),
            "3" to arrayOf("d", "e", "f"),
            "4" to arrayOf("g", "h", "i"),
            "5" to arrayOf("j", "k", "l"),
            "6" to arrayOf("m", "n", "o"),
            "7" to arrayOf("p", "q", "r", "s"),
            "8" to arrayOf("t", "u", "v"),
            "9" to arrayOf("w", "x", "y", "z")
        )
    }
    
    private fun dfsRecursive(map: Map<String, Array<String>>, combs: MutableList<String>, comb: String, digit: String): List<String> {
        if (digit.isEmpty()) {
            combs.add(comb)
            return combs
        }

        for (s in map[digit[0].toString()]!!) {
            dfsRecursive(map, combs, comb + s, digit.substring(1))
        }
        return combs
    }
}
