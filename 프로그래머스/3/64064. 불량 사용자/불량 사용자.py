def solution(user_id, banned_id):
    n = len(banned_id)
    # 후보 찾기
    candidates = [[] for _ in range(n)]
    for i, id in enumerate(banned_id):
        for user in [u_id for u_id in user_id if len(id) == len(u_id)]:
            is_candidate = True
            for c1, c2 in zip(id, user):
                if c1 != '*' and c1 != c2:
                    is_candidate = False
                    break
            if is_candidate:
                candidates[i].append(user)
    answer = set()

    # 목록 찾기
    def dfs(banned, i):
        if i == n:
            answer.add(tuple(sorted(banned)))
            return
        
        for c in candidates[i]:
            if c not in banned:
                banned.append(c)
                dfs(banned, i+1)
                banned.pop()
        return
                
    dfs([],0)
    return len(answer)