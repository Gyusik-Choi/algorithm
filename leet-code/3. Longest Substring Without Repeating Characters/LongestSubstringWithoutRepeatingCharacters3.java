import java.util.HashMap;
import java.util.Map;

public class LongestSubstringWithoutRepeatingCharacters3 {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        // 가장 긴 길이를 구하는 변수
        int maxSubstringLength = 0;
        // 현재 상황에서 가장 긴 길이를 구하는 변수
        int temp = 0;
        // 왼쪽 기준점
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            // 해당 문자가 해시맵에 존재하는 경우
            if (map.containsKey(c)) {
                // 해시맵에서 꺼낸 문자가 왼쪽 기준점 보다 왼쪽에 위치하는 경우는
                // left 를 기준으로 비교할 수 있도록 한다
                // 예를 들어, abba 가 나왔을 때 마지막 a 의 경우
                // 앞선 a 에 의해 a 가 해시맵에 존재하지만
                // 실제로 길이에 포함해야할 범위는 두번째 b 부터다
                // LongestSubstringWithoutRepeatingCharacters3_2 에서는
                // 해시맵에서 꺼낸 문자가 왼쪽 기준점 보다 왼쪽에 위치하는지 여부를 조건에 포함한다
                left = Math.max(map.get(c), left);
                // 기존의 최대 길이, 현재 상황에서 최대 길이, rigth - left 중 최대값을 구한다
                maxSubstringLength = Math.max(maxSubstringLength, Math.max(temp, right - left));
                // temp 를 현재 상황에서 가장 긴 길이를 갖도록 갱신
                temp = right - left;
            } else {
                temp += 1;
            }
            map.put(c, right);
        }
        maxSubstringLength = Math.max(maxSubstringLength, temp);
        return maxSubstringLength;
    }
}
