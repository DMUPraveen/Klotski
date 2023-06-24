import pygame
import sys
from time import time
from Klotski_Solver import get_solution
moves = [[5, (1, 0)], [3, (0, 1)], [6, (-1, 0)], [4, (0, 1)], [7, (1, 0)], [8, (0, -1)], [8, (-1, 0)], [7, (-1, 0)], [4, (0, -1)], [6, (1, 0)], [5, (1, 0)], [3, (1, 0)], [8, (0, 1)], [7, (-1, 0)], [8, (0, 1)], [9, (0, -1)], [5, (0, -1)], [6, (-1, 0)], [4, (0, 1)], [9, (1, 0)], [7, (1, 0)], [1, (0, 1)], [1, (0, 1)], [0, (-1, 0)], [2, (-1, 0)], [9, (0, -1)], [4, (0, -1)], [6, (1, 0)], [9, (0, -1)], [4, (0, -1)], [5, (1, 0)], [3, (1, 0)], [8, (1, 0)], [1, (0, 1)], [7, (-1, 0)], [3, (0, -1)], [6, (-1, 0)], [8, (0, -1)], [6, (-1, 0)], [3, (0, 1)], [2, (0, 1)], [9, (-1, 0)], [4, (0, -1)], [5, (0, -1)], [3, (1, 0)], [2, (0, 1)], [2, (0, 1)], [5, (-1, 0)], [5, (0, -1)], [7, (1, 0)], [1, (0, -1)], [6, (-1, 0)], [7, (1, 0)], [8, (0, 1)], [1, (1, 0)], [6, (0, -1)], [8, (-1, 0)],
         [1, (0, 1)], [7, (-1, 0)], [4, (0, 1)], [7, (-1, 0)], [2, (0, -1)], [9, (1, 0)], [5, (0, -1)], [2, (0, -1)], [1, (1, 0)], [6, (1, 0)], [6, (0, 1)], [7, (0, 1)], [0, (0, 1)], [5, (-1, 0)], [5, (-1, 0)], [9, (-1, 0)], [4, (0, -1)], [3, (0, -1)], [9, (-1, 0)], [2, (0, -1)], [1, (0, -1)], [6, (1, 0)], [6, (1, 0)], [8, (1, 0)], [8, (1, 0)], [7, (0, 1)], [0, (0, 1)], [5, (0, 1)], [9, (-1, 0)], [2, (-1, 0)], [1, (0, -1)], [1, (0, -1)], [0, (1, 0)], [5, (0, 1)], [5, (0, 1)], [9, (0, 1)], [9, (0, 1)], [2, (-1, 0)], [1, (-1, 0)], [4, (-1, 0)], [3, (0, -1)], [3, (0, -1)], [0, (1, 0)], [5, (1, 0)], [5, (0, -1)], [7, (0, -1)], [8, (-1, 0)], [6, (-1, 0)], [8, (-1, 0)], [6, (-1, 0)], [0, (0, 1)], [5, (1, 0)], [5, (1, 0)], [9, (1, 0)], [9, (1, 0)], [7, (0, -1)], [6, (0, -1)], [6, (-1, 0)]]
moves = [[5, (1, 0)], [3, (0, 1)], [6, (-1, 0)], [4, (0, 1)], [7, (1, 0)], [8, (0, -1)], [8, (-1, 0)], [7, (-1, 0)], [4, (0, -1)], [6, (1, 0)], [5, (1, 0)], [3, (1, 0)], [8, (0, 1)], [7, (-1, 0)], [8, (0, 1)], [9, (0, -1)], [5, (0, -1)], [6, (-1, 0)], [4, (0, 1)], [9, (1, 0)], [7, (1, 0)], [1, (0, 1)], [1, (0, 1)], [0, (-1, 0)], [2, (-1, 0)], [9, (0, -1)], [4, (0, -1)], [6, (1, 0)], [9, (0, -1)], [4, (0, -1)], [5, (1, 0)], [3, (1, 0)], [8, (1, 0)], [1, (0, 1)], [7, (-1, 0)], [3, (0, -1)], [6, (-1, 0)], [8, (0, -1)], [6, (-1, 0)], [3, (0, 1)], [2, (0, 1)], [9, (-1, 0)], [4, (0, -1)], [5, (0, -1)], [3, (1, 0)], [2, (0, 1)], [2, (0, 1)], [5, (-1, 0)], [5, (0, -1)], [7, (1, 0)], [1, (0, -1)], [6, (-1, 0)], [7, (1, 0)], [8, (0, 1)], [1, (1, 0)], [6, (0, -1)], [8, (-1, 0)], [1, (0, 1)], [7, (-1, 0)], [4, (0, 1)], [7, (-1, 0)], [2, (0, -1)], [9, (1, 0)], [5, (0, -1)], [2, (0, -1)], [1, (1, 0)], [6, (1, 0)], [6, (0, 1)], [7, (0, 1)], [0, (0, 1)], [5, (-1, 0)], [5, (-1, 0)], [9, (-1, 0)], [4, (0, -1)], [3, (0, -1)], [9, (-1, 0)], [2, (0, -1)], [1, (0, -1)], [6, (1, 0)], [6, (1, 0)], [8, (1, 0)], [8, (1, 0)], [7, (0, 1)], [0, (0, 1)], [5, (0, 1)], [9, (-1, 0)], [2, (-1, 0)], [1, (0, -1)], [1, (0, -1)], [0, (1, 0)], [5, (0, 1)], [5, (0, 1)], [9, (0, 1)], [9, (0, 1)], [2, (-1, 0)], [1, (-1, 0)], [4, (-1, 0)], [3, (0, -1)], [3, (0, -1)], [0, (1, 0)], [5, (1, 0)], [5, (0, -1)], [7, (0, -1)], [8, (-1, 0)], [6, (-1, 0)], [8, (-1, 0)], [6, (-1, 0)], [0, (0, 1)], [5, (1, 0)], [5, (1, 0)], [9, (1, 0)], [9, (1, 0)], [7, (0, -1)], [6, (0, -1)], [6, (-1, 0)], [0, (-1, 0)]]
screen_height = 400
screen_width = 400

pygame.init()
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('Klotski')


tile_size = 50
board_width = 4 * tile_size
board_height = 5 * tile_size
origin = ((400-board_width)/2, (400-board_height)/2)

board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


def draw_tile(pos):
    color = (255, 255, 255)
    position = (origin[0]+pos[0]*tile_size, origin[1]+pos[1]*tile_size)
    pygame.draw.rect(
        screen, color, (position[0], position[1], tile_size, tile_size), 1)


def fill_tile(pos, color):
    position = (origin[0]+pos[0]*tile_size, origin[1]+pos[1]*tile_size)
    pygame.draw.rect(
        screen, color, (position[0], position[1], tile_size, tile_size))


def draw_block(pos, size, color, thikness=1):
    rect = (origin[0]+pos[0]*tile_size, origin[1]+pos[1] *
            tile_size, size[0]*tile_size, size[1]*tile_size)
    pygame.draw.rect(screen, color, rect, thikness)


def draw_grid():
    for i in range(0, 4):
        for j in range(0, 5):
            draw_tile((i, j))


draw_grid()


class block:
    def __init__(self, pos, size, color, board):
        global blocks
        self.pos = pos
        self.size = size
        self.color = color
        self.fill_board(board)
        blocks.append(self)

    def draw(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                fill_tile((self.pos[0]+i, self.pos[1]+j), self.color)

    def fill_board(self, board):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                board[j+self.pos[1]][i+self.pos[0]] = 1

    def clear_board(self, board):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                board[j+self.pos[1]][i+self.pos[0]] = 0

    def move(self, direction, board):
        self.clear_board(board)
        self.pos[0] += direction[0]
        self.pos[1] += direction[1]

        if(self.pos[0]+self.size[0] > 4 or self.pos[1]+self.size[1] > 5 or self.pos[0] < 0 or self.pos[1] < 0):
            print("out of bounds")
            self.pos[0] -= direction[0]
            self.pos[1] -= direction[1]
            self.fill_board(board)
            return False
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if(board[j+self.pos[1]][i+self.pos[0]] == 1):
                    print("blocked")
                    self.pos[0] -= direction[0]
                    self.pos[1] -= direction[1]
                    self.fill_board(board)
                    return False
        self.fill_board(board)
        # update_display()
        # print_board(board)
        return True

    def is_in_box(self, x, y):
        tile_x = (x - origin[0])/tile_size
        tile_y = (y - origin[1])/tile_size
        if(self.pos[0] < tile_x and self.pos[1] < tile_y and self.pos[0] + self.size[0] > tile_x and self.pos[1]+self.size[1] > tile_y):
            return True
        else:
            return False


def update_display():
    screen.fill((0, 0, 0))
    draw_grid()
    for block in blocks:
        block.draw()
        draw_block(block.pos, block.size, (255, 255, 255))
    # pygame.display.update()


def print_board(board):
    for row in board:
        print(row)


red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
blocks = []
a = block([1, 0], (2, 2), red, board)
b = block([0, 0], (1, 2), blue, board)
c = block([3, 0], (1, 2), blue, board)
d = block([0, 2], (1, 2), blue, board)
e = block([3, 2], (1, 2), blue, board)
f = block([0, 4], (1, 1), green, board)
e = block([3, 4], (1, 1), green, board)
g = block([1, 2], (2, 1), blue, board)
h = block([1, 3], (1, 1), green, board)
i = block([2, 3], (1, 1), green, board)
update_display()
right = (1, 0)
left = (-1, 0)
down = (0, 1)
up = (0, -1)





def game():
    
    Running = True
    selected_block = None
    while Running:

        update_display()
        if(selected_block != None):
            draw_block(blocks[selected_block].pos,
                    blocks[selected_block].size, (255, 255, 0), 2)

        mouse = (0, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = event.pos
                for ids, block in enumerate(blocks):

                    if(block.is_in_box(mouse[0], mouse[1])):

                        selected_block = ids

                        break
            if event.type == pygame.KEYDOWN and selected_block != None:
                if(event.key == pygame.K_DOWN):
                    blocks[selected_block].move(down, board)
                if(event.key == pygame.K_RIGHT):
                    blocks[selected_block].move(right, board)
                if(event.key == pygame.K_LEFT):
                    blocks[selected_block].move(left, board)
                if(event.key == pygame.K_UP):
                    blocks[selected_block].move(up, board)
                if(event.key == pygame.K_a):
                    auto_matic_game()
        pygame.display.update()

    pygame.quit()
    sys.exit()


def auto_matic_game():
    Running  = True
    t = time()
    index = 0
    now_board = [block.pos for block in blocks]
    moves = get_solution(now_board)
    while Running:
        update_display()
        if(time() -t > 0.1 ):
            if(index == len(moves)):
                index = 0
                break
            move = moves[index]
            blocks[move[0]].move(move[1],board)
            t = time()
            index +=1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
                break
        pygame.display.update()
  


        
'''
Running = True
while Running:
    pygame.display.update()
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           Running = False
           break

pygame.quit()
sys.exit()
'''
if __name__ == "__main__":
    game()
    #auto_matic_game()
    