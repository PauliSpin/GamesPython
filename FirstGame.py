import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("First Game")

# Each of the images 64x64 pixels and there are 9 each for walking right and left
walkRight = [pygame.image.load('pics/R1.png'), pygame.image.load('pics/R2.png'), pygame.image.load('pics/R3.png'), pygame.image.load('pics/R4.png'), pygame.image.load(
    'pics/R5.png'), pygame.image.load('pics/R6.png'), pygame.image.load('pics/R7.png'), pygame.image.load('pics/R8.png'), pygame.image.load('pics/R9.png')]
walkLeft = [pygame.image.load('pics/L1.png'), pygame.image.load('pics/L2.png'), pygame.image.load('pics/L3.png'), pygame.image.load('pics/L4.png'), pygame.image.load(
    'pics/L5.png'), pygame.image.load('pics/L6.png'), pygame.image.load('pics/L7.png'), pygame.image.load('pics/L8.png'), pygame.image.load('pics/L9.png')]
bg = pygame.image.load('pics/bg.jpg')
char = pygame.image.load('pics/standing.png')

screenWidth = 500
frameRate = 27  # Because we have this many sprites
clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):

        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[int(self.walkCount//3)],
                     (int(self.x), int(self.y)))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[int(self.walkCount//3)],
                     (int(self.x), int(self.y)))
            self.walkCount += 1
        else:
            win.blit(char, (int(self.x), int(self.y)))
            self.walkCount = 0

    pygame.display.update()


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    pygame.display.update()


# main loop

man = player(300, 410, 64, 64)
run = True
while run:
    # pygame.time.delay(100)  # milliseconds

    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < screenWidth - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
    else:
        man.right = False
        man.left = False
        man.walkCount = 0

    if not(man.isJump):

        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
