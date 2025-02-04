# from settings import *

# class Game:
#     def __init__(self):
#         pygame.init()
#         self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#         pygame.display.set_caption('Pong')
#         self.clock = pygame.time.Clock()
#         self.running = True
        
#     def run(self):
#         while self.running:
#             dt = self.clock.tick() / 1000
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.running = False
                    
#             # update

#             # draw
#             pygame.display.update()
#         pygame.quit()
        
# if __name__ == '__main__':
#     game = Game()
#     game.run()

import arcade
import random
import math
import constants



class PongGame(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Pong")
        # Game state
        self.game_state = "MENU"
        
        # Create Text objects for the menu
        self.title_text = arcade.Text(
            "PONG",
            WINDOW_WIDTH / 2,
            WINDOW_HEIGHT * 0.7,
            arcade.color.AMARANTH_PINK,
            50,
            anchor_x="center"
        )
        
        self.instruction_text = arcade.Text(
            "Use UP/DOWN or W/S to move paddle",
            WINDOW_WIDTH / 2,
            WINDOW_HEIGHT * 0.5,
            arcade.color.BURNT_UMBER,
            20,
            anchor_x="center"
        )
        
        self.start_text = arcade.Text(
            "Press SPACE to start",
            WINDOW_WIDTH / 2,
            WINDOW_HEIGHT * 0.4,
            arcade.color.CORAL,
            20,
            anchor_x="center"
        )
        
        # Create Text objects for scores
        self.player_score_text = arcade.Text(
            "0",
            WINDOW_WIDTH / 4,
            WINDOW_HEIGHT - 50,
            arcade.color.DARK_GOLDENROD,
            30
        )
        
        self.opponent_score_text = arcade.Text(
            "0",
            3 * WINDOW_WIDTH / 4,
            WINDOW_HEIGHT - 50,
            arcade.color.AMARANTH_PINK,
            30
        )
        
        # Set up game objects
        self.player_paddle = None
        self.opponent_paddle = None
        self.ball = None
        
        # Create the sprite list
        self.sprite_list = None
        
        # Set background color
        arcade.set_background_color(arcade.color.BLACK)
        self.setup()
        
        self.player_score = 0
        self.opponent_score = 0
        # Track ball speed
        self.current_ball_speed = BALL_SPEED
        
    def setup(self):
        # Create sprite list
        self.sprite_list = arcade.SpriteList()
        
        # Create game objects
        self.player_paddle = arcade.SpriteSolidColor(10, 100, arcade.color.WHITE)
        self.player_paddle.center_x = 50
        self.player_paddle.center_y = WINDOW_HEIGHT // 2
        
        # Create AI opponent
        self.opponent_paddle = arcade.SpriteSolidColor(10, 100, arcade.color.RADICAL_RED)
        self.opponent_paddle.center_x = WINDOW_WIDTH - 50
        self.opponent_paddle.center_y = WINDOW_HEIGHT // 2
        
        # Add ball
        self.ball = arcade.SpriteCircle(BALL_SIZE, arcade.color.WHITE)
        self.ball.center_x = WINDOW_WIDTH // 2
        self.ball.center_y = WINDOW_HEIGHT // 2
        self.ball.change_x = BALL_SPEED
        self.ball.change_y = BALL_SPEED
        
        # Add sprites to the list
        self.sprite_list.append(self.player_paddle)
        self.sprite_list.append(self.opponent_paddle)
        self.sprite_list.append(self.ball)
            
    def on_draw(self):
       # Clear screen and draw objects
        self.clear()
        self.sprite_list.draw()
        
        # Draw scores (update text and draw)
        self.player_score_text.text = f"{self.player_score}"
        self.opponent_score_text.text = f"{self.opponent_score}"
        self.player_score_text.color = arcade.color.AIR_FORCE_BLUE
        self.opponent_score_text.color = arcade.color.ARMY_GREEN
        self.player_score_text.draw()
        self.opponent_score_text.draw()
        
        # Draw Menu state if in menu state
        if self.game_state == "MENU":
            # Update colors for menu items
            self.title_text.color = arcade.color.YELLOW_ROSE
            self.instruction_text.color = arcade.color.PURPLE_HEART
            self.start_text.color = arcade.color.WHITE
            
            # Draw menu items
            self.title_text.draw()
            self.instruction_text.draw()
            self.start_text.draw()
        
    def on_update(self, delta_time):
        if self.game_state == "PLAYING":
            
            # Update sprite position
            self.sprite_list.update()
            
            # Keep player paddle in bounds
            if self.player_paddle.top > WINDOW_HEIGHT:
                self.player_paddle.top = WINDOW_HEIGHT
            if self.player_paddle.bottom < 0:
                self.player_paddle.bottom = 0
                    
            # Ball bouncing off top and bottom
            if self.ball.top > WINDOW_HEIGHT or self.ball.bottom < 0:
                self.ball.change_y *= -1
                    
            # Check for ball collision with paddles
            if arcade.check_for_collision(self.ball, self.player_paddle) or \
            arcade.check_for_collision(self.ball, self.opponent_paddle):
                # Reverse ball direction
                self.ball.change_x *= -1
                # Increase ball speed
                self.current_ball_speed *= 1.1
                self.ball.change_x = self.current_ball_speed if self.ball.change_x > 0 else -self.current_ball_speed
                self.ball.change_y = self.current_ball_speed if self.ball.change_y > 0 else -self.current_ball_speed
                    
            # AI movement
            if self.opponent_paddle.center_y < self.ball.center_y:
                self.opponent_paddle.center_y += PADDLE_SPEED
            elif self.opponent_paddle.center_y > self.ball.center_y:
                self.opponent_paddle.center_y -= PADDLE_SPEED
                    
            # Keep AI paddle in bounds
            if self.opponent_paddle.top > WINDOW_HEIGHT:
                self.opponent_paddle.top = WINDOW_HEIGHT
            if self.opponent_paddle.bottom < 0:
                self.opponent_paddle.bottom = 0
                        
            # Scoring and reset ball
            if self.ball.right > WINDOW_WIDTH: # Player scores
                self.player_score += 1
                self.reset_ball()
            elif self.ball.left < 0:
                self.opponent_score += 1
                self.reset_ball()
                    
                
    def on_key_press(self, key, modifiers):
        print("Any key when pressed")
        # Handle key presses
        if key == arcade.key.SPACE and self.game_state == "MENU":
            # Change game state to playing
            self.game_state = "PLAYING"
            # Reset ball to start the game
            self.reset_ball()
        if self.game_state == "PLAYING":
            if key == arcade.key.UP:
                self.player_paddle.change_y = PADDLE_SPEED
            elif key == arcade.key.DOWN:
                self.player_paddle.change_y = -PADDLE_SPEED
            
    def on_key_release(self, key, modifiers):
        # Stop paddle when key is released
        if key in (arcade.key.UP, arcade.key.S, arcade.key.DOWN, arcade.key.W):
            self.player_paddle.change_y = 0
            
    def reset_ball(self):
        self.ball.center_x = WINDOW_WIDTH // 2
        self.ball.center_y = WINDOW_HEIGHT // 2
        
        # Reset speed to initial value
        self.current_ball_speed = BALL_SPEED
        
        # Randomize direction
        direction = random.choice([-1, 1])
        
        # Randomize angle
        angle = random.uniform(-45, 45)
        
        # Convert angle to radians and calculate x/y components
        angle_rad = math.radians(angle)
        self.ball.change_x = direction * self.current_ball_speed * math.cos(angle_rad)
        self.ball.change_y = self.current_ball_speed * math.sin(angle_rad)
            
def main():
    game = PongGame()
    game.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()
    
    # Adding in more features to get it working on personal portfoilio
    # More features to add.