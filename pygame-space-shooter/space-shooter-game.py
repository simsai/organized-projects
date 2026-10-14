import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Shooter")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
BROWN = (139, 69, 19)

# Player
player_size = 30
player_x = width // 2
player_y = height - player_size - 10
player_speed = 5
player_health = 100
player_damage = 15  # Increased by 1.5x
player_shoot_delay = 30
player_bullet_spread = 15  # Minimum bullet spread
player_bullet_count = 5  # Minimum bullet count

# Enemy types
enemy_types = [
    {"color": RED, "health": 30, "speed": 2, "bullet_speed": 5, "shoot_delay": 60, "bullets": 1, "spread": 0},
    {"color": BLUE, "health": 50, "speed": 1, "bullet_speed": 7, "shoot_delay": 90, "bullets": 2, "spread": 15},
    {"color": YELLOW, "health": 40, "speed": 3, "bullet_speed": 6, "shoot_delay": 75, "bullets": 3, "spread": 30}
]

# Bullets
bullet_width = 5
bullet_height = 15
bullet_speed = 7
bullets = []
enemy_bullets = []

# Power-ups
power_ups = []
HEALTH_POWERUP = 0
DAMAGE_POWERUP = 1
SPEED_POWERUP = 2
SHIELD_POWERUP = 3
RAPID_FIRE_POWERUP = 4
SPREAD_SHOT_POWERUP = 5
powerup_duration = 5 * 60  # 5 seconds at 60 FPS
damage_multiplier = 1
speed_multiplier = 1
SHIELD_POWERUP = 3
powerup_duration = 5 * 60  # 5 seconds at 60 FPS for other power-ups
shield_duration = 3 * 60  # 3 seconds at 60 FPS for shield

rapid_fire_active = False
spread_shot_active = False

# Game variables
enemies = []
score = 0
frame_count = 0
spread_change_timer = 0
game_state = "menu"
paused = False
shield_active = False
shield_timer = 0

# Helper functions
def create_enemy():
    enemy_type = random.choice(enemy_types)
    return {
        'x': random.randint(0, width - player_size),
        'y': 0,
        'type': enemy_type,
        'health': enemy_type['health']
    }

def draw_triangle(surface, color, x, y, size, direction="up"):
    if direction == "up":
        points = [(x, y + size), (x + size, y + size), (x + size // 2, y)]
    else:  # down
        points = [(x, y), (x + size, y), (x + size // 2, y + size)]
    pygame.draw.polygon(surface, color, points)

def spawn_powerup():
    powerup_type = random.choice([HEALTH_POWERUP, DAMAGE_POWERUP, SPEED_POWERUP, SHIELD_POWERUP, RAPID_FIRE_POWERUP, SPREAD_SHOT_POWERUP])
    return {
        'x': random.randint(0, width - player_size),
        'y': random.randint(0, height // 2),
        'type': powerup_type,
        'timer': 5 * 60  # 5 seconds at 60 FPS
    }

def draw_text(surface, text, size, x, y, color=WHITE):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def show_menu():
    window.fill(BLACK)
    draw_text(window, "Space Shooter", 64, width // 2, height // 4)
    draw_text(window, "Press P to Play", 32, width // 2, height // 2)
    draw_text(window, "Press I for Instructions", 32, width // 2, height // 2 + 50)
    pygame.display.flip()

def show_instructions():
    window.fill(BLACK)
    instructions = [
        "Player Controls:",
        "- WASD keys to move",
        "- Automatically shoot bullets",
        "- Bullet spread and count changes every 20 seconds",
        "",
        "Enemy Types:",
        "- Red: Fast, low health, single bullet",
        "- Blue: Slow, high health, two bullets",
        "- Yellow: Medium speed, three bullets",
        "",
        "Power-ups:",
        "- Purple: Restore 50% health (Health)",
        "- Green: 2x damage for 5 seconds (Damage)",
        "- Cyan: Increased speed for 5 seconds (Speed)",
        "- Orange: Temporary shield (Shield)",
        "- Pink: Increased fire rate for 5 seconds (Rapid Fire)",
        "- Brown: Wider bullet spread for 5 seconds (Spread Shot)",
        "",
        "Press B to return to menu"
    ]
    for i, line in enumerate(instructions):
        draw_text(window, line, 24, width // 2, height // 10 + i * 30)
    pygame.display.flip()

def show_game_over():
    window.fill(BLACK)
    draw_text(window, "GAME OVER", 64, width // 2, height // 4)
    draw_text(window, f"Score: {score}", 32, width // 2, height // 2)
    draw_text(window, "Press P to Play Again", 32, width // 2, height // 2 + 50)
    pygame.display.flip()

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    if game_state == "menu":
        show_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_state = "game"
                    # Reset game variables
                    score = 0
                    player_health = 100
                    enemies = []
                    bullets = []
                    enemy_bullets = []
                    power_ups = []
                    frame_count = 0
                    spread_change_timer = 0
                    damage_multiplier = 1
                    speed_multiplier = 1
                    shield_active = False
                    rapid_fire_active = False
                    spread_shot_active = False
                elif event.key == pygame.K_i:
                    game_state = "instructions"

    elif game_state == "instructions":
        show_instructions()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_state = "menu"

    elif game_state == "game":
        frame_count += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused

        if paused:
            draw_text(window, "PAUSED", 64, width // 2, height // 2)
            pygame.display.flip()
            continue

        # Player shooting
        shoot_delay = player_shoot_delay
        if rapid_fire_active:
            shoot_delay //= 2
        if frame_count % shoot_delay == 0:
            bullet_spread = player_bullet_spread
            if spread_shot_active:
                bullet_spread *= 2
            for i in range(player_bullet_count):
                angle = math.radians(random.uniform(-bullet_spread, bullet_spread))
                dx = math.sin(angle) * bullet_speed
                dy = -math.cos(angle) * bullet_speed
                bullets.append([player_x + player_size // 2, player_y, dx, dy])

        # Move player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_x > 0:
            player_x -= player_speed * speed_multiplier
        if keys[pygame.K_d] and player_x < width - player_size:
            player_x += player_speed * speed_multiplier
        if keys[pygame.K_w] and player_y > 0:
            player_y -= player_speed * speed_multiplier
        if keys[pygame.K_s] and player_y < height - player_size:
            player_y += player_speed * speed_multiplier

        # Spawn enemies
        enemy_spawn_rate = 0.02 + score * 0.001  # Increase spawn rate with score
        if len(enemies) < 10 and random.random() < enemy_spawn_rate:
            enemies.append(create_enemy())

        # Spawn power-ups
        if random.random() < 0.001:  # Adjust this value to change power-up frequency
            power_ups.append(spawn_powerup())

        # Move and manage enemies
        for enemy in enemies[:]:  # Iterate over a copy of the list
            enemy['y'] += enemy['type']['speed']
            if enemy['y'] > height:
                enemies.remove(enemy)
            
            # Enemy shooting
            if frame_count % enemy['type']['shoot_delay'] == 0:
                for i in range(enemy['type']['bullets']):
                    angle = math.radians(enemy['type']['spread'] * (i - (enemy['type']['bullets'] - 1) / 2))
                    dx = math.sin(angle) * enemy['type']['bullet_speed']
                    dy = math.cos(angle) * enemy['type']['bullet_speed']
                    enemy_bullets.append([enemy['x'] + player_size // 2, enemy['y'] + player_size, dx, dy])

        # Move bullets
        for bullet in bullets[:]:
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]
            if bullet[1] < 0 or bullet[0] < 0 or bullet[0] > width:
                bullets.remove(bullet)

        for bullet in enemy_bullets[:]:
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]
            if bullet[1] > height or bullet[0] < 0 or bullet[0] > width:
                enemy_bullets.remove(bullet)

# ... (rest of the code)

        # Check for collisions
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

        enemies_to_remove = []  # List to store enemies marked for removal

        for enemy in enemies[:]:  # Iterate over a copy of the list
            enemy_rect = pygame.Rect(enemy['x'], enemy['y'], player_size, player_size)

            # Player-enemy collision
            if player_rect.colliderect(enemy_rect):
                if not shield_active:
                    game_state = "game_over"
                elif shield_active:
                    enemies.remove(enemy)
                    shield_active = False
                else:
                   game_state = "game_over"

            for bullet in bullets[:]:
                bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
                if enemy_rect.colliderect(bullet_rect):
                    bullets.remove(bullet)
                    enemy['health'] -= player_damage * damage_multiplier
                    if enemy['health'] <= 0:
                        enemies_to_remove.append(enemy)  # Mark for removal
                        score += 1 

        for bullet in enemy_bullets[:]:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
            if player_rect.colliderect(bullet_rect):
                if not shield_active:
                    enemy_bullets.remove(bullet)
                    player_health -= 10
                    if player_health <= 0:
                        game_state = "game_over"
                else:  # If shield is active
                    shield_active=False
                    
                    enemy_bullets.remove(bullet)



        # Remove marked enemies
        for enemy in enemies_to_remove:
            if enemy in enemies:  # Check if enemy still exists
                enemies.remove(enemy)

        # ... (rest of the code)

        # Check for power-up collisions
        for power_up in power_ups[:]:
            power_up_rect = pygame.Rect(power_up['x'], power_up['y'], player_size, player_size)
            if player_rect.colliderect(power_up_rect):
                if power_up['type'] == HEALTH_POWERUP:
                    player_health = min(100, player_health + 50)
                elif power_up['type'] == DAMAGE_POWERUP:
                    damage_multiplier = 2
                elif power_up['type'] == SPEED_POWERUP:
                    speed_multiplier = 2
                elif power_up['type'] == SHIELD_POWERUP:
                    shield_active = True
                    shield_timer = shield_duration  # Reset shield timer
                elif power_up['type'] == RAPID_FIRE_POWERUP:
                    rapid_fire_active = True
                elif power_up['type'] == SPREAD_SHOT_POWERUP:
                    spread_shot_active = True
                power_up['timer'] = powerup_duration
                power_ups.remove(power_up)

        # Update power-ups
        for power_up in power_ups[:]:
            power_up['timer'] -= 1
            if power_up['timer'] <= 0:
                if power_up['type'] == DAMAGE_POWERUP:
                    damage_multiplier = 1
                elif power_up['type'] == SPEED_POWERUP:
                    speed_multiplier = 1
                elif power_up['type'] == SHIELD_POWERUP:
                    shield_active = False
                elif power_up['type'] == RAPID_FIRE_POWERUP:
                    rapid_fire_active = False
                elif power_up['type'] == SPREAD_SHOT_POWERUP:
                    spread_shot_active = False
                power_ups.remove(power_up)


        if shield_active:
            shield_timer -= 1
            if shield_timer <= 0:
                shield_active = False

        # Change bullet spread and count
        spread_change_timer += 1
        if spread_change_timer >= 20 * 60:  # 20 seconds at 60 FPS
            player_bullet_count = random.randint(3, 10)  # Number of bullets: 3-10
            player_bullet_spread = player_bullet_count * 5  # Spread proportional to bullet count
            spread_change_timer = 0

        # Draw everything
        window.fill(BLACK)
        draw_triangle(window, WHITE, player_x, player_y, player_size)
        
        # Draw player health bar
        pygame.draw.rect(window, RED, (player_x, player_y - 10, player_size, 5))
        pygame.draw.rect(window, GREEN, (player_x, player_y - 10, player_size * (player_health / 100), 5))

        # Draw shield
        if shield_active:
            pygame.draw.circle(window, ORANGE, (player_x + player_size // 2, player_y + player_size // 2), player_size // 2 + 5, 2)

        for enemy in enemies:
            draw_triangle(window, enemy['type']['color'], enemy['x'], enemy['y'], player_size, "down")
            # Draw enemy health bar
            pygame.draw.rect(window, RED, (enemy['x'], enemy['y'] - 10, player_size, 5))
            pygame.draw.rect(window, GREEN, (enemy['x'], enemy['y'] - 10, player_size * (enemy['health'] / enemy['type']['health']), 5))

        for bullet in bullets:
            pygame.draw.rect(window, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))

        for bullet in enemy_bullets:
            pygame.draw.rect(window, RED, (bullet[0], bullet[1], bullet_width, bullet_height))

        for power_up in power_ups:
            color = {
                HEALTH_POWERUP: PURPLE,
                DAMAGE_POWERUP: GREEN,
                SPEED_POWERUP: CYAN,
                SHIELD_POWERUP: ORANGE,
                RAPID_FIRE_POWERUP: PINK,
                SPREAD_SHOT_POWERUP: BROWN
            }[power_up['type']]
            pygame.draw.rect(window, color, (power_up['x'], power_up['y'], player_size, player_size))
            # Draw power-up name
            power_up_name = {
                HEALTH_POWERUP: "Health",
                DAMAGE_POWERUP: "Damage",
                SPEED_POWERUP: "Speed",
                SHIELD_POWERUP: "Shield",
                RAPID_FIRE_POWERUP: "Rapid Fire",
                SPREAD_SHOT_POWERUP: "Spread Shot"
            }[power_up['type']]
            draw_text(window, power_up_name, 12, power_up['x'] + player_size // 2, power_up['y'] + player_size // 2, BLACK)

        # Draw score
        draw_text(window, f"Score: {score}", 36, width - 100, 10)

        pygame.display.flip()
        clock.tick(60)

    elif game_state == "game_over":
        show_game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_state = "game"
                    # Reset game variables
                    score = 0
                    player_health = 100
                    enemies = []
                    bullets = []
                    enemy_bullets = []
                    power_ups = []
                    frame_count = 0
                    spread_change_timer = 0
                    damage_multiplier = 1
                    speed_multiplier = 1
                    shield_active = False
                    rapid_fire_active = False
                    spread_shot_active = False

pygame.quit()