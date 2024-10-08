import java.util.PriorityQueue
import java.util.Queue

class CheapestFlightsWithinKStops787_2 {
    fun findCheapestPrice(n: Int, flights: Array<IntArray>, src: Int, dst: Int, k: Int): Int {
        val map: MutableMap<Int, MutableList<IntArray>> = mutableMapOf()
        for (flight in flights) {
            map.putIfAbsent(flight[0], mutableListOf())
            map[flight[0]]!!.add(intArrayOf(flight[1], flight[2]))
        }
        return dijkstra(map, src, dst, k)
    }

    private fun dijkstra(map: MutableMap<Int, MutableList<IntArray>>, src: Int, dst: Int, k: Int): Int {
        val pq: Queue<Flight> = PriorityQueue()
        val visit: MutableMap<Int, Int> = mutableMapOf()
        pq.add(Flight(src, 0, 0))

        while (!pq.isEmpty()) {
            val start = pq.poll()
            if (start.source == dst) return start.cost
            if (start.stop > k) continue
            if (!map.containsKey(start.source)) continue
            visit[start.source] = start.stop

            for (end in map[start.source]!!) {
                if (visit.containsKey(end[0]) && visit[end[0]]!! < start.stop + 1) continue
                pq.add(Flight(end[0], start.cost + end[1], start.stop + 1))
            }
        }
        return -1
    }

    class Flight(val source: Int, val cost: Int, val stop: Int) : Comparable<Flight> {
        override fun compareTo(other: Flight): Int {
            return cost.compareTo(other.cost)
        }
    }
}

// 특정 정점에 가장 먼저 도착한 경우가 최소 비용이다
// 이 문제에서는 이미 방문한 정점이더라도 경유한 횟수가 적으면
// 최종적으로 최소 비용으로 도착점에 도착할 가능성이 있기 때문에 허용한다
// 이미 방문한 정점인데 경유한 횟수도 많은 경우는 제외한다
