#백준 2178 미로탐색

#미로 최단거리 뽑느거
#BFS로 탐색하면 됨 간단

import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
lst = list()
for i in range(N):
    lst.append(list(map(int,input())))


dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >=M:
                continue
            if lst[nx][ny] == 0:
                continue
            elif lst[nx][ny] == 1:
                lst[nx][ny] = lst[x][y] + 1
                que.append((nx, ny))
    return lst[N-1][M-1]

print(bfs(0,0))

