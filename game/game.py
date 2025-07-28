import pygame
import sys
from game.ball import Ball
from game.paddle import Paddle
from game.brick import Brick
from game.level_manager import load_level

WIDTH, HEIGHT = 800, 600

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bounce Ball Game - 11 Levels")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)

    level = 1
    score = 0

    paddle = Paddle(WIDTH // 2 - 60, HEIGHT - 30)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 4, -4)
    bricks, ball_speed = load_level(level)
    ball.speed_x, ball.speed_y = ball_speed, -ball_speed

    game_over = False

    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_over and event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                # Check if restart button clicked
                if restart_button.collidepoint(mx, my):
                    # Reset game state
                    level = 1
                    score = 0
                    paddle.reset(WIDTH // 2 - 60)
                    ball.reset(WIDTH // 2, HEIGHT // 2)
                    bricks, ball_speed = load_level(level)
                    ball.speed_x, ball.speed_y = ball_speed, -ball_speed
                    game_over = False

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddle.move(-1)
            if keys[pygame.K_RIGHT]:
                paddle.move(1)

            ball.move()
            ball.check_wall_collision(WIDTH, HEIGHT)

            if paddle.rect.colliderect(ball.rect):
                ball.bounce_y()

            for brick in bricks[:]:
                if brick.rect.colliderect(ball.rect):
                    ball.bounce_y()
                    bricks.remove(brick)
                    score += 10
                    break

            if ball.rect.top > HEIGHT:
                # Ball fell down, game over
                game_over = True

            if not bricks:
                level += 1
                if level > 11:
                    print("🎉 Game Completed!")
                    pygame.quit()
                    sys.exit()
                bricks, ball_speed = load_level(level)
                ball.reset(WIDTH // 2, HEIGHT // 2)
                paddle.reset(WIDTH // 2 - 60)
                ball.speed_x, ball.speed_y = ball_speed, -ball_speed

        # Draw game objects
        paddle.draw(screen)
        ball.draw(screen)
        for brick in bricks:
            brick.draw(screen)

        # Draw score and level
        text = font.render(f"Score: {score} | Level: {level}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        # If game over, draw popup
        if game_over:
            popup_rect = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 - 100, 300, 200)
            pygame.draw.rect(screen, (50, 50, 50), popup_rect)
            pygame.draw.rect(screen, (255, 255, 255), popup_rect, 3)

            msg = font.render("Game Over!", True, (255, 0, 0))
            screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 70))

            score_msg = font.render(f"Your Score: {score}", True, (255, 255, 255))
            screen.blit(score_msg, (WIDTH//2 - score_msg.get_width()//2, HEIGHT//2 - 30))

            # Draw restart button
            restart_button = pygame.Rect(WIDTH//2 - 60, HEIGHT//2 + 20, 120, 40)
            pygame.draw.rect(screen, (0, 128, 0), restart_button)
            button_text = font.render("Restart", True, (255, 255, 255))
            screen.blit(button_text, (restart_button.x + (restart_button.width - button_text.get_width()) // 2,
                                      restart_button.y + (restart_button.height - button_text.get_height()) // 2))

        pygame.display.flip()
        clock.tick(60)
