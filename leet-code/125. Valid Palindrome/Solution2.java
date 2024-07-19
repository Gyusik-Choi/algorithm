public class Solution2 {
    public boolean isPalindrome(String s) {
        String word = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        String reversedWord = new StringBuilder(word).reverse().toString().toLowerCase();
        return word.equals(reversedWord);
    }
}
