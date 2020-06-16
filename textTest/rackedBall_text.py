#pygame racked ball game with text
import pygame,sys
import pygame.freetype

pygame.init()
icon = pygame.image.load("../PYG03-flower.png")
pygame.display.set_icon(icon)
size = width, height = 600, 400
speed = [1,1]
BLACK = 0, 0, 0
fps = 300
fclock = pygame.time.Clock()
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

GOLD = 255, 251, 0
f1 = pygame.freetype.Font("c://windows//Fonts//msyh.ttc", 36) #微软雅黑
f1surf, f1rect = f1.render("世界和平", fgcolor=GOLD, size=50)
ballrect = f1rect

# pygame.display.set_caption("Pygame壁球")
# ball = pygame.image.load("../PYG02-ball.gif")
#ballrect = ball.get_rect()
still = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0])-1) *int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] +1 if speed[0]>0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1]>0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1])-1)*int(speed[1]/abs(speed[1]))
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                still = True
        elif event.type == pygame.MOUSEBUTTONUP:
            still = False
            if event.button == 1:
                ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1]-ballrect.top)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1]-ballrect.top)
    if pygame.display.get_active() and not still:
        ballrect = ballrect.move(speed)

    if ballrect.left<0 or ballrect.right > width:
        speed[0] = - speed[0]
        if ballrect.right > width and ballrect.right + speed[0] > ballrect.right:
            speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]
        if ballrect.bottom > height and ballrect.bottom + speed[1] > ballrect.bottom:
            speed[1] = -speed[1]
    screen.fill(BLACK)
    #f1surf, f1rect = f1.render("世界和平", fgcolor=GOLD, size = 50)
    #screen.blit(f1surf, (pos[0], pos[1]))
    screen.blit(f1surf, ballrect)
    #screen.blit(ball, ballrect)
    pygame.display.update()
    fclock.tick(fps)
