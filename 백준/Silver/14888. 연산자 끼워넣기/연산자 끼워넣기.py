def dfs(i, s, op):
  global max_v, min_v
  if i == N:
    max_v = max(max_v, s)
    min_v = min(min_v, s)
    return

  for d in range(4):
    if op[d] > 0:
      op[d] -= 1
      
      if d == 0: dfs(i+1, s + A[i], op)
      elif d == 1: dfs(i+1, s - A[i], op)
      elif d == 2: dfs(i+1, s * A[i], op)
      # 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 
      else: dfs(i+1, int(s / A[i]), op)
      
      op[d] += 1

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split())) # +, -, x, //

max_v, min_v = -float('inf'), float('inf')
dfs(1, A[0], op)
print(max_v)
print(min_v)