import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class Programmers42576 {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> nameInfo = new HashMap<>();
        for (String p : participant) {
            nameInfo.put(p, nameInfo.getOrDefault(p, 0) + 1);
        }
        for (String c : completion) {
            if (nameInfo.containsKey(c)) {
                nameInfo.put(c, nameInfo.get(c) - 1);
            }
        }

        return nameInfo
                .keySet()
                .stream()
                .filter(k -> nameInfo.getOrDefault(k, 0) > 0)
                // .toList() 는 프로그래머스에서 통과되지 않는다
                // 자바 버전 문제로 보인다
                .collect(Collectors.toList())
                .get(0);
    }
}
