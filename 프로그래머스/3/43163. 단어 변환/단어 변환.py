from collections import deque

def is_one_diff(word1, word2):
    return sum(1 for a, b in zip(word1, word2) if a != b) == 1

def solution(begin, target, words):
    visited = [0] * len(words)
    queue = deque([(begin, 0)])
    
    while queue:
        current, d = queue.popleft()
        
        if current == target:
            return d
        
        for i in range(len(words)):
            if visited[i] == 0 and is_one_diff(current, words[i]):
                visited[i] = 1
                queue.append((words[i], d+1))
    
    return 0