import java.util.HashSet;
import java.util.Set;

public class JewelsAndStones771_3 {
    public int numJewelsInStones(String jewels, String stones) {
        Set<Character> set = new HashSet<>();
        for (char j : jewels.toCharArray()) {
            set.add(j);
        }
        int cnt = 0;
        for (char s : stones.toCharArray()) {
            if (set.contains(s)) {
                cnt += 1;
            }
        }
        return cnt;
    }
}
