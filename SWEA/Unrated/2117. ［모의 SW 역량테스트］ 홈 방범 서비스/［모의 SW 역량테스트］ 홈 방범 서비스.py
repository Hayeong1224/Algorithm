from collections import deque
# import sys
# sys.stdin = open("sample_input.txt", "r")

dx = [0,1,0,-1]
dy = [1,0,-1,0]

# K가 고정됐을 때, (x, y) 중심 마름모 안에 들어오는 '손해 안 보는 최대 집의 수'를 찾는 함수
def bfs(x, y, K, cost):
    q = deque([(x, y, 1)]) # 현재 거리!
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True

    num_of_houses = 0

    while q:
        cx, cy, dist = q.popleft()

        # 맵 안이고 집이 있다면 카운트
        if board[cx][cy] == 1:
            num_of_houses += 1

        # 거리가 K면 더 퍼져나가지 않음
        if dist == K:
            continue

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, dist+1))

    if num_of_houses * M >= cost:
        return num_of_houses
    else:
        return 0

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_houses = 1
    for K in range(1, N + 2):
        # 운영 비용 = K * K + (K - 1) * (K - 1)
        cost = K * K + (K - 1) * (K - 1)

        # 모든 좌표에서 서비스 영역 햐보기!
        for r in range(N):
            for c in range(N):
                houses = bfs(r, c, K, cost)
                max_houses = max(max_houses, houses)

    print(f"#{test_case} {max_houses}")