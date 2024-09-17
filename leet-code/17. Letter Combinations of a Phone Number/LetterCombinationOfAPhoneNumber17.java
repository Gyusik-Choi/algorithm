import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LetterCombinationOfAPhoneNumber17 {
    public List<String> letterCombinations(String digits) {
        Map<Integer, List<String>> map = initMap();
        if (digits.isEmpty()) return new ArrayList<>();
        return dfs(map, new ArrayList<>(), "", digits);
    }

    private Map<Integer, List<String>> initMap() {
        return new HashMap<>() {{
            put(2, List.of("a", "b", "c"));
            put(3, List.of("d", "e", "f"));
            put(4, List.of("g", "h", "i"));
            put(5, List.of("j", "k", "l"));
            put(6, List.of("m", "n", "o"));
            put(7, List.of("p", "q", "r", "s"));
            put(8, List.of("t", "u", "v"));
            put(9, List.of("w", "x", "y", "z"));
        }};
    }

    private List<String> dfs(Map<Integer, List<String>> map, List<String> combs, String comb, String digit) {
        if (digit.isEmpty()) {
            combs.add(comb);
            return combs;
        }

        for (String s : map.get(Integer.parseInt(String.valueOf(digit.charAt(0))))) {
            combs = dfs(map, combs, comb + s, digit.substring(1));
            // combs 에 대한 참조가 유지돼서 아래와 같이 작성해도 된다
            // dfs(map, combs, comb + s, digit.substring(1));
        }
        return combs;
    }

    // digits 에서 앞글자 한자씩 떼서 재귀 호출
    // ->
    // 각 글자는 map 에서 가진 값의 길이만큼 for 문을 돈다
    // 정답을 담는 리스트에 넣을 문자열에 해당 for 문의 요소를 더하고
    // digits 에서 앞글자 한자를 떼서 재귀 호출
    // 만약에 더 이상 글자가 없으면 문자열을 배열에 더한다
}
