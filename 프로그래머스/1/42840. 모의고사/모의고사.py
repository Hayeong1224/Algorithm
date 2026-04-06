def solution(answers):
    ans1 = [1, 2, 3, 4, 5] * 2000
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5] * 2000
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 2000
    
    s1 = sum(1 for a, b in zip(answers, ans1) if a == b)
    s2 = sum(1 for a, b in zip(answers, ans2) if a == b)
    s3 = sum(1 for a, b in zip(answers, ans3) if a == b)
    
    scores = [s1, s2, s3]
    target = max(scores)
    
    ans = [i+1 for i, s in enumerate(scores) if s == target]
    
    return sorted(ans)