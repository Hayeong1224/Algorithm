def solution(sticker):
    n = len(sticker)

    if n == 1: return sticker[0]
    
    # 처음 스티커 사용 -> 두 번째 스티커, 마지막 스티커 사용 x
    dp_f = [0] * n
    dp_f[0], dp_f[1] = sticker[0], sticker[0]

    for i in range(2, n-1):
        dp_f[i] = max(dp_f[i-1], dp_f[i-2] + sticker[i])
    
    # 처음 스티커 사용 x -> 마지막 스티커 사용
    dp_l = [0] * n
    dp_l[1] = sticker[1]
    
    for i in range(2, n):
        dp_l[i] = max(dp_l[i-1], dp_l[i-2] + sticker[i])
        
    return max(dp_f[n-2], dp_l[n-1])