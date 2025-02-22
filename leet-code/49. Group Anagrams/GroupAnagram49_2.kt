package com.example.algorithm

class GroupAnagram49_2 {

    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val map: MutableMap<String, MutableList<String>> = mutableMapOf()
        for (str in strs) {
            val sortedStr = str.toCharArray().sorted().joinToString("")
            map.getOrPut(sortedStr) { mutableListOf() }.add(str)
        }
        return ArrayList(map.values)
    }
}
