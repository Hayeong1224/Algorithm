from collections import deque

def is_enable_to_change(a, b):
    cnt = 0
    for c1, c2 in zip(a,b):
        if c1 != c2:
            cnt += 1
    return True if cnt == 1 else False

def solution(begin, target, words):
    q = deque([(begin, 0)])
    while q:
        cur, dist = q.popleft()
        if cur == target:
            return dist
        
        for i in range(len(words)):
            w = words[i]
            if is_enable_to_change(cur, w):
                words[i] = ''
                q.append((w, dist+1))
    return 0