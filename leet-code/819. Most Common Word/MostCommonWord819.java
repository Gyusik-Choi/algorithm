import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class MostCommonWord819 {
    public String mostCommonWord(String paragraph, String[] banned) {
        System.out.println(paragraph.replaceAll("[!?',;.]+", " "));
//         공백을 잘 제거하기 위해
//         regex 에 \\s 도 추가한다
//
//         b,b,b,b 처럼 공백 없이 이어진 문자열이 주어질 수 있다
//         이때 공백도 잘 제거하기 위해
//         replacement 문자열을 빈 문자열 ""가 아닌 공백인 " "를 설정한다
//
//         위의 설정들을 통해
//         "b , b" 이런 문자열이 주어졌을 때
//         ["b", "b"] 로 만들 수 있다
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

        String answer = "";
        int maxCnt = 0;
        for (Map.Entry<String, Integer> entry : maps.entrySet()) {
            if (maxCnt < entry.getValue()) {
                answer = entry.getKey();
                maxCnt = entry.getValue();
            }
        }
        return answer;
    }
}
