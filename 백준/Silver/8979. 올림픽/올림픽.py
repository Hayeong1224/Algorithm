# 금 은 동
N, K = map(int, input().split())
contries = []
for _ in range(N): # i, g, s, b
  contries.append(list(map(int,input().split())))
contries.sort(key= lambda x: (-x[1], -x[2], -x[3]))

ranking = {}
cur_ranking = 1
for i in range(N):
  x1, g1, s1, b1 = contries[i]
  ranking[x1] = cur_ranking
  if i < N-1:
    x2, g2, s2, b2 = contries[i+1]
    if g1!=g2 or s1!=s2 or b1!=b2:
      cur_ranking += 1

print(ranking[K])