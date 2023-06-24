class block:
    def __init__(self, pos, size, board):
        global blocks
        self.pos = pos
        self.size = size
        #self.color = color
        self.fill_board(board)
        blocks.append(self)

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
            #print("out of bounds")
            self.pos[0] -= direction[0]
            self.pos[1] -= direction[1]
            self.fill_board(board)
            return False
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if(board[j+self.pos[1]][i+self.pos[0]] == 1):
                    # print("blocked")
                    self.pos[0] -= direction[0]
                    self.pos[1] -= direction[1]
                    self.fill_board(board)
                    return False
        self.fill_board(board)
        return True


def print_board(board):
    for row in board:
        print(row)
    print("")


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
blocks = []


class Game:
    board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
    ]

    a = block([1, 0], (2, 2), board)
    b = block([0, 0], (1, 2), board)
    c = block([3, 0], (1, 2), board)
    d = block([0, 2], (1, 2), board)
    e = block([3, 2], (1, 2), board)
    f = block([0, 4], (1, 1), board)
    g = block([3, 4], (1, 1), board)
    h = block([1, 2], (2, 1), board)
    i = block([1, 3], (1, 1), board)
    j = block([2, 3], (1, 1), board)

    def get_valid_directions(self, block):
        valid_directions = []
        for direction in directions:
            if(block.move(direction, self.board)):
                # print("found")
                block.move((-direction[0], -direction[1]), self.board)
                valid_directions.append(direction)
        return valid_directions

    def clear_board(self):
        for i in range(0, 5):
            for j in range(0, 4):
                self.board[i][j] = 0

    def get_valid_moves(self):
        valid_moves = []
        for index, block in enumerate(blocks):
            # print(index)
            directions = self.get_valid_directions(block)
            for direction in directions:
                valid_moves.append([index, direction])
        # print_board(self.board)
        return valid_moves

    def do_move(self, block_id, direction):
        blocks[block_id].move(direction, self.board)

    def return_board(self):
        this_board = []
        for block in blocks:
            this_board.append([block.pos[0], block.pos[1]])
        return this_board

    def print(self):
        print_board(self.board)

    def set_game(self, board):
        self.clear_board()
        for index, pos in enumerate(board):
            blocks[index].pos = [pos[0], pos[1]]
            blocks[index].fill_board(self.board)


game = Game()


current = []
#visited = []

current.append([game.return_board(),[]])
#visited.append([game.return_board(),[]])

next_b = []


def solver():
    global current
    global next_b
    for board in current:
        game.set_game(board)
        moves = game.get_valid_moves()
        for move in moves:
            game.set_game(board)
            game.do_move(move[0], move[1])
            new_board = game.return_board()
            if(new_board not in visited)  and (new_board not in next_b):
                visited.append(new_board)
                next_b.append(new_board)

            if(new_board[0] == [1, 2]):
                print(new_board)
                return True

    current = [i for i in next_b]
    next_b = []

    return False


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

def get_index(pos):
    return pos[0]+pos[1]*4

def improved_hasher(board):
    hashed = ""
    hashed += str(get_index(board[0])) + " "
    hashed += str(get_index(board[7])) + " "
    value = primes[get_index(board[1])]*primes[get_index(board[2])]*primes[get_index(board[3])]*primes[get_index(board[4])]
    hashed += str(value) + " "
    value = primes[get_index(board[5])]*primes[get_index(board[6])]*primes[get_index(board[8])]*primes[get_index(board[9])]
    hashed += str(value) + " "
    return hashed

        

def board_hasher(board):
    hashed = ""
    for info in board:
        hashed  += str(info[0]+info[1]*4)
    return hashed

hashed_visited = {}
#hashed_visited[board_hasher(game.return_board())] = 1

hashed_visited[improved_hasher(game.return_board())] = 1
solution = []
def hashed_solver():
    global current
    global next_b
    global solution
    for board,move_stack in current:
        game.set_game(board)
        moves = game.get_valid_moves()
        for move in moves:
            game.set_game(board)
            game.do_move(move[0], move[1])
            new_board = game.return_board()
            #hashed = board_hasher(new_board)
            hashed = improved_hasher(new_board)
            if(hashed not in hashed_visited):

                hashed_visited[hashed] = 1
                new_stack = [i for i in move_stack]

                new_stack.append(move)
                next_b.append([new_board,new_stack])

            if(new_board[0] == [1,3]):
                move_stack.append(move)
                #print(new_board,move_stack)
                solution = move_stack
                #print(len(move_stack))
                return True
    
    current = [i for i in next_b]
    
    next_b = []

    return False


def main():
    global current
    global next_b
    global hashed_visited
    current = []
    next_b = []
    hashed_visited = {}

    current.append([game.return_board(),[]])
    hashed_visited[improved_hasher(game.return_board())] = 1
    #visited.append([game.return_board(),[]])
    n = 0
    while(not hashed_solver()):
        pass
        n= n+1
        #print(n)
    print("done in",n,"steps")
    print(solution)

def get_solution(board):
    game.set_game(board)
    global current
    global next_b
    global hashed_visited
    current = []
    next_b = []
    hashed_visited = {}

    current.append([game.return_board(),[]])
    hashed_visited[improved_hasher(game.return_board())] = 1
    #visited.append([game.return_board(),[]])
    #n = 0
    while(not hashed_solver()):
        #n= n+1
        #print(n)
        pass
    return solution
if __name__ == "__main__":
    main()