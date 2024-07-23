import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class GroupAnagrams49 {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> maps = new HashMap<>();
        for (String str : strs) {
            char[] strArray = str.toCharArray();
            Arrays.sort(strArray);
            String sortedStr = String.valueOf(strArray);

            if (!maps.containsKey(sortedStr)) {
                maps.put(sortedStr, new ArrayList<>());
            }
            maps.get(sortedStr).add(str);
        }
        return new ArrayList<>(maps.values());
    }
}
