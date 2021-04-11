import pygame
import time

nums = (1600,900)

screen = pygame.display.set_mode(nums)

def board(maze,nums,lis):
    row = -1
    col = -1
    for line in maze:
        row += 1
        col = -1
        for square in line:
            col += 1
            if square == 0 :
                pygame.draw.rect(screen,(0,255,0),((col*100)+(nums[0]/2)+(lis[0]*100),(row*100)+(nums[1]/2)+(lis[1]*100),100,100),0)
            elif square == 1 :
                pygame.draw.rect(screen,(0,255,0),((col*100)+(nums[0]/2)+(lis[0]*100),(row*100)+(nums[1]/2)+(lis[1]*100),100,100),0)
 #   pygame.draw.rect(screen,(0,0,0),((nums[0]/2)-2150,(nums[1]/2)-1000,2000,2000),0)
 #   pygame.draw.rect(screen,(0,0,0),((nums[0]/2)-1000,(nums[1]/2-2150),2000,2000),0)
 #   pygame.draw.rect(screen,(0,0,0),((nums[0]/2)+150,(nums[1]/2)-1000,2000,2000),0)
  #  pygame.draw.rect(screen,(0,0,0),((nums[0]/2)-1000,(nums[1]/2)+150,2000,2000),0)
    pygame.display.update() 
    
def main(lis,nums):
    board([[1,1,1,1,0,1,1,0],
      [1,0,0,0,0,0,1,0],
      [1,0,1,1,0,1,1,0],
      [1,0,1,1,0,1,1,0],
      [1,0,1,0,0,0,0,0],
      [0,0,1,1,0,1,1,1],
      [1,0,1,1,1,1,0,0],
      [1,0,0,0,0,0,0,1]],nums,lis)
    maze=[[1,1,1,1,0,1,1,0],
      [1,0,0,0,0,0,1,0],
      [1,0,1,1,0,1,1,0],
      [1,0,1,1,0,1,1,0],
      [1,0,1,0,0,0,0,0],
      [0,0,1,1,0,1,1,1],
      [1,0,1,1,1,1,0,0],
      [1,0,0,0,0,0,0,1]]
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
            [lis] = move(move_key,lis,maze,nums)
        if key[K]:
            move_key = "K"
            [lis] = move(move_key,lis,maze,nums)
        if key[J]:
            move_key = "J"
            [lis] = move(move_key,lis,maze,nums)
        if key[L]:
            move_key = "L"
            [lis] = move(move_key,lis,maze,nums)
        if key[Q]:
            pygame.display.quit()
            break


def move(move_key,lis,maze,nums):
    if move_key == "I":
        if lis[1] > 1:
            if maze[lis[1]-2][lis[0]-1] == 0:
                lis[1] += 1
                board([[1,1,1,1,0,1,1,0],
                  [1,0,0,0,0,0,1,0],
                  [1,0,1,1,0,1,1,0],
                  [1,0,1,1,0,1,1,0],
                  [1,0,1,0,0,0,0,0],
                  [0,0,1,1,0,1,1,1],
                  [1,0,1,1,1,1,0,0],
                  [1,0,0,0,0,0,0,1]],nums,lis)
                pygame.draw.circle(screen,(0,0,255),(int(nums[0]/2),int(nums[1]/2)),50,0)                
    elif move_key == "K":
        if lis[1] < 8:
            if maze[lis[1]][lis[0]-1] == 0:
                lis[1] -= 1
                board([[1,1,1,1,0,1,1,0],
                  [1,0,0,0,0,0,1,0],
                  [1,0,1,1,0,1,1,0],
                  [1,0,1,1,0,1,1,0],
                  [1,0,1,0,0,0,0,0],
                  [0,0,1,1,0,1,1,1],
                  [1,0,1,1,1,1,0,0],
                  [1,0,0,0,0,0,0,1]],nums,lis)
                pygame.draw.circle(screen,(0,0,255),(int(nums[0]/2),int(nums[1]/2)),50,0)
    elif move_key == "J":
        if lis[0] > 1:
            if maze[lis[1]-1][lis[0]-2] == 0:
                lis[0] += 1
                board([[1,1,1,1,0,1,1,0],
                  [1,0,0,0,0,0,1,0],
                  [1,0,1,1,0,1,1,0],
                  [1,0,1,1,0,1,1,0],
                  [1,0,1,0,0,0,0,0],
                  [0,0,1,1,0,1,1,1],
                  [1,0,1,1,1,1,0,0],
                  [1,0,0,0,0,0,0,1]],nums,lis)
                pygame.draw.circle(screen,(0,0,255),(int(nums[0]/2),int(nums[1]/2)),50,0)
    elif move_key == "L":
        if lis[0] < 8:
            if maze[lis[1]-1][lis[0]] == 0:
                lis[0] -= 1
                board([[1,1,1,1,0,1,1,0],
                  [1,0,0,0,0,0,1,0],
                  [1,0,1,1,0,1,1,0],
                  [1,0,1,1,0,1,1,0],
                  [1,0,1,0,0,0,0,0],
                  [0,0,1,1,0,1,1,1],
                  [1,0,1,1,1,1,0,0],
                  [1,0,0,0,0,0,0,1]],nums,lis)
                pygame.draw.circle(screen,(0,0,255),(int(nums[0]/2),int(nums[1]/2)),50,0)
    pygame.display.update()        
    return [lis]

board([[1,1,1,1,0,1,1,0],
  [1,0,0,0,0,0,1,0],
  [1,0,1,1,0,1,1,0],
  [1,0,1,1,0,1,1,0],
  [1,0,1,0,0,0,0,0],
  [0,0,1,1,0,1,1,1],
  [1,0,1,1,1,1,0,0],
  [1,0,0,0,0,0,0,1]],nums,[8,1])
#main([8,1],nums)
