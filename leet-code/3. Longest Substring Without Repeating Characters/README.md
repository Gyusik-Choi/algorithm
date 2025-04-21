# LeetCode

## 3. Longest Substring Without Repeating Characters

### Python

문자마다 가장 우측에 있는 값을 갱신하고 조회하기 위해 딕셔너리를 활용한다.

for 문을 돌면서 문자가 딕셔너리에 있으면서 부분 문자열을 판단하는 시작 위치가 해당 문자의 직전 위치값 (딕셔너리의 키로 해당 문자를 조회한 값 - 키의 값은 for 문을 돌면서 매번 갱신하므로 현재까지 가장 우측에 위치한 값을 갖는다) 보다 작거나 같으면 부분 문자열을 판단하는 시작 위치를 조정한다. 시작 위치는 직전 문자의 위치에서 한칸 이동한다. 

시작 위치가 해당 문자의 직전 위치보다 크다면 해당 문자는 이미 나온적이 있더라도 이전에 나왔을 당시의 위치는 현재 탐색 구간에 포함되지 않는다. 탐색 중인 부분 문자열 구간에 포함시켜서 최대 길이를 판단하는데 활용해야 한다.

<br>

### Java

#### LongestSubstringWithoutRepeatingCharacters3

교재의 풀이를 참고하지 않고 직접 풀이했다. 

s 길이만큼 for 문을 돌면서 s 의 문자가 해시맵에 문자가 존재하는 경우 왼쪽 비교 범위와 최대 길이, 임시 최대 길이를 갱신한다. 

해당 문자가 해시맵에 존재하는 경우 기존에 해당 문자가 위치한 범위 혹은 기존에 해당 문자가 위치한 범위보다 뒤에 위치한 해당 문자의 이전 문자가 중복된 범위부터 비교해야 한다.

예를 들어, abba 가 입력으로 주어졌을 때, 마지막 a 는 해시맵에서 a 를 조회하면 0이 나오는데 이때 올바른 비교 범위는 두번째 b 가 위치한 2부터다.

<br>

#### LongestSubstringWithoutRepeatingCharacters3_2

교재의 풀이를 참고했다. LongestSubstringWithoutRepeatingCharacters3 보다 간결하게 풀이했다.

LongestSubstringWithoutRepeatingCharacters3 의 경우 해시맵에 문자가 있는 경우에 최대 길이를 갱신하는데 이 풀이는 이와 반대로 해시맵에 문자가 없는 경우 최대 길이를 갱신한다. 

해시맵에 문자가 있는 경우 해시맵에서 조회한 문자의 값이 left 보다 크거나 같으면 left 를 갱신한다. 해시맵에서 조회한 문자의 값이 left 보다 크거나 같아야 올바른 비교 범위에 있는 것이다.

<br>

#### LongestSubstringWithoutRepeatingCharacters3_3

비교를 위해 lengthOfLongestSubstring 와 lengthOfLongestSubstringOld 두개의 함수를 뒀다.

교재의 풀이를 참고하지 않은 lengthOfLongestSubstringOld 를 교재의 풀이를 참고해서 lengthOfLongestSubstring 로 개선했다.

lengthOfLongestSubstringOld 의 경우 해시맵으로 문자별 인덱스 정보를 리스트로 구했다. 가장 앞선 인덱스에 접근하기 위해 리스트의 첫번째 인덱스에 접근했다. 

해시맵에 중복된 문자가 있는 경우 첫번째 인덱스 값을 제거하거나 prev 를 갱신해야 하는데 이를 위한 조건도 까다로웠다. 해시맵에 중복된 문자가 있으면 prev 안에 있으면서 가장 앞선 인덱스에 접근하기 위해 첫번째 인덱스 값은 항상 제거했다. 대신 prev 의 경우 기존 해시맵의 첫번째 인덱스 값이 prev 인덱스 보다 더 크거나 같은 경우만 갱신해야 한다.

이를 개선하기 위해서 해시맵에서 문자별 인덱스 정보를 리스트로 구하지 않고 최신 값만 유지하도록 했다. 이러면서 리스트에 더하거나 빼는 코드도 없어지고, prev 를 갱신하는 로직도 단순해졌다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

