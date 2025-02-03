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

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_SPEED = 5
BALL_SIZE = 10
BALL_SPEED = 5

class PongGame(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Pong")
        # Set up game objects
        self.player_paddle = None
        self.opponent_paddle = None
        self.ball = None
        
        # Create the sprite list
        self.sprite_list = None
        
        # Set background color
        arcade.set_background_color(arcade.color.BLACK)
        self.setup()
        
    def setup(self):
        # Create sprite list
        self.sprite_list = arcade.SpriteList()
        
        # Create game objects
        self.player_paddle = arcade.SpriteSolidColor(10, 100, arcade.color.WHITE)
        self.player_paddle.center_x = 50
        self.player_paddle.center_y = WINDOW_HEIGHT // 2
        
        # Create AI opponent
        self.opponent_paddle = arcade.SpriteSolidColor(10, 100, arcade.color.RED)
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
        
    def on_update(self, delta_time):
        # Update sprite position
        self.sprite_list.update()
        
        # Keep paddle in bounds
        if self.player_paddle.top > WINDOW_HEIGHT:
            self.player_paddle.top = WINDOW_HEIGHT
        if self.player_paddle.bottom < 0:
            self.player_paddle.bottom = 0
            
        # Ball bouncing off top and bottom
        if self.ball.top > WINDOW_HEIGHT or self.ball.bottom < 0:
            self.ball.change_y = -self.ball.change_y
            
        # Ball bouncing off paddle
        if arcade.check_for_collision(self.ball, self.player_paddle):
            self.ball.change_x = -self.ball.change_x
            
        # AI movement (Make opponent paddle follow the ball)
        if self.opponent_paddle.center_y < self.ball.center_y:
            self.opponent_paddle.center_y += PADDLE_SPEED
        elif self.opponent_paddle.center_y > self.ball.center_y:
            self.opponent_paddle.center_y -= PADDLE_SPEED
            
        # Keep AI paddle in bounds
        if self.opponent_paddle.top > WINDOW_HEIGHT:
            self.opponent_paddle.top = WINDOW_HEIGHT
        if self.opponent_paddle.bottom < 0:
            self.opponent_paddle.bottom = 0
        
        # Reset ball if it goes off screen
        if self.ball.left > WINDOW_WIDTH or self.ball.right < 0:
            self.ball.center_x = WINDOW_WIDTH // 2
            self.ball.center_y = WINDOW_HEIGHT // 2

    def on_key_press(self, key, modifiers):
        # Handle key presses
        if key == arcade.key.UP:
            self.player_paddle.change_y = PADDLE_SPEED
        elif key == arcade.key.DOWN:
            self.player_paddle.change_y = -PADDLE_SPEED
            
    def on_key_release(self, key, modifiers):
        # Stop paddle when key is released
        if key in (arcade.key.UP, arcade.key.DOWN):
            self.player_paddle.change_y = 0
            
def main():
    game = PongGame()
    game.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()
    
    # Adding in more features to get it working on personal portfoilio
    # More features to add.