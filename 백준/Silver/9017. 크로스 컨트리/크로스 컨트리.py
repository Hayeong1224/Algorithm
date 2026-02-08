T = int(input())
for _ in range(T):
  N = int(input())
  ranking = list(map(int, input().split()))
  teams = [[] for _ in range(max(ranking)+1)]

  cnt = 0
  for rank, t in enumerate(ranking):
    if ranking.count(t) < 6:
      cnt += 1
      continue

    if t not in teams:
      teams[t].append(rank+1-cnt)

  winner, winner_score = -1, float('inf')
  for t in range(len(teams)):
    if len(teams[t]) < 6:
      continue
      
    team_score = sum(teams[t][:4])
    if team_score < winner_score or (team_score == winner_score and teams[winner][4] > teams[t][4]):
      winner, winner_score = t, team_score

  print(winner)