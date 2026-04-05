def dfs(tickets, used, cur, path):
    if False not in used:
        return path
    
    for i in range(len(tickets)):
        if not used[i] and cur == tickets[i][0]:
            used[i] = True
            res = dfs(tickets, used, tickets[i][1], path + [tickets[i][1]])
            if res: 
                return res
            
            used[i] = False
            
    return None

def solution(tickets):
    tickets.sort(key = lambda x : x[1])
    used = [False] * len(tickets)
    return dfs(tickets, used, 'ICN', ['ICN'])     