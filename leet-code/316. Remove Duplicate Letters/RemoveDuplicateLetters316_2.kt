package com.example

class RemoveDuplicateLetters316_2 {
    fun removeDuplicateLetters(s: String): String {
        val listSet = getSortedSetList(s)
        for (char in listSet) {
            val suffix = s.substring(s.indexOf(char))
            val suffixListSet = getSortedSetList(suffix)
            if (listSet == suffixListSet) {
                return char + removeDuplicateLetters(suffix.replace(char.toString(), ""))
            }
        }
        return ""
    }

    private fun getSortedSetList(s: String): List<Char> {
        val set = mutableSetOf<Char>()
        for (char in s) {
            set.add(char)
        }
        return set.sorted()
    }
}