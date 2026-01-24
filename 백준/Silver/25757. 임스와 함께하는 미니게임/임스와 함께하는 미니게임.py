n, g = input().split()
n = int(n)
players = {input() for _ in range(n)}
min_p = {'Y': 1, 'F': 2, 'O': 3} # 임스 제외

print(len(players)//min_p[g])