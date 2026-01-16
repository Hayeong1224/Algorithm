n, m = map(int, input().split())
result = []

def dfs(num):
  if len(result) == m:
    print(*(result))
    return

  for i in range(1,n+1):
    result.append(i)
    dfs(i)
    result.pop()

dfs(1)