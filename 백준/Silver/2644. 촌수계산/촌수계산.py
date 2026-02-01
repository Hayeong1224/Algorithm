def dfs(x, y, cnt):
  if x == y:
    return cnt

  for r in relations[x]:
    if not visited[r]:
      visited[r] = True
      result = dfs(r,y,cnt+1)

      if result != -1:
        return result

  return -1

N = int(input())
a, b = map(int,input().split())
M = int(input())
relations = [[] for _ in range(N)]
for _ in range(M):
  x, y = map(int, input().split())
  relations[x-1].append(y-1)
  relations[y-1].append(x-1)
  
visited = [False] * N
visited[a-1] = True
print(dfs(a-1,b-1,0)) 