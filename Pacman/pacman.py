import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 560
SCREEN_HEIGHT = 620
CELL_SIZE = 20
FPS = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

font = pygame.font.SysFont('Arial', 18)

board = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#o####.#####.##.#####.####o#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "######.##### ## #####.######",
    "######.##          ##.######",
    "######.## ###--### ##.######",
    "######.## #      # ##.######",
    "       ## #      # ##       ",
    "######.## #      # ##.######",
    "######.## ######## ##.######",
    "######.##          ##.######",
    "######.## ######## ##.######",
    "######.## ######## ##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#o..##................##..o#",
    "###.##.##.########.##.##.###",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################"
]

# Initialize variables
pacman_x, pacman_y = 13, 23  # Starting position of Pac-Man
pacman_direction = 'LEFT'   # Default direction
score = 0

# Initialize ghost positions
ghosts = [
    {'x': 13, 'y': 11},  # Ghost 1 starting position
    {'x': 14, 'y': 11},  # Ghost 2 starting position
    {'x': 13, 'y': 12},  # Ghost 3 starting position
    {'x': 14, 'y': 12}   # Ghost 4 starting position
]

# Load assets
pacman_img = pygame.image.load('Pacman/assets/pacman.png')
ghost_imgs = [
    pygame.image.load('Pacman/assets/yellow.png'),
    pygame.image.load('Pacman/assets/red.png'),
    pygame.image.load('Pacman/assets/blue.png'),
    pygame.image.load('Pacman/assets/green.png')
]

pacman_img = pygame.transform.scale(pacman_img, (CELL_SIZE, CELL_SIZE))
for i in range(len(ghost_imgs)):
    ghost_imgs[i] = pygame.transform.scale(ghost_imgs[i], (CELL_SIZE, CELL_SIZE))


def draw_board():
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == '#':
                pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == '.':
                pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 3)
            elif cell == 'o':
                pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 7)

def draw_pacman():
    screen.blit(pacman_img, (pacman_x * CELL_SIZE, pacman_y * CELL_SIZE))

def draw_ghosts():
    for i, ghost in enumerate(ghosts):
        screen.blit(ghost_imgs[i], (ghost['x'] * CELL_SIZE, ghost['y'] * CELL_SIZE))

def move_pacman():
    global pacman_x, pacman_y, score
    if pacman_direction == 'LEFT' and board[pacman_y][pacman_x - 1] != '#':
        pacman_x -= 1
    elif pacman_direction == 'RIGHT' and board[pacman_y][pacman_x + 1] != '#':
        pacman_x += 1
    elif pacman_direction == 'UP' and board[pacman_y - 1][pacman_x] != '#':
        pacman_y -= 1
    elif pacman_direction == 'DOWN' and board[pacman_y + 1][pacman_x] != '#':
        pacman_y += 1
    
    if board[pacman_y][pacman_x] == '.':
        board[pacman_y] = board[pacman_y][:pacman_x] + ' ' + board[pacman_y][pacman_x + 1:]
        score += 10
    elif board[pacman_y][pacman_x] == 'o':
        board[pacman_y] = board[pacman_y][:pacman_x] + ' ' + board[pacman_y][pacman_x + 1:]
        score += 50

def move_ghosts():
    for ghost in ghosts:
        direction = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])
        if direction == 'LEFT' and board[ghost['y']][ghost['x'] - 1] != '#':
            ghost['x'] -= 1
        elif direction == 'RIGHT' and board[ghost['y']][ghost['x'] + 1] != '#':
            ghost['x'] += 1
        elif direction == 'UP' and board[ghost['y'] - 1][ghost['x']] != '#':
            ghost['y'] -= 1
        elif direction == 'DOWN' and board[ghost['y'] + 1][ghost['x']] != '#':
            ghost['y'] += 1

def check_collisions():
    for ghost in ghosts:
        if ghost['x'] == pacman_x and ghost['y'] == pacman_y:
            return True
    return False

def check_all_pellets_eaten():
    for row in board:
        if '.' in row or 'o' in row:
            return False
    return True

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                pacman_direction = 'RIGHT'
            elif event.key == pygame.K_UP:
                pacman_direction = 'UP'
            elif event.key == pygame.K_DOWN:
                pacman_direction = 'DOWN'

    move_pacman()
    move_ghosts()

    if check_collisions():
        print("Game Over!")
        running = False

    if check_all_pellets_eaten():
        print("You Win!")
        running = False

    screen.fill(BLACK)
    draw_board()
    draw_pacman()
    draw_ghosts()

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, SCREEN_HEIGHT - 30))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

