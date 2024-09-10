import java.util.HashMap;

public class JewelsAndStones771 {
    public int numJewelsInStones(String jewels, String stones) {
        HashMap<Character, Boolean> map = new HashMap<>();
        for (char j : jewels.toCharArray()) {
            map.put(j, true);
        }
        int answer = 0;
        for (char c : stones.toCharArray()) {
            if (map.containsKey(c)) {
                answer += 1;
            }
        }
        return answer;
    }
}
