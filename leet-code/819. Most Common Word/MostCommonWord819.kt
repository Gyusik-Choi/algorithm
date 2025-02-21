package com.example

class MostCommonWord819 {
    fun mostCommonWord(paragraph: String, banned: Array<String>): String {
        val words = paragraph
            .replace("[^a-zA-Z]+".toRegex(), " ")
            .lowercase()
//            .trim()
            .split(" ")
        println(paragraph
            .replace("[^a-zA-Z]+".toRegex(), " ")
            .lowercase())
        println(words)
        val map: MutableMap<String, Int> = mutableMapOf()
        for (word in words) {
            if (!banned.contains(word)) {
                map[word] = map.getOrDefault(word, 0) + 1
            }
        }
        return map.maxBy { it.value }.key
    }
}