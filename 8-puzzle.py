import heapq

class PuzzleState:
    def __init__(self, board, empty_pos, moves, cost):
        self.board = board
        self.empty_pos = empty_pos
        self.moves = moves
        self.cost = cost

    def get_possible_moves(self):
        directions = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]
        moves = []
        x, y = self.empty_pos
        for dx, dy, action in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                moves.append((nx, ny, action))
        return moves

    def create_new_state(self, nx, ny, action):
        new_board = [row[:] for row in self.board]
        x, y = self.empty_pos
        new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
        return PuzzleState(new_board, (nx, ny), self.moves + [action], self.cost + 1)

    def __lt__(self, other):
        return self.cost < other.cost

def manhattan_distance(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val == 0:
                continue
            x, y = (val - 1) // 3, (val - 1) % 3
            distance += abs(x - i) + abs(y - j)
    return distance

def solve_8_puzzle(start, goal):
    start_pos = [(i, j) for i in range(3) for j in range(3) if start[i][j] == 0][0]
    goal_state = tuple(tuple(row) for row in goal)
    initial_state = PuzzleState(start, start_pos, [], 0)

    heap = [(manhattan_distance(start), initial_state)]
    visited = set()

    while heap:
        _, current = heapq.heappop(heap)
        if tuple(tuple(row) for row in current.board) == goal_state:
            return current.moves
        visited.add(tuple(tuple(row) for row in current.board))
        for nx, ny, action in current.get_possible_moves():
            new_state = current.create_new_state(nx, ny, action)
            if tuple(tuple(row) for row in new_state.board) not in visited:
                estimate = manhattan_distance(new_state.board) + new_state.cost
                heapq.heappush(heap, (estimate, new_state))
    return None

# Example usage
start_board = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]
goal_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
solution = solve_8_puzzle(start_board, goal_board)
print("Solution moves:", solution)
