import java.util.Comparator;
import java.util.Set;
import java.util.TreeSet;

public class RemoveDuplicateLetters316_3 {
    public Set<Character> toSortedSet(String s) {
        Set<Character> set = new TreeSet<>(Comparator.comparingInt(o -> o));
        for (int i = 0; i < s.length(); i ++) {
            set.add(s.charAt(i));
        }
        return set;
    }

    public String removeDuplicateLetters(String s) {
        Set<Character> sortedSet = toSortedSet(s);
        // s 를 문자 단위로 정렬한 Set 이
        // 해당 문자가 포함된 위치부터 잘라낸 접미사와 동일하면
        // 해당 문자 앞의 문자는 필요없고
        // 해당 문자가 현재 s 에서 가장 앞에 나오는 문자라는 의미다
        //
        // bbcaac 를 오름차순으로 정렬해서 Set 으로 만들면
        // a, b, c 가 된다
        // a 의 suffix 가 aac 가 되고 정렬해서 Set 으로 만들면 a, c 라서
        // a, b, c 와 다르다
        // 그러나 b 의 suffix 가 bbcaac 가 되고 정렬해서 Set 으로 만들면 a, b, c 라서
        // a, b, c 와 동일하다
        // bbcaac 에서 가장 앞에 나오는 문자는 b 다
        for (char c : sortedSet) {
            String suffix = s.substring(s.indexOf(c));
            Set<Character> sortedSuffix = toSortedSet(suffix);
            if (sortedSet.equals(sortedSuffix)) {
                // suffix 에 남아있는 c 를 제거
                // 그리고 c 앞의 문자들은 자연스럽게 포함되지 않는다
                return c + removeDuplicateLetters(suffix.replace(String.valueOf(c), ""));
            }
        }
        return "";
    }
}

// bbcaac
