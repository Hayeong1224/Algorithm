def solution(participant, completion):
    players = {}
    for p in participant:
        players[p] = players.get(p, 0) + 1
    for c in completion:
        players[c] -= 1
    
    for p in players:
        if players.get(p, 0) > 0: 
            return p 