def solution(n, results):
    win = [set() for _ in range(n+1)]
    lose = [set() for _ in range(n+1)]
    
    for a, b in results:
        win[a].add(b)
        lose[b].add(a)
        
    for i in range(1,n+1):
        # 나에게 진 사람들은 내가 진 사람들한테도 진 거
        for loser in win[i]:
            lose[loser].update(lose[i])
        # 나를 이긴 사람들은 내가 이긴 사람들도 이긴 거
        for winner in lose[i]:
            win[winner].update(win[i])
            
    answer = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
            
    return answer