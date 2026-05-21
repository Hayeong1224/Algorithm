# import sys
# sys.stdin = open("sample_input.txt", "r")

T = 10
for t in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))

    # 조망권 확보된 세대 수
    # 조망권 확보 - 양쪽 모두 거리가 2 이상 확보
    cnt = 0

    # 층수가 다른 곳보다 일단 높아야 함!
    for i in range(2, N-2):
        maxAround = max(buildings[i-1], buildings[i-2], buildings[i+1], buildings[i+2])
        if buildings[i] > maxAround:
            cnt += buildings[i] - maxAround

    print(f"#{t} {cnt}")