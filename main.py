import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("미로 탈출 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# 미로 생성 (간단한 배열 예시)
maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]

# 플레이어 설정
player_x, player_y = 1, 1
cell_size = 100

# 게임 루프
running = True
while running:
    screen.fill(WHITE)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and maze[player_y - 1][player_x] == 0:
                player_y -= 1
            elif event.key == pygame.K_DOWN and maze[player_y + 1][player_x] == 0:
                player_y += 1
            elif event.key == pygame.K_LEFT and maze[player_y][player_x - 1] == 0:
                player_x -= 1
            elif event.key == pygame.K_RIGHT and maze[player_y][player_x + 1] == 0:
                player_x += 1

    # 미로 그리기
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            color = BLACK if maze[row][col] == 1 else WHITE
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

    # 플레이어 그리기
    pygame.draw.rect(screen, BLUE, (player_x * cell_size, player_y * cell_size, cell_size, cell_size))

    pygame.display.flip()

# 게임 종료
pygame.quit()
