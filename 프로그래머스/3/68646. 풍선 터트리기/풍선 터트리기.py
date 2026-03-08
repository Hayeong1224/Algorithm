def solution(a):
    n = len(a)
    l, r = [float('inf')] * n, [float('inf')] * n
    for i in range(1, n-1):
        l[i] = min(l[i-1], a[i-1])
    for i in range(n-2, 0, -1):
        r[i] = min(r[i+1], a[i+1])
        
        
    ans = 2 # 양 끝 값
    for i in range(1, n-1):
        if a[i] < l[i] or a[i] < r[i]:
            ans += 1
    
    return ans