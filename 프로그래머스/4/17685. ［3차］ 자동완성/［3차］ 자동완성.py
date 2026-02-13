def solution(words):
    words.sort()
    result = []

    for i in range(len(words)):
        cnt1, cnt2 = 0, 0
        
        if i-1 >= 0: # 앞 비교
            for j in range(len(words[i-1])):
                if words[i][j] != words[i-1][j]:
                    break
                cnt1 += 1
                
        if i+1 < len(words): # 뒤 비교
            for j in range(len(words[i])):
                if words[i][j] != words[i+1][j]:
                    break
                cnt2 += 1
        
        cnt = max(cnt1, cnt2)
        
        if cnt == len(words[i]):
            result.append(cnt)
        else:
            result.append(cnt + 1)
    
    return sum(result)