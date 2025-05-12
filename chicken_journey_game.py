
import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FONT = pygame.font.SysFont("Arial", 32)

# Game Variables
difficulty_options = ["Easy", "Medium", "Hard", "Deathtrap"]
multiplier_progression = {
    "Easy": [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 14, 15, 17, 18, 20, 22, 25, 28, 30, 33, 35, 38, 40, 45, 50],
    "Medium": [1, 3, 5, 7, 10, 12, 15, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 80, 90, 100, 110, 120, 150],
    "Hard": [1, 5, 10, 15, 20, 30, 40, 50, 60, 75, 100, 150, 200, 300, 500, 700, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 7000, 10000],
    "Deathtrap": [1, 10, 25, 50, 100, 150, 200, 300, 500, 700, 1000, 1500, 2000, 3000, 5000, 10000, 20000, 30000, 40000, 50000, 75000, 100000, 150000, 200000, 250000]
}

# Initialize the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Journey")

# Function to display text
def display_text(text, font, color, x, y):
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center=(x, y))
    screen.blit(text_surf, text_rect)

# Function to simulate the chicken journey
def play_game(difficulty):
    bet = 1  # Starting bet
    multiplier = 1
    square_count = 25  # Total number of squares to pass
    progression = multiplier_progression[difficulty]
    path = []

    # Randomly determine which direction is the correct one (for now, just simulating)
    for i in range(square_count):
        direction = random.choice(["left", "right"])
        path.append(direction)
    
    survived_squares = 0
    for i in range(square_count):
        if random.random() < 0.8:  # 80% chance to survive (simplified)
            survived_squares += 1
            multiplier = progression[survived_squares - 1]
        else:
            break  # Player dies, lose everything
        
        # Update the screen with the current game status
        screen.fill(WHITE)
        display_text(f"Difficulty: {difficulty}", FONT, BLACK, WIDTH / 2, 50)
        display_text(f"Square: {survived_squares}/{square_count}", FONT, BLACK, WIDTH / 2, 100)
        display_text(f"Current Multiplier: {multiplier}x", FONT, BLACK, WIDTH / 2, 150)
        display_text(f"Bet: ${bet}", FONT, BLACK, WIDTH / 2, 200)
        
        pygame.display.update()
        pygame.time.delay(500)  # Delay to simulate chicken progress

    # If survived all squares, reward multiplier
    if survived_squares == square_count:
        display_text(f"YOU WIN! {multiplier}x your bet", FONT, GREEN, WIDTH / 2, 300)
    else:
        display_text("YOU LOSE!", FONT, RED, WIDTH / 2, 300)
    
    pygame.display.update()
    pygame.time.delay(2000)  # Wait before closing

# Main game loop
def main():
    running = True
    difficulty = None
    
    while running:
        screen.fill(WHITE)
        
        display_text("Welcome to Chicken Journey!", FONT, BLACK, WIDTH / 2, HEIGHT / 4)
        display_text("Select Difficulty: Easy, Medium, Hard, Deathtrap", FONT, BLACK, WIDTH / 2, HEIGHT / 2 - 50)
        
        display_text("Press 1 for Easy, 2 for Medium, 3 for Hard, 4 for Deathtrap", FONT, BLACK, WIDTH / 2, HEIGHT / 2 + 50)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = "Easy"
                    play_game(difficulty)
                elif event.key == pygame.K_2:
                    difficulty = "Medium"
                    play_game(difficulty)
                elif event.key == pygame.K_3:
                    difficulty = "Hard"
                    play_game(difficulty)
                elif event.key == pygame.K_4:
                    difficulty = "Deathtrap"
                    play_game(difficulty)
    
    pygame.quit()
    sys.exit()

# Run the game
if __name__ == "__main__":
    main()
