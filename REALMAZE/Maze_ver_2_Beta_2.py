import pygame
import time

screen = pygame.display.set_mode((1600,800))

def board(maze,nums,lis):
    screen.fill((0,0,0))
    row = -1
    col = -1
    for line in maze:
        row += 1
        col = -1
        for square in line:
            col += 1
            if square == 0 :
                pygame.draw.rect(screen,(0,255,0),((col*100)+(nums[0]/2)+(lis[0]*100)+50,(row*100)+(nums[1]/2)+(lis[1]*100)+50,100,100),0)
            elif square == 1 :
                pygame.draw.rect(screen,(255,0,0),((col*100)+(nums[0]/2)+(lis[0]*100)+50,(row*100)+(nums[1]/2)+(lis[1]*100)+50,100,100),0)
            elif square == 2 :
                pygame.draw.rect(screen,(255,255,0),((col*100)+(nums[0]/2)+(lis[0]*100)+50,(row*100)+(nums[1]/2)+(lis[1]*100)+50,100,100),0)
            elif square == 3 :
                pygame.draw.rect(screen,(0,255,0),((col*100)+(nums[0]/2)+(lis[0]*100)+50,(row*100)+(nums[1]/2)+(lis[1]*100)+50,100,100),0)
                
    pygame.draw.rect(screen,(0,0,0),((nums[0]/2)-2250,(nums[1]/2)-1000,2000,2000),0)
    pygame.draw.rect(screen,(0,0,0),((nums[0]/2)-1000,(nums[1]/2)-2250,2000,2000),0)
    pygame.draw.rect(screen,(0,0,0),((nums[0]/2)+250,(nums[1]/2)-1000,2000,2000),0)
    pygame.draw.rect(screen,(0,0,0),((nums[0]/2)-1000,(nums[1]/2)+250,2000,2000),0)
    pygame.display.update() 
    
def main(lis,nums,bound,maze):
    board(maze,nums,lis)
    fin = 0
    while True:
        pygame.draw.circle(screen,(0,0,255),(int(nums[0]/2),int(nums[1]/2)),50,0)
        pygame.display.update()
        time.sleep(0.1)
        pygame.event.pump()
        key = pygame.key.get_pressed()
        I = pygame.K_i
        K = pygame.K_k
        J = pygame.K_j
        L = pygame.K_l
        Q = pygame.K_q
        if key[I]:
            move_key = "I"
            [lis,fin] = move(move_key,lis,maze,nums,bound)
        if key[K]:
            move_key = "K"
            [lis,fin] = move(move_key,lis,maze,nums,bound)
        if key[J]:
            move_key = "J"
            [lis,fin] = move(move_key,lis,maze,nums,bound)
        if key[L]:
            move_key = "L"
            [lis,fin] = move(move_key,lis,maze,nums,bound)
        if key[Q]:
            pygame.display.quit()
            break
        if fin == 1:
            break


def move(move_key,lis,maze,nums,bound):
    fin = 0
    direct = 0
    if move_key == "I":
        if lis[1] < -1:
            if maze[(lis[1]-(lis[1]*2))-2][(lis[0]-(lis[0]*2))-1] == 0:
                lis[1] += 1
                board(maze,nums,lis)
                pygame.draw.circle(screen,(0,0,255),(int(nums[0]/2),int(nums[1]/2)),50,0)
            elif maze[(lis[1]-(lis[1]*2))-2][(lis[0]-(lis[0]*2))-1] == 2:
                fin = 1
            elif maze[(lis[1]-(lis[1]*2))-2][(lis[0]-(lis[0]*2))-1] == 3:
                direct = "d"
    elif move_key == "K":
        if lis[1] > bound[1]:
            if maze[lis[1]-(lis[1]*2)][(lis[0]-(lis[0]*2))-1] == 0:
                lis[1] -= 1
                board(maze,nums,lis)
                pygame.draw.circle(screen,(0,0,255),(int(nums[0]/2),int(nums[1]/2)),50,0)
            elif maze[lis[1]-(lis[1]*2)][(lis[0]-(lis[0]*2))-1] == 2:
                fin = 1
            elif maze[lis[1]-(lis[1]*2)][(lis[0]-(lis[0]*2))-1] == 3:
                direct = "u"
    elif move_key == "J":
        if lis[0] < -1:
            if maze[(lis[1]-(lis[1]*2))-1][(lis[0]-(lis[0]*2))-2] == 0:
                lis[0] += 1
                board(maze,nums,lis)
                pygame.draw.circle(screen,(0,0,255),(int(nums[0]/2),int(nums[1]/2)),50,0)
            elif maze[(lis[1]-(lis[1]*2))-1][(lis[0]-(lis[0]*2))-2] == 2:
                fin = 1
            elif maze[(lis[1]-(lis[1]*2))-1][(lis[0]-(lis[0]*2))-2] == 3:
                direct = "r"
    elif move_key == "L":
        if lis[0] > bound[0]:
            if maze[(lis[1]-(lis[1]*2))-1][(lis[0]-(lis[0]*2))] == 0:
                lis[0] -= 1
                board(maze,nums,lis)
                pygame.draw.circle(screen,(0,0,255),(int(nums[0]/2),int(nums[1]/2)),50,0)
            elif maze[(lis[1]-(lis[1]*2))-1][(lis[0]-(lis[0]*2))] == 2:
                fin = 1
            elif maze[(lis[1]-(lis[1]*2))-1][(lis[0]-(lis[0]*2))] == 3:
                direct = "l"
    if direct == "d":
        print(direct)
        pygame.draw.circle(screen,(50,50,50),(int(nums[0]/2),int(nums[1]/2)),50,0)
    elif direct == "l":
        pygame.draw.circle(screen,(50,50,50),(500,500),1000,0)
    elif direct == "u":
        [col,row] = check_boulder(maze)
        pygame.draw.circle(screen,(50,50,50),((col*100)-(lis[0]*100),int(row*100)+50),50,0)
    elif direct == "r":
        pygame.draw.circle(screen,(50,50,50),(500,500),1000,0)
        
    pygame.display.update()        
    return [lis,fin]

def check_boulder(maze):
    row = -1
    col = -1
    for line in maze:
        row += 1
        col = -1
        for square in line:
            col += 1
            if square == 3:
                break
    return [col-1,row/2]

# -player pos , screensize, -boundary, map --------------------------

