import pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()
clock.tick(1)
x = 100
y = 100
for _ in range(100):
    pygame.draw.circle(screen,(255,255,255),(x,y),50,1)
    pygame.display.update()
    x +=1
    y+=1

running = True
while running:
    clock.tick(1)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False