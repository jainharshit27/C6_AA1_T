import pygame

pygame.init()

screen = pygame.display.set_mode((200, 200))

game_over = "GAME OVER"
go_font = pygame.font.Font("freesansbold.ttf", 16)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    go = go_font.render(game_over, True, (0, 0, 0))
    screen.blit(go, (50, 90)) 
    
    pygame.display.update()