
def dfs(s, t):
  if s == t:
    return True

  if len(t) <= len(s):
    return False

  # 마지막 글자가 A면 떼기
  if t[-1] == 'A':
    if dfs(s, t[:-1]):
      return True

  # 첫 글자가 B면 떼고 뒤집기
  if t[0] == 'B':
    if dfs(s, t[1:][::-1]):
      return True

  return False

def solve():
  S = input()
  T = input()

  if dfs(S, T):
    print(1)
  else:
    print(0)


solve()