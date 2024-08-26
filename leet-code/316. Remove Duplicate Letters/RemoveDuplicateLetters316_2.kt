import java.util.*

class RemoveDuplicateLetters316_2 {
    fun removeDuplicateLetters(s: String): String {
        val counter: MutableMap<Char, Int> = mutableMapOf()
        val complete: MutableMap<Char, Boolean> = mutableMapOf()
        val stack: Deque<Char> = LinkedList()

        for (c in s) {
            counter[c] = counter.getOrDefault(c, 0) + 1
        }

        for (c in s) {
            counter[c] = counter[c]!! - 1

            if (complete.containsKey(c) && complete[c]!!) {
                continue
            }

            while (!stack.isEmpty() && stack.peek() > c && counter[stack.peek()]!! > 0) {
                complete[stack.pop()] = false
            }

            complete[c] = true
            stack.push(c)
        }

        val sb: StringBuilder = StringBuilder()
        while (!stack.isEmpty()) {
            sb.append(stack.pollLast())
        }
        return sb.toString()
    }
}