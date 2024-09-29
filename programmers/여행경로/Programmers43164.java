import java.util.*;

public class Programmers43164 {
    public String[] solution(String[][] tickets) {
        Map<String, PriorityQueue<String>> map = new HashMap<>();
        for (String[] ticket : tickets) {
            PriorityQueue<String> dest = map.getOrDefault(ticket[0], new PriorityQueue<>());
            dest.add(ticket[1]);
            map.put(ticket[0], dest);
        }
        return dfs(map, new LinkedList<>(), "ICN");
    }

    private String[] dfs(Map<String, PriorityQueue<String>> map, List<String> visit, String start) {
        while (map.containsKey(start) && !map.get(start).isEmpty()) {
            dfs(map, visit, map.get(start).poll());
        }
        visit.add(0, start);
        return visit.toArray(new String[0]);
    }
}
