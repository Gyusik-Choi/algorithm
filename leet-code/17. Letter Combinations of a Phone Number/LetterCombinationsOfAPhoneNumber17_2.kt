package com.example

class LetterCombinationsOfAPhoneNumber17_2 {
    private val map = hashMapOf(
        '2' to listOf('a', 'b', 'c'),
        '3' to listOf('d', 'e', 'f'),
        '4' to listOf('g', 'h', 'i'),
        '5' to listOf('j', 'k', 'l'),
        '6' to listOf('m', 'n', 'o'),
        '7' to listOf('p', 'q', 'r', 's'),
        '8' to listOf('t', 'u', 'v'),
        '9' to listOf('w', 'x', 'y', 'z'),
    )

    fun letterCombinations(digits: String): List<String> {
        val answer = mutableListOf<String>()
        recursion(digits, answer, StringBuilder())
        return answer
    }

    private fun recursion(digits: String, combinations: MutableList<String>, combination: StringBuilder) {
        if (digits.isEmpty()) {
            combinations.add(combination.toString())
            return
        }
        for (c in map[digits[0]]!!) {
            combination.append(c)
            recursion(digits.substring(1), combinations, combination)
            combination.deleteCharAt(combination.length - 1)
        }
    }
}
