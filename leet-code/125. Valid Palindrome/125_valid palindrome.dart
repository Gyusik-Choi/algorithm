class Solution {
  bool isPalindrome(String s) {
    s = s.toLowerCase();

    // 배열 시작 부분에 ^를 사용하면 not 의 의미를 갖는다
    // ^ 뒤의 조건에 해당하지 않는 문자열을 찾는다
    RegExp regex = new RegExp(r'[^0-9a-zA-Z]');
    String lowerAlphaNumericS = s.replaceAll(regex, '');  
    String reversedLowerAlphaNumericS = lowerAlphaNumericS.split('').reversed.join();

    return lowerAlphaNumericS == reversedLowerAlphaNumericS;
  }
}

// 참고
// https://api.dart.dev/stable/2.19.6/dart-core/String/replaceAll.html
// https://www.cloudhadoop.com/dart-string-contains-alphabet-number/
// https://stackoverflow.com/questions/21521729/how-do-i-reverse-a-string-in-dart
// https://api.dart.dev/stable/2.19.6/dart-core/List/reversed.html
// https://cosmosproject.tistory.com/180
// https://stackoverflow.com/questions/16944357/carets-in-regular-expressions
