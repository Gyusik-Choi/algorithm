class Solution {
  String twoPointers(String s, int start, int end) {
    while (start >= 0 && end <= s.length - 1 && s[start] == s[end]) {
      start -= 1;
      end += 1;
    }
    return s.substring(start + 1, end);
  }

  String longestPalindrome(String s) {
    if (s.length < 2 || s == s.split('').reversed.toList().join('')) {
      return s;
    }
    
    String longest = '';

    for (int i = 0; i < s.length - 1; i++) {
      String odd = twoPointers(s, i, i);
      String even = twoPointers(s, i, i + 1);

      if (longest.length < odd.length) {
        longest = odd;
      }

      if (longest.length < even.length) {
        longest = even;
      }
    }

    return longest;
  }
}

void main() {
  Solution solution = Solution();
  print(solution.longestPalindrome('babad'));
  print(solution.longestPalindrome('cbbd'));
  print(solution.longestPalindrome('babab'));
  print(solution.longestPalindrome('a'));
  print(solution.longestPalindrome('ab'));
}
