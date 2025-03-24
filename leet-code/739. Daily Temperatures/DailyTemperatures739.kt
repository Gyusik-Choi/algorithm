import java.util.*

class DailyTemperatures739_2 {
    fun dailyTemperatures(temperatures: IntArray): IntArray {
        val answer: IntArray = IntArray(temperatures.size)
        val stack: Deque<Int> = LinkedList()
        for (cur in temperatures.indices) {
            while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[cur]) {
                val prev = stack.pop()
                answer[prev] = cur - prev
            }
            stack.push(cur)
        }
        return answer
    }
}