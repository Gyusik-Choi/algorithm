import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class MostCommonWord819_2 {
    public String mostCommonWord(String paragraph, String[] banned) {
        String[] words = paragraph
                .replaceAll("[\\s!?',;.]+", " ")
                .toLowerCase()
                .split(" ");

        HashMap<String, Integer> maps = new HashMap<>();
        for (String word : words) {
            if (Arrays.asList(banned).contains(word)) {
                continue;
            }
            if (maps.containsKey(word)) {
                maps.put(word,  maps.get(word) + 1);
            } else {
                maps.put(word, 1);
            }
        }

        return Collections
                .max(maps.entrySet(), Map.Entry.comparingByValue())
                .getKey();
    }
}
