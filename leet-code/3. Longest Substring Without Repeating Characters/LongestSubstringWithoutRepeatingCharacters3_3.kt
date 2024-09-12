import kotlin.math.max

class LongestSubstringWithoutRepeatingCharacters3_3 {
    fun lengthOfLongestSubstring(s: String): Int {
        val map: MutableMap<Char, Int> = HashMap()
        var maxLength = 0
        var left = 0
        for (right in s.indices) {
            if (map.containsKey(s[right]) && map[s[right]]!! >= left) {
                left = map[s[right]]!! + 1
            } else {
                maxLength = max(maxLength, right - left + 1)
            }
            map[s[right]] = right
        }
        return maxLength
    }
}
