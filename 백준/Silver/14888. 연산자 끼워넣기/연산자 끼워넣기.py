def dfs(n, temp, p, m, mu, d):
  global min_ans, max_ans
  
  if n == N:
    min_ans = min(min_ans, temp)
    max_ans = max(max_ans, temp)
    return

  if p > 0:
    dfs(n+1, temp+array[n], p-1, m, mu, d)

  if m > 0:
    dfs(n+1, temp-array[n], p, m-1, mu, d)

  if mu > 0:
    dfs(n+1, temp*array[n], p, m, mu-1, d)

  if d > 0:
    dfs(n+1, int(temp/array[n]), p, m, mu, d-1)


N = int(input())
array = list(map(int, input().split()))
p, m, mu, d = map(int, input().split())
      
min_ans, max_ans = float('inf'), -float('inf')
dfs(1,array[0], p, m, mu, d)
print(max_ans, min_ans, sep='\n')