def solution(n, results):
    win = [set() for _ in range(n+1)]
    lose = [set() for _ in range(n+1)]
    
    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if k in win[i] and j in win[k]:
                    win[i].add(j)
                    lose[j].add(i)
    
    return sum(1 for i in range(1, n+1) if len(win[i]) + len(lose[i]) == n-1)