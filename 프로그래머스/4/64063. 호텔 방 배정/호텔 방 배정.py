import sys
sys.setrecursionlimit(10**6)

def find_room(rooms, r):
    # 1. empty
    if r not in rooms:
        # next possible room
        rooms[r] = r + 1
        return r
    
    # 2. full
    empty = find_room(rooms, rooms[r])
    rooms[r] = empty + 1
    return empty

def solution(k, room_number):
    rooms = {}
    answer = []
    
    for r in room_number:
        assigned = find_room(rooms, r)
        answer.append(assigned)
        
    return answer