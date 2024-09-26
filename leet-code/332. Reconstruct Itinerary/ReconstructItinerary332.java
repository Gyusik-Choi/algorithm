import java.util.*;

public class ReconstructItinerary332 {
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, PriorityQueue<String>> map = new HashMap<>();
        for (List<String> ticket : tickets) {
            map.putIfAbsent(ticket.get(0), new PriorityQueue<>());
            map.get(ticket.get(0)).add(ticket.get(1));
        }
        return dfs(map, new ArrayList<>(), "JFK");
    }

    private List<String> dfs(Map<String, PriorityQueue<String>> map,
                             List<String> itinerary,
                             String departure) {
        while (map.containsKey(departure) && !map.get(departure).isEmpty()) {
            String destination = map.get(departure).poll();
            dfs(map, itinerary, destination);
        }
        itinerary.add(0, departure);
        return itinerary;
    }
}

//[
// ["ANU","EZE"],
// ["EZE","AXA"],
// ["AXA","TIA"],
// ["TIA","ANU"],
// ["ANU","JFK"],
// ["JFK","ANU"],
// ["TIA","ANU"],
// ["TIA","JFK"],
// ["ANU","TIA"],
// ["JFK","TIA"],
//]
