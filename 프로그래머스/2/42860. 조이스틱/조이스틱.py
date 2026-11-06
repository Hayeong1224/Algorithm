def solution(name):
    n = len(name)
    
    # 알파벳 이동 (상하)
    up_down = 0
    for c in name:
        up_down += min(ord(c)-ord('A'), ord('Z')-ord(c)+1)
    
    # 커서 이동 (좌우) => min(abs(t-c), n - max(c, t) + min(c, t))
    # 그냥 오른쪽으로 쭉 / A 구간 안 가고 오른쪽으로 가다가 왼쪽으로 가는 / A 구간 안 가고 왼쪽으로 가다 오른족으로 가는
    left_right = n - 1
    
    for i in range(n):
        nxt = i + 1
        
        # A가 아닌 nxt 구하기
        while nxt < n and name[nxt] == 'A':
            nxt += 1
            
        left_right = min(
            left_right,
            2 * i + (n - nxt),
            i + 2 * (n - nxt)
        )
    return up_down + left_right