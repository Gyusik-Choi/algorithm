String mostCommonWord(String paragraph, List<String> banned) {
  RegExp regExp = RegExp('[^a-zA-Z]');
  List<String> p = paragraph.replaceAll(regExp, ' ').toLowerCase().split(' ');
  Map<String, int> p_map = Map();

  for (int i = 0; i < p.length; i++) {
    String word = p[i];

    // 빈 문자열도 있어서 '' 여부를 체크한다
    if (word.isNotEmpty && !banned.contains(word)) {
      if (p_map.containsKey(word)) {
        p_map[word] = (p_map[word] as int) + 1;
      } else {
        p_map[word] = 1;
      }
    }
  }

  int max_cnt = 0;
  String common_word = '';

  for (var element in p_map.entries) {
    String k = element.key;
    int v = element.value;

    if (max_cnt < v) {
      max_cnt = v;
      common_word = k;
    }
  }

  return common_word;
}

void main() {
  print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]));
}
