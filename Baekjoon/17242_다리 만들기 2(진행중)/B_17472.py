import sys


def dfs():
    pass


N, M = map(int, sys.stdin.readline().split())
islands = []
for _ in range(N):
    island = list(map(int, sys.stdin.readline().split()))
    islands.append(island)

for i in range(N):
    for j in range(M):
        if islands[i][j] == 1:


# dfs 로 1의 정점별 갈 수 있는 [도착지, 거리] 값 구해서 딕셔너리로 정리
# mst 로 최소 연결 비용 구하기
# 크루스칼을 쓰려면 인덱스화 + [거리, 출발 인덱스, 도착 인덱스]