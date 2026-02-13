def solution(cookie):
    # 누적합
    pre_sum = [0, cookie[0]]
    for c in cookie[1:]:
        pre_sum.append(pre_sum[-1] + c)
    
    result = [0]
    for l in range(1,len(cookie)):
        m = {pre_sum[l]}
        for r in range(l+1, len(cookie)+1):
            t = (pre_sum[r] + pre_sum[l-1]) / 2
            
            if t in m:
                result.append(t - pre_sum[l-1])
                
            m.add(pre_sum[r])
            
    return max(result)       