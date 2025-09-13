package com.example

class RemoveDuplicateLetters316_3 {
    fun removeDuplicateLetters(s: String): String {
        val list = toSortedSetList(s)
        for (c in list) {
            val suffix = s.substring(s.indexOf(c))
            if (list == toSortedSetList(suffix)) {
                return c + removeDuplicateLetters(suffix.replace(c.toString(), ""))
            }
        }
        return ""
    }

    private fun toSortedSetList(s: String): List<Char> {
        val set = mutableSetOf<Char>()
        set.addAll(s.toCharArray().toList())
        return set.sorted()
    }
}
