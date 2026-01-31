from collections import deque 

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

lands = [[5] * (N) for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
  x, y, z = map(int, input().split())
  trees[x-1][y-1].append(z)

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

for _ in range(K):

  # 봄 and 여름
  for r in range(N):
    for c in range(N):
      if not trees[r][c]:
        continue

      new_trees = deque()
      dead_nutrient = 0
      for age in trees[r][c]:
        if lands[r][c] >= age:
          lands[r][c] -= age
          new_trees.append(age+1)
        else:
          dead_nutrient += (age // 2)

      trees[r][c] = new_trees
      lands[r][c] += dead_nutrient

  # 가을 and 겨울
  for r in range(N):
    for c in range(N):

      # 가을
      if trees[r][c]:
        for age in trees[r][c]:
          if age % 5 == 0:
            for i in range(8):
              nr, nc = r + dx[i], c + dy[i]
              if 0<=nr<N and 0<=nc<N:
                trees[nr][nc].appendleft(1)
      # 겨울
      lands[r][c] += A[r][c]

print(sum(len(trees[r][c]) for r in range(N) for c in range(N)))