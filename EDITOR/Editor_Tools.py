import pygame
import Maze_ver_2_Beta_1

load = Maze_ver_2_Beta_1.main

maze = [[0,0,0],
        [1,1,0],
        [2,0,0]]

#player_x = int(input("Enter your player's x pos: "))
#player_y = int(input("Enter your player's y pos: "))

#win_x = int(input("Enter your window's x size: "))
#win_y = int(input("Enter your window's y size: "))

#bound = int(input("Enter your boundary (biggest length): "))

load([-1,-1],(1600,800),-3,maze)

maze = [[1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1]]
        
