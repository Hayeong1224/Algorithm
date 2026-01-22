from itertools import combinations
N, M = map(int, input().split())
houses, stores = [], []
for i in range(N):
  line = list(map(int, input().split()))
  for j in range(N):
    x = line[j]
    if x == 1:
      houses.append((i+1,j+1))
    elif x == 2:
      stores.append((i+1,j+1))

ans = float('inf')
# 남길 치킨집 정하는 조합
for selected_stores in combinations(stores, M):
  total_city_distance = 0

  for hx, hy in houses:
    temp_dist = float('inf')
    for sx, sy in selected_stores:
      d = abs(hx-sx) + abs(hy-sy)
      temp_dist = min(temp_dist, d)
    total_city_distance += temp_dist

  ans = min(ans, total_city_distance)

print(ans)