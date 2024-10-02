import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.List;

public class CourseSchedule207_2 {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // 특정 정점을 기준으로 연결된 정점들 정보
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int[] prerequisite : prerequisites) {
            // 첫번째 인덱스를 완수하려면 두번째 인덱스 요소를 먼저 끝내야 해서
            // 두번째 인덱스를 key, 첫번째 인덱스를 value 로 넣는다
            map.putIfAbsent(prerequisite[1], new ArrayList<>());
            map.get(prerequisite[1]).add(prerequisite[0]);
        }
        // 순환 구조가 아닌 정점 정보를 모은다
        // 순환 구조가 아닌 정점은 true
        // true 인 정점은 연결된 정점들까지 모두 순환 구조가 아님을 보장한다
        boolean[] visit = new boolean[numCourses];
        // 순환 여부를 판단하는 리스트
        // 한 dfs 사이클에서 한 정점이 이미 리스트에 존재하면 순환 구조다
        // 예를 들어 0 -> 1 -> 2 -> 1 의 형태라면
        // 1은 0에서 1로 갈때 리스트에 포함되고 이후 2에서 1로 갈때 다시 리스트에 들어가려고 하므로
        // 이미 리스트에 있어서 순환 구조다
        List<Integer> seconds = new ArrayList<>();
        for (Integer first : map.keySet()) {
            if (!dfs(map, visit, seconds, first)) return false;
        }
        return true;
    }

    private boolean dfs(Map<Integer, List<Integer>> map, boolean[] visit, List<Integer> seconds, Integer first) {
        // 먼저 끝내야 할 정점이 여기 들어있으면 순환 구조
        if (seconds.contains(first)) return false;
        // 이미 순환 구조가 아님이 확인된 정점
        if (visit[first]) return true;
        if (!map.containsKey(first)) return true;
        // 순환 여부를 판단하는 리스트에 추가
        seconds.add(first);
        for (Integer second : map.get(first)) {
            if (!dfs(map, visit, seconds, second)) return false;
        }
        // dfs 재귀 호출이 끝나고 순환 여부가 아님이 확인 되어서 seconds 에서 제거한다
        // first 에 대한 중복 호출을 막기 위해 visit 에 추가한다
        seconds.remove(first);
        visit[first] = true;
        return true;
    }
}

// seconds 에 map 의 keySet 은
// 한번의 dfs 사이클 이후에 포함되면 안된다
// 포함되어 있으면 다음 dfs 사이클에서 keySet 을 조회할 때
// if (seconds.contains(first)) 조건에 의해 false 가 된다
// 대신 중복 dfs 호출을 막기 위해 visit 배열을 사용한다
// visit 에는 true 로 반환되는 dfs 사이클이 거쳐간 모든 정점들을 true 로 변환한다
// 해당 정점들의 경우 연결된 모든 정점들까지 순환 구조가 아님을 보장한다
