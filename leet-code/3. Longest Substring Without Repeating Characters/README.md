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



