class ValidPalindrome125 {
    fun isPalindrome(s: String): Boolean {
        val word: String = s.replace("[^a-zA-Z0-9]".toRegex(), "").lowercase()
        val reversedWord: String = StringBuilder(word).reversed().toString()
        return word == reversedWord
    }
}
