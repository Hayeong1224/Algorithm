def solution(s):
    words = s.split(" ")
    answer = []
    
    for w in words:
        new_w = ''
        for i in range(len(w)):
            if i == 0 and w[i].isalpha():
                new_w += w[i].upper()
            elif w[i].isalpha:
                new_w += w[i].lower()
            else:
                new_w += w[i]
                
        answer.append(new_w)
                
    return " ".join(answer)