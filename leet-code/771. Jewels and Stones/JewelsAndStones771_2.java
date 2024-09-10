import java.util.HashMap;

public class JewelsAndStones771_2 {
    public int numJewelsInStones(String jewels, String stones) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (char s : stones.toCharArray()) {
            if (map.containsKey(s)) {
                map.put(s, map.get(s) + 1);
            } else {
                map.put(s, 1);
            }
        }

        int answer = 0;
        for (char j : jewels.toCharArray()) {
            if (map.containsKey(j)) {
                answer += map.get(j);
            }
        }
        return answer;
    }
}
