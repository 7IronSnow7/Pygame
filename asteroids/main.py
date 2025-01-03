# import pygame
# from constants import *
# from player import *
            
# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     clock = pygame.time.Clock()
#     player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
#     # player_velocity_x = 200
    
#     running = True
    
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
                
#         # limit the framerate to 60 fps
#         dt = clock.tick(60) / 1000
                
#         # update player state
#         player.update(dt)
                
#         # update player position
#         # x += player_velocity_x * dt
#         # player.update(x, y)
        
#         # Drawing
#         screen.fill("black")
#         player.draw(screen)
#         pygame.display.flip()
        
       
        
# pygame.quit()

def get_player_position(position, velocity, friction, gravity):
    moved = calc_move(position, velocity)
    slowed = calc_friction(moved, friction)
    final = calc_gravity(slowed, gravity)
    print("Given:")
    print(f"position: {position}, velocity: {velocity}, friction: {friction}, gravity: {gravity}")
    print("Results:")
    print(f"moved: {moved}, slowed: {slowed}, final: {final}")
    return final

def main():
    position = 1
    velocity = 1
    friction = 1
    gravity  = 1
    get_player_position()
    
    
if __name__ == "__main__":
    main()