def solution(money):
    n = len(money)
    if n == 1: return money[0]

    # choose first -> ignore last
    dp_f = [0] * n
    dp_f[0] = money[0]
    dp_f[1] = max(money[0], money[1])
    
    for i in range(2, n-1):
        dp_f[i] = max(dp_f[i-2] + money[i], dp_f[i-1])
        
    # choose last -> ignore first
    dp_l = [0] * n
    dp_l[1] = money[1]
    for i in range(2, n):
        dp_l[i] = max(dp_l[i-2] + money[i], dp_l[i-1])
    
    
    return max(max(dp_f), max(dp_l))