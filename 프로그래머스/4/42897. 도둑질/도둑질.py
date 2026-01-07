def solution(money):
    n = len(money)
    if n == 1: return money[0]

    d_f = [0] * n
    d_f[0] = money[0]
    d_f[1] = max(money[0], money[1])
    
    d_l = [0] * n
    d_l[1] = money[1]
    
    # 첫 번째 집을 터는 경우
    for i in range(2, n-1):
        d_f[i] = max(d_f[i-1], d_f[i-2]+money[i])
    
    # 마지막 집을 터는 경우
    for i in range(2, n):
        d_l[i] = max(d_l[i-1], d_l[i-2]+money[i])
    
    return max(max(d_f), max(d_l))