def dfs(tickets, used, path, cur):
    if False not in used:
        return path
    
    for i in range(len(tickets)):
        departure, dest = tickets[i]
        if departure == cur and not used[i]:
            used[i] = True
            result = dfs(tickets, used, path + [dest], dest)
            if result:
                return result
            used[i] = False
    
def solution(tickets):
    tickets.sort()
    used = [False for _ in range(len(tickets))]
    return dfs(tickets, used, ["ICN"], "ICN")