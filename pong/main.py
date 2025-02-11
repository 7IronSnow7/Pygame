# from settings import *
# from sprites import *

# class Game:
#     def __init__(self):
#         pygame.init()
#         self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#         pygame.display.set_caption("Pong")
#         self.clock = pygame.time.Clock()
#         self.running = True
        
#         # sprites
#         self.all_sprites = pygame.sprite.Group()
#         self.paddle_sprites = pygame.sprite.Group()
#         self.player = Player((self.all_sprites, self.paddle_sprites))
#         self.ball = Ball(self.all_sprites, self.paddle_sprites)
        
#     def run(self):
#         while self.running:
#             dt = self.clock.tick() / 1000
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.running = False
                    
#             # update
#             self.all_sprites.update(dt)
            
#             # draw
#             self.display_surface.fill(COLORS['bg'])
#             self.all_sprites.draw(self.display_surface)
#             pygame.display.update()
#         pygame.quit()
        
# if __name__ == '__main__':
#     game = Game()
#     game.run()
    
#     # add more updates

# Using this as a testing ground real quick ADHD I feel is the issue here

def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    month = ""
    day = 0
    year = 0
    date = input("Date: ")
    
    print(date)
    
    # Let's split the date
    split_str = date.split(",")
    print("Split date, well hopefully")
    print(f"This should be the year {split_str[0]}")
    
    split_split = split_str[0].split()
    print("This should be the split split here")
    print(split_split)

    
    if split_split[0] in months:
        print("It is")
        month = split_split[0]
        
        if int(split_split[1]) > 0 and int(split_split[1]) <= 12: # Day
            print(f"It is {split_split[1]}")
            day = split_split[1]
        
    
        
    
    
main()
#