import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        HashMap<Integer, Integer> users = new HashMap<Integer, Integer>();

        for (int stage: stages) {
            if (users.containsKey(stage)) {
                Integer cnt = users.get(stage);
                users.put(stage, cnt + 1);
            } else {
                users.put(stage, 1);
            }
        }

        HashMap<Integer, Double> failRate = new HashMap<Integer, Double>();;
        int total = stages.length;

        for (int i = 1; i <= N; i++) {
            int userCnt = 0;

            if (users.containsKey(i)) {
                userCnt = users.get(i);
            }

            // 0 으로 나누지 않도록 예외 처리
            if (total == 0) {
                failRate.put(i, 0.0);
            } else {
                failRate.put(i, (double) userCnt / total);
            }

            total -= userCnt;
        }

        ArrayList<Integer> stageList = new ArrayList<>(failRate.keySet());
        // Collections.sort(stageList);
        // stageList 를 stage 번호 순서로 오름차순 정렬하지 않아도 오답이 발생하지 않는다
        // keySet 메소드는 map 의 키 순서를 보장하지 않는데
        // 어떻게 실패율이 같을 때 stage 번호 순서대로 정렬이 잘 됐는지 아직 이해하지 못했다
        stageList.sort((s1, s2) -> Double.compare(failRate.get(s2), failRate.get(s1)));
        return stageList.stream().mapToInt(Integer::intValue).toArray();
    }
}

// 참고
// https://bada744.tistory.com/54
// https://codechacha.com/ko/java-sort-map/
// https://velog.io/@jwkim/java-arraylist-array-type-conversion
// https://school.programmers.co.kr/questions/50861
// https://recordsoflife.tistory.com/1263
// https://stackoverflow.com/questions/43871017/are-the-hashmap-entries-always-sorted-by-key-if-the-key-is-of-type-integer
