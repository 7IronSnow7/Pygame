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
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    month_n = 0
    day = 0
    year = 0
    date = input("Date: ")
    
    print(date)
    
    # Let's split the date
    split_str = date.split(",")
    print("Split date, well hopefully")
    year = split_str[1]
    print(f"This should be the year {split_str[1]}")
    
    split_split = split_str[0].split()
    print("This should be the split split here")
    print(split_split)

    
    if split_split[0] in months:
        print("It is")
        month_name = split_split[0]
        month_mumber = months[month_name]
        month_n = month_mumber
        
        if int(split_split[1]) > 0 and int(split_split[1]) <= 12: # Day
            print(f"It is {split_split[1]}")
            day = split_split[1]
            
    print("day: " + day)
    print(f"month: {month_n}")
    print(f"year: {year}")

    print(f"{year}-{int(month_n):02}-{int(day):02}")
    print(f"{1:02}")
    
        
    
    
main()
#