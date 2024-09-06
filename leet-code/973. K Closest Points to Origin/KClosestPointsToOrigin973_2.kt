import java.util.PriorityQueue

class KClosestPointsToOrigin973_2 {
    fun kClosest(points: Array<IntArray>, k: Int): Array<IntArray> {
        val pq: PriorityQueue<Point> = PriorityQueue<Point>(Comparator.comparingInt{ it.distance })
        for (point in points) {
            pq.add(Point(point))
        }
        val answer: Array<IntArray> = Array(k) { intArrayOf() }
        for (i in 0 until k) {
            answer[i] = pq.poll().point
        }
        return answer
    }

    class Point(val point: IntArray) {
        val distance: Int = (point[0] * point[0]) + (point[1] * point[1])
    }
}