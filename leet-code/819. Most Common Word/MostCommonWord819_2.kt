package com.example

class MostCommonWord819_2 {
    fun mostCommonWord(paragraph: String, banned: Array<String>): String {
        val p = paragraph
            .replace(Regex("[^a-zA-Z\\s]"), " ")
            .lowercase()
            .split(" ")
            .filter { it.isNotEmpty() && !banned.contains(it) }
        val count = p.groupingBy { it }.eachCount()
        return count.maxBy { it.value }.key
    }
}
