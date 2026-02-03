def rotate_90(matrix, clockwise=True):
    if clockwise:
        return [list(row) for row in zip(*matrix[::-1])]
    else:
        return [list(row) for row in zip(*matrix)][::-1]

def rotate_U(cube):
    cube['U'] = rotate_90(cube['U'])
    temp = [cube['F'][0][i] for i in range(3)]
    for i in range(3): cube['F'][0][i] = cube['R'][0][i]
    for i in range(3): cube['R'][0][i] = cube['B'][0][i]
    for i in range(3): cube['B'][0][i] = cube['L'][0][i]
    for i in range(3): cube['L'][0][i] = temp[i]
    
def rotate_U_counter(cube):
    cube['U'] = rotate_90(cube['U'], False)
    temp = [cube['F'][0][i] for i in range(3)]
    for i in range(3): cube['F'][0][i] = cube['L'][0][i]
    for i in range(3): cube['L'][0][i] = cube['B'][0][i]
    for i in range(3): cube['B'][0][i] = cube['R'][0][i]
    for i in range(3): cube['R'][0][i] = temp[i]
    
def rotate_D(cube):
    cube['D'] = rotate_90(cube['D'])
    temp = [cube['F'][2][i] for i in range(3)]
    for i in range(3): cube['F'][2][i] = cube['L'][2][i]
    for i in range(3): cube['L'][2][i] = cube['B'][2][i]
    for i in range(3): cube['B'][2][i] = cube['R'][2][i]
    for i in range(3): cube['R'][2][i] = temp[i]
    
def rotate_D_counter(cube):
    cube['D'] = rotate_90(cube['D'], False)
    temp = [cube['F'][2][i] for i in range(3)]
    for i in range(3): cube['F'][2][i] = cube['R'][2][i]
    for i in range(3): cube['R'][2][i] = cube['B'][2][i]
    for i in range(3): cube['B'][2][i] = cube['L'][2][i]
    for i in range(3): cube['L'][2][i] = temp[i]
    
def rotate_L(cube):
    cube['L'] = rotate_90(cube['L'])
    temp = [cube['F'][i][0] for i in range(3)]
    for i in range(3): cube['F'][i][0] = cube['U'][i][0]
    for i in range(3): cube['U'][i][0] = cube['B'][2-i][2]
    for i in range(3): cube['B'][i][2] = cube['D'][2-i][0]
    for i in range(3): cube['D'][i][0] = temp[i]
    
def rotate_L_counter(cube):
    cube['L'] = rotate_90(cube['L'], False)
    temp = [cube['F'][i][0] for i in range(3)]
    for i in range(3): cube['F'][i][0] = cube['D'][i][0]
    for i in range(3): cube['D'][i][0] = cube['B'][2-i][2]
    for i in range(3): cube['B'][i][2] = cube['U'][2-i][0]
    for i in range(3): cube['U'][i][0] = temp[i]
    
def rotate_R(cube):
    cube['R'] = rotate_90(cube['R'])
    temp = [cube['F'][i][2] for i in range(3)]
    for i in range(3): cube['F'][i][2] = cube['D'][i][2]
    for i in range(3): cube['D'][i][2] = cube['B'][2-i][0]
    for i in range(3): cube['B'][i][0] = cube['U'][2-i][2]
    for i in range(3): cube['U'][i][2] = temp[i]
    
def rotate_R_counter(cube):
    cube['R'] = rotate_90(cube['R'], False)
    temp = [cube['F'][i][2] for i in range(3)]
    for i in range(3): cube['F'][i][2] = cube['U'][i][2]
    for i in range(3): cube['U'][i][2] = cube['B'][2-i][0]
    for i in range(3): cube['B'][i][0] = cube['D'][2-i][2]
    for i in range(3): cube['D'][i][2] = temp[i]
    
def rotate_F(cube):
    cube['F'] = rotate_90(cube['F'])
    temp = [cube['U'][2][i] for i in range(3)]
    for i in range(3): cube['U'][2][i] = cube['L'][2-i][2]
    for i in range(3): cube['L'][i][2] = cube['D'][0][i]
    for i in range(3): cube['D'][0][2-i] = cube['R'][i][0]
    for i in range(3): cube['R'][i][0] = temp[i]
    
def rotate_F_counter(cube):
    cube['F'] = rotate_90(cube['F'], False)
    temp = [cube['U'][2][i] for i in range(3)]
    for i in range(3): cube['U'][2][i] = cube['R'][i][0]
    for i in range(3): cube['R'][i][0] = cube['D'][0][2-i]
    for i in range(3): cube['D'][0][i] = cube['L'][i][2]
    for i in range(3): cube['L'][2-i][2] = temp[i]
    
def rotate_B(cube):
    cube['B'] = rotate_90(cube['B'])
    temp = [cube['U'][0][i] for i in range(3)]
    for i in range(3): cube['U'][0][i] = cube['R'][i][2]
    for i in range(3): cube['R'][i][2] = cube['D'][2][2-i]
    for i in range(3): cube['D'][2][i] = cube['L'][i][0]
    for i in range(3): cube['L'][2-i][0] = temp[i]
    
def rotate_B_counter(cube):
    cube['B'] = rotate_90(cube['B'], False)
    temp = [cube['U'][0][i] for i in range(3)]
    for i in range(3): cube['U'][0][i] = cube['L'][2-i][0]
    for i in range(3): cube['L'][i][0] = cube['D'][2][i]
    for i in range(3): cube['D'][2][i] = cube['R'][2-i][2]
    for i in range(3): cube['R'][i][2] = temp[i]
   
t = int(input())
for _ in range(t):

    cube = {'U': [['w'] * 3 for _ in range(3)],
        'D': [['y'] * 3 for _ in range(3)],
        'L': [['g'] * 3 for _ in range(3)],
        'R': [['b'] * 3 for _ in range(3)],
        'F': [['r'] * 3 for _ in range(3)],
        'B': [['o'] * 3 for _ in range(3)]}

    n = int(input())
    array = list(input().split())
    
    for a in array:
        side, dir = a[0], a[1]
        if dir == '+':
            if side == 'U': rotate_U(cube)
            elif side == 'D': rotate_D(cube)
            elif side == 'L': rotate_L(cube)
            elif side == 'R': rotate_R(cube)
            elif side == 'F': rotate_F(cube)
            elif side == 'B': rotate_B(cube)
        else:
            if side == 'U': rotate_U_counter(cube)
            elif side == 'D': rotate_D_counter(cube)
            elif side == 'L': rotate_L_counter(cube)
            elif side == 'R': rotate_R_counter(cube)
            elif side == 'F': rotate_F_counter(cube)
            elif side == 'B': rotate_B_counter(cube)
    
    for r in range(3):
        for c in range(3):
            print(cube['U'][r][c], end='')
        print()
    