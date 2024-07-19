import java.util.regex.Pattern;

public class Solution {
    public boolean isPalindrome(String s) {
        String word = Pattern
                .compile("[^a-zA-Z0-9]")
                .matcher(s)
                .replaceAll("")
                .toLowerCase();

        String halfWord = word
                .substring(0, word.length() / 2);

        String reversedHalfWord = new StringBuilder(word)
                .reverse()
                .substring(0, word.length() / 2);

        return halfWord.equals(reversedHalfWord);
    }
}
