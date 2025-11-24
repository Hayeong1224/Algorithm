def solution(name):
    answer = 0
    
    #최소 이동 -> 다음/이전 & 오른쪽/왼쪽
    l = len(name)

    for c in name:
        # 다음/이전 최소 이동
        answer += min(ord(c)-ord('A'), 1+ord('Z')-ord(c))
    
    # 오른쪽/왼쪽 최소 이동
    move = l - 1   # 기본: 오른쪽으로 쭉 가기

    for i in range(l):
        next_i = i + 1
        # 다음 non-A 찾기
        while next_i < l and name[next_i] == 'A':
            next_i += 1

        # 좌우 왕복 고려
        move = min(
            move,
            i * 2 + (l - next_i),
            (l - next_i) * 2 + i
        )

    answer += move
    
    return answer