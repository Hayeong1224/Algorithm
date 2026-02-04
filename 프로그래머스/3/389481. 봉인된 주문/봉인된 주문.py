def alpha_to_num(alpha):
    result = 0
    for idx, a in enumerate(alpha[::-1]): 
        result += (ord(a) - ord('a') + 1) * (26 ** idx)
    return result

def num_to_alpha(num):
    result = []
    while num > 0:
        num -= 1 # 0~25로 맞추게
        result.append(chr(ord('a') + (num % 26)))
        num //= 26
    return "".join(result[::-1])
    
def solution(n, bans):
    ban_num = sorted([alpha_to_num(b) for b in bans])
    for b in ban_num:
        if b <= n:
            n += 1
        else:
            break
            
    return num_to_alpha(n)