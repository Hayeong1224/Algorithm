def check(s, t):
  if len(s) == len(t):
    if s == t: return 1
    else: return 0

  if t[-1] == 'A':
    return check(s,t[:-1])

  else:
    return check(s, t[:-1][::-1])

S = input()
T = input()

print(check(S, T))