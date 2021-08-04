# 백준

## 11657

벨만 포드 알고리즘을 활용하는 문제다. 벨만 포드 알고리즘에 대해서는 [이곳](https://github.com/Gyusik-Choi/Algorithm/blob/master/Algorithm/bellman_ford.py)에 정리해두었다.

최단 거리를 구하려면 경로에 싸이클(순환)이 생기면 안된다. 정점의 수가 A라면 경로의 수는 A - 1이 되어야 한다.

그래서 A - 1번에 걸쳐서 모든 경로들에 대한 edge relaxation을 해주고 추가적으로 1번을 더 검사하여 이때도 값이 줄어든다면 음의 순환이 생긴 것다.

