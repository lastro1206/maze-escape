import random
import pygame

# 미로 크기 설정 (가로 x 세로)
width, height = 21, 21
# 미로 생성 함수
def create_maze(width, height):
    # 미로 초기화 (1은 벽, 0은 통로)
    maze = [[1 for _ in range(width)] for _ in range(height)]

    # 초기 위치 설정
    start_x, start_y = 1, 1
    maze[start_y][start_x] = 0

    # DFS를 위한 스택
    stack = [(start_x, start_y)]

    # 이동할 방향 (상, 하, 좌, 우)
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]

    while stack:
        x, y = stack[-1]
        random.shuffle(directions)  # 방향을 랜덤하게 섞어줌

        moved = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and maze[ny][nx] == 1:
                # 중간 벽 제거
                maze[y + dy // 2][x + dx // 2] = 0
                maze[ny][nx] = 0
                stack.append((nx, ny))
                moved = True
                break

        if not moved:
            stack.pop()

    return maze

cell_size = 100

# 미로 시각화
def draw_maze(maze):
    pygame.init()
    cell_size = 20
    screen = pygame.display.set_mode((len(maze[0]) * cell_size, len(maze) * cell_size))
    pygame.display.set_caption("Random Maze")
    
    player_x, player_y = 1, 1

    running = True
    while running:
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

        screen.fill((255, 255, 255))  # 흰색 배경

        # 미로 그리기
        for y in range(len(maze)):
            for x in range(len(maze[0])):
                color = (0, 0, 0) if maze[y][x] == 1 else (255, 255, 255)
                pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
        
        pygame.draw.rect(screen, (0, 0, 255), (player_x * cell_size, player_y * cell_size, cell_size, cell_size))

        pygame.display.flip()  # 화면 업데이트

    pygame.quit()

# 미로 생성 및 시각화 실행
maze = create_maze(width, height)
draw_maze(maze)
