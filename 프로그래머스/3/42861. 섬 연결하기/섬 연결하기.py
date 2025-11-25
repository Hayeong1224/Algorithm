def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    answer = 0
    
    # union-find 사용하자!
    parents = [i for i in range(n)]
    
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(a, b):
        rootA = find(a)
        rootB = find(b)
        if rootA != rootB:
            parents[rootB] = rootA
            return True
        return False
    
    count = 0
    
    # union-find 사용
    for a, b, cost in costs:
        if union(a,b):
            answer += cost
            count += 1
        if count == n-1:
            break
    
    return answer