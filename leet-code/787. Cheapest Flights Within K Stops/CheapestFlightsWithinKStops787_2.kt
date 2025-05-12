package com.example

import java.util.PriorityQueue

class CheapestFlightsWithinKStops787_2 {
    // 일반적으로 풀이했던 다익스트라와 달리
    // 방문한 정점을 다시 방문할 수 있도록 하는 조건이 필요하다
    fun findCheapestPrice(n: Int, flights: Array<IntArray>, src: Int, dst: Int, k: Int): Int {
        // 인접 리스트로 정점별 방문 가능한 정점 및 비용 정보
        val map = mutableMapOf<Int, MutableList<IntArray>>()
        for (flight in flights) {
            val start = flight[0]
            val end = flight[1]
            val price = flight[2]
            map.putIfAbsent(start, mutableListOf())
            map[start]!!.add(intArrayOf(end, price))
        }

        // 정점별 경유 횟수
        val stops = IntArray(n)
        // 출발지, 비용, 경유 횟수
        val pq = PriorityQueue<IntArray>{ o1, o2 -> o1[1] - o2[1]}
        pq.add(intArrayOf(src, 0, 0))

        while (!pq.isEmpty()) {
            val departure = pq.poll()

            if (departure[0] == dst) {
                return departure[1]
            }

            if (departure[2] > k) {
                continue
            }

            // 경유 횟수 갱신
            // (일종의 방문 처리)
            stops[departure[0]] = departure[2]

            if (!map.containsKey(departure[0])) {
                continue
            }

            for (arrival in map[departure[0]]!!) {
                // stops 를 기준으로 보면
                // 0 -> 1 -> 2 로 가는 경로를 거치면
                // 정점 2의 경유 횟수는 2가 된다
                // 그리고나서
                // 0 -> 2 로 가는 경로가 있으면
                // 정점 0의 경유 횟수는 0이라
                // 정점 0의 경유 횟수에 1을 더한 것보다 정점 2의 경유 횟수가 더 크다
                if (stops[arrival[0]] == 0 || stops[arrival[0]] > departure[2] + 1) {
                    pq.add(intArrayOf(arrival[0], departure[1] + arrival[1], departure[2] + 1))
                }
            }
        }

        return -1
    }
}