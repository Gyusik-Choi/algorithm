class GroupAnagrams49_2 {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val maps: MutableMap<String, MutableList<String>> = mutableMapOf()
        for (str in strs) {
            val sortedStr = str.toCharArray().sorted().joinToString("")
            maps.getOrPut(sortedStr) { mutableListOf() }
            maps[sortedStr]!!.add(str)
        }
        return ArrayList(maps.values)
    }
}

// 참고
// https://www.baeldung.com/kotlin/arraylist-vs-mutablelistof
