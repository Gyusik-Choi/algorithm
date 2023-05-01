class Solution {
  void reverseString(List<String> s) {
    int front = 0;
    int back = s.length - 1;

    while (front < back) {
      String temp = s[front];
      s[front] = s[back];
      s[back] = temp;

      front += 1;
      back -= 1;
    }
  }
}

void main() {
  Solution solution = Solution();
  solution.reverseString(["h", "e", "l", "l", "o"]);
}
