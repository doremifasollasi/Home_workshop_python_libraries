import pygame

# визначаємо константу затримки кадрів
# та інші константи
FPS = 60

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

WHITE_COLOR = (255, 255, 255)  
ORANGE_COLOR = (255, 150, 100)

COORD_X=50
COORD_Y=50
WIDTH_RECTANGLE=40
HEIGHT_RECTANGLE=60
DELTA_STEP=5
 
# ініціалізація та створення об'єктів
pygame.init()
# pygame.display.set_mode((600, 400))

gameDisplay=pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    


    gameDisplay.fill((0,0,0))
       
    pygame.draw.rect(gameDisplay, (255,0,0), [COORD_X, 
                                        COORD_Y, 
                                        WIDTH_RECTANGLE, 
                                        HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)