import java.util.*

class NetworkDelayTime743_2 {
    fun networkDelayTime(times: Array<IntArray>, n: Int, k: Int): Int {
        val map: MutableMap<Int, MutableList<IntArray>> = mutableMapOf()
        for (time in times) {
            map.putIfAbsent(time[0], mutableListOf())
            map[time[0]]!!.add(intArrayOf(time[1], time[2]))
        }

        fun dijkstra(): IntArray {
            val distance: IntArray = IntArray(n + 1)
            val visit: BooleanArray = BooleanArray(n + 1)
            var pq: PriorityQueue<IntArray> = PriorityQueue<IntArray>(compareBy { it[1] })

            for (i in distance.indices) distance[i] = Int.MAX_VALUE
            distance[0] = 0
            distance[k] = 0
            pq.add(intArrayOf(k, 0))

            while (!pq.isEmpty()) {
                val start = pq.poll()
                if (visit[start[0]]) continue
                visit[start[0]] = true
                if (!map.containsKey(start[0])) continue
                for (end in map[start[0]]!!) {
                    if (distance[end[0]] < distance[start[0]] + end[1]) continue
                    distance[end[0]] = distance[start[0]] + end[1]
                    pq.add(intArrayOf(end[0], distance[end[0]]))
                }
            }

            return distance
        }

        val distanceInfo = dijkstra()
        if (isNotConnected(distanceInfo)) return -1
        return getMaxValue(distanceInfo)
    }

    private fun isNotConnected(array: IntArray): Boolean {
        return array.any { it == Int.MAX_VALUE }
    }

    private fun getMaxValue(array: IntArray): Int {
        return array.max()
    }
}
