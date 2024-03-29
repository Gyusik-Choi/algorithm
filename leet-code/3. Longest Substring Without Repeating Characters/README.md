# LeetCode

## 3. Longest Substring Without Repeating Characters

문자마다 가장 우측에 있는 값을 갱신하고 조회하기 위해 딕셔너리를 활용한다.

for 문을 돌면서 문자가 딕셔너리에 있으면서 부분 문자열을 판단하는 시작 위치가 해당 문자의 직전 위치값 (딕셔너리의 키로 해당 문자를 조회한 값 - 키의 값은 for 문을 돌면서 매번 갱신하므로 현재까지 가장 우측에 위치한 값을 갖는다) 보다 작거나 같으면 부분 문자열을 판단하는 시작 위치를 조정한다. 시작 위치는 직전 문자의 위치에서 한칸 이동한다. 

시작 위치가 해당 문자의 직전 위치보다 크다면 해당 문자는 이미 나온적이 있더라도 이전에 나왔을 당시의 위치는 현재 탐색 구간에 포함되지 않는다. 탐색 중인 부분 문자열 구간에 포함시켜서 최대 길이를 판단하는데 활용해야 한다.