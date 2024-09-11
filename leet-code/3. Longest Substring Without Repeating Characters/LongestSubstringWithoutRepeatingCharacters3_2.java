import java.util.HashMap;
import java.util.Map;

public class LongestSubstringWithoutRepeatingCharacters3_2 {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int maxSubstringLength = 0;
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            // 해시맵에 문자가 존재하고 해시맵의 값이 left 범위 안에 있는 경우
            if (map.containsKey(c) && map.get(c) >= left) {
                left = map.get(c) + 1;
            } else {
                maxSubstringLength = Math.max(maxSubstringLength, right - left + 1);
            }
            map.put(c, right);
        }
        return maxSubstringLength;
    }
}
