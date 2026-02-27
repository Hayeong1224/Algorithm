def solution(enroll, referral, seller, amount):
    n = len(enroll)
    hierarchy = {}
    idx = {}
    for i in range(n):
        idx[enroll[i]] = i
        if referral[i] != '-':
            hierarchy[enroll[i]] = referral[i]
    
    def cal(name, profit):
        up = profit // 10
        mine = profit - up
    
        if name in hierarchy: # 추천인이 있다면 10% 보내주기
            if up > 0:
                cal(hierarchy[name], up)
    
        result[idx[name]] += mine
        return
    
    result = [0] * n
    for i in range(len(seller)):
        cal(seller[i], amount[i] * 100)   
                   
    return result