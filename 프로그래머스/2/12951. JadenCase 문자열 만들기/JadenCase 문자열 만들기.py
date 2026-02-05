def solution(s):
    answer = []
    
    for w in s.split(" "):
        # answer.append(w[0].upper() + w[1:].lower() if w[0].isalpha() else w[0] + w[1:].lower())
        answer.append(w.capitalize())
        
    return " ".join(answer)