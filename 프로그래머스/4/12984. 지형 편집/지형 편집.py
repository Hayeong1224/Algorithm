def solution(land, P, Q):
    h = []
    for row in land:
        h.extend(row)
    h.sort()
    
    n = len(h)
    total_sum = sum(h)
    cur_h = h[0]
    
    cost = (total_sum - cur_h * n) * Q # 제일 낮게 깎기
    answer = cost
    
    for i in range(1, n):
        if h[i] != h[i-1]:
            diff = h[i] - h[i-1]
            # i개는 diff만큼 쌓기 + n-1개는 diff만큼 덜 깎기! 
            cost += (i * diff * P) - ((n-i) * diff * Q)
            answer = min(answer, cost)
    
    return answer