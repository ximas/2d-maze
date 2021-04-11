import pygame
import time

screen = pygame.display.set_mode((1600,900))

def drawboard(x,y):
    for col in range(x):
        for row in range(y):
            pygame.draw.rect(screen,(130,0,0),(col*100+400,row*100+50,100,100),0)
            pygame.draw.rect(screen,(200,0,0),(col*100+400,row*100+50,100,100),1)

def drawroute(lis,x,y,end):
    for _lis_ in lis:
        pygame.draw.rect(screen,(10,10,10),(((_lis_[1])*100)+300,((_lis_[0])*100)-50,100,100),0)
        pygame.draw.rect(screen,(255,255,255),(400,50,x*100,y*100),1)
    pygame.draw.rect(screen,(10,50,10),((end[0]*100)+300,(end[1]*100)-50,100,100),0)    
    pygame.display.update()


def move_command(lis):
    users = lis
    fin = 0
    while True:
        user = pygame.draw.circle(screen,(0,0,255),(lis[0],lis[1]),50,0)
        users = [user.x,user.y]
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
            [lis,users,fin] = move(move_key,lis,users)
        if key[K]:
            move_key = "K"
            [lis,users,fin] = move(move_key,lis,users)
        if key[J]:
            move_key = "J"
            [lis,users,fin] = move(move_key,lis,users)
        if key[L]:
            move_key = "L"
            [lis,users,fin] = move(move_key,lis,users)
        if key[Q]:
            pygame.display.quit()
            break
        if fin == 1:
            break


def move(move_key,lis,users):
    drawboard(8,8)
    drawroute([[1,8],[2,8],[3,8],[4,8],[5,8],[5,7],[5,6],[5,5],[4,5],[3,5],[2,5],[2,4],[2,3]
       ,[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7],
       [7,7],[7,8],[6,5],[5,4],[2,6],[1,5],[6,1]],8,8,[9,7])
    fin = 0
    if move_key == "I":
        if screen.get_at((users[0]+50,users[1]-50)) == (10,10,10,255) :
            lis[1] -= 100
            user = pygame.draw.circle(screen,(0,0,255),(lis[0],lis[1]),50,0)
            users = [user.x,user.y]
        elif screen.get_at((users[0]+50,users[1]-50)) == (10,50,10,255) :
            lis[1] -= 100
            user = pygame.draw.circle(screen,(0,0,255),(lis[0],lis[1]),50,0)
            print("Well Done! Press \"enter\" to continue...")
            fin = 1
    elif move_key == "K":
        if screen.get_at((users[0]+50,users[1]+100)) == (10,10,10,255) :
            lis[1] += 100
            user = pygame.draw.circle(screen,(0,0,255),(lis[0],lis[1]),50,0)
            users = [user.x,user.y]
        elif screen.get_at((users[0]+50,users[1]+100)) == (10,50,10,255) :
            lis[1] += 100
            user = pygame.draw.circle(screen,(0,0,255),(lis[0],lis[1]),50,0)
            print("Well Done! Press \"enter\" to continue...")
            fin = 1
    elif move_key == "J":
        if screen.get_at((users[0]-50,users[1])) == (10,10,10,255) :
            lis[0] -= 100
            user = pygame.draw.circle(screen,(0,0,255),(lis[0],lis[1]),50,0)
            users = [user.x,user.y]
        elif screen.get_at((users[0]-50,users[1])) == (10,50,10,255) :
            lis[0] -= 100
            user = pygame.draw.circle(screen,(0,0,255),(lis[0],lis[1]),50,0)
            print("Well Done! Press \"enter\" to continue...")
            fin = 1
    elif move_key == "L":
        if screen.get_at((users[0]+100,users[1])) == (10,10,10,255) :
            lis[0] += 100
            user = pygame.draw.circle(screen,(0,0,255),(lis[0],lis[1]),50,0)
        elif screen.get_at((users[0]+100,users[1])) == (10,50,10,255) :
            lis[0] += 100
            user = pygame.draw.circle(screen,(0,0,255),(lis[0],lis[1]),50,0)
            print("Well Done! Press \"enter\" to continue...")
            fin = 1
        
    return [lis,users,fin]


drawboard(8,8)

drawroute([[1,8],[2,8],[3,8],[4,8],[5,8],[5,7],[5,6],[5,5],[4,5],[3,5],[2,5],[2,4],[2,3]
           ,[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7],
           [7,7],[7,8],[6,5],[5,4],[2,6],[1,5],[6,1]],8,8,[9,7])

move_command([1150,100])




























