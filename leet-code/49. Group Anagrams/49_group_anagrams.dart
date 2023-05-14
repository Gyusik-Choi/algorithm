List<List<String>> groupAnagrams(List<String> strs) {
  Map<String, List<String>> anagramMaps = {};
  
  for (int i = 0; i < strs.length; i++) {
    List<String> s = strs[i].split('');
    s.sort();
    String sortedS = s.join('');
    
    if (anagramMaps.containsKey(sortedS)) {
      anagramMaps[sortedS]!.add(strs[i]);
    } else {
      anagramMaps[sortedS] = [strs[i]];
    }
  }

  List<List<String>> answer = [];
  anagramMaps.forEach((key, value) { answer.add(value); });

  return answer;
}

void main() {
  print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]));
}