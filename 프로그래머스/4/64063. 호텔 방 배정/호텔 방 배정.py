import sys
sys.setrecursionlimit(2**31 - 1)

def solution(k, room_number):
    rooms = {}
    answer = []
    
    for r in room_number:
        assigned_room = find_room(rooms, r)
        answer.append(assigned_room)
        
    return answer

def find_room(rooms, r):
    if r not in rooms: # empty room
        rooms[r] = r + 1
        return r
    
    # already full
    empty = find_room(rooms, rooms[r])
    rooms[r] = empty + 1
    
    return empty
    