# 프로그래머스

## 스킬트리

위상정렬을 활용하는 문제다.

선행 스킬에 포함되지 않는 스킬은 순서에 상관없이 배울 수 있으며, 선행 스킬에 포함되는 스킬은 위상 정렬을 통해 우선 순위가 맞는지 판단해야 한다.

skill_degree 는 각 스킬별로 우선 순위 정보를 갖고, skill_priorities 는 각 스킬별로 자신과 연결된 후순위의 스킬들을 갖는다.

예를 들어 skill 이 "CBD" 라면 skill_degree, skill_priorities 는 아래와 같다.

```python
skill_degree = {"C": 0, "B": 1, "D": 2}
skill_priorities = {"C": ["B", "D"], "B": ["D"], "D": []}
```

<br>

C 가 맨 앞에 있기 때문에 우선 순위가 가장 높으며 그 다음으로 B, D 순서로 우선 순위가 높다. C 는 B, D 가 후순위 스킬이며 B 는 D 가 후순위 스킬이며 D 는 후순위 스킬이 없다.

<br>

for 문으로 skills 를 순회하면서 for 문의 요소가 skill_priorities 에 없으면 선행 스킬에 포함되지 않는 스킬이라 배울 수 있다. for 문의 요소가 skill_priorities 에 있으면 skill_degree 가 1이상이면 최우선 순위가 아니라 배울 수 없다. skill_degree 가 0이면 최우선 순위라 배울 수 있고 자신과 연결된 후순위의 스킬들의 skill_degree 값을 1씩 뺀다.

for 문을 빠져나오면 모두 배울 수 있는 스킬들이다.

