class Solution {
  bool isdigit(String word) {
    RegExp regExp = RegExp(r'[0-9]');
    // https://api.flutter.dev/flutter/dart-core/RegExp-class.html
    return regExp.allMatches(word).toList().length == word.length;
  }

  List<String> reorderLogFiles(List<String> logs) {
    List<String> letters = [];
    List<String> digits = [];

    for (int i = 0; i < logs.length; i++) {
      String log = logs[i];
      String word = log.split(' ')[1];

      if (isdigit(word)) {
        digits.add(log);
      } else {
        letters.add(log);
      }
    }

    letters.sort((a, b) {
      String letterWithoutIdentifierA = a.substring(a.indexOf(' ') + 1);
      String letterWithoutIdentifierB = b.substring(b.indexOf(' ') + 1);

      // letter-logs 의 식별자를 제외한 content 가 같을 경우
      // 식별자로 정렬
      if (letterWithoutIdentifierA == letterWithoutIdentifierB) {
        return a.substring(0, a.indexOf(' ') + 1).compareTo(b.substring(0, b.indexOf(' ') + 1));
      }

      return letterWithoutIdentifierA.compareTo(letterWithoutIdentifierB);
    });

    return [...letters, ...digits];
  }
}

void main() {
  Solution solution = Solution();
  print(solution.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]));
}

// 참고
// https://monsters-dev.tistory.com/39
