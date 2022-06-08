import pygame
WIDTH , HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH , HEIGHT))
WHITE = (255,255,255)

pygame.display.set_caption("Shooter")


from pygame import mixer

mixer.music.load('Main_Theme.mp3')

mixer.music.play()

#Game loop 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    WIN.fill(WHITE)
    pygame.display.update()
    
    
    
