import random
import pygame
pygame.init()

sw = 600
sh = 600
# bg = pygame.image.load('bg2.png')
win = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Slider")
numbers = []
for i in range(4):
    for j in range(4):
        numbers.append((j, i))
print(numbers)
clock = pygame.time.Clock()


class Tile(object):
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.w = 100
        self.h = 100
        self.color = (0, 100, 200)
        self.point = (self.x, self.y)
        self.coordinate = ((self.x - 100)/100, (self.y - 100)/100)

    def moveUp(self):
        self.y -= 100
        self.point = (self.x, self.y)
        self.coordinate = ((self.x - 100) / 100, (self.y - 100) / 100)

    def moveDown(self):
        self.y += 100
        self.point = (self.x, self.y)
        self.coordinate = ((self.x - 100) / 100, (self.y - 100) / 100)

    def moveRight(self):
        self.x += 100
        self.point = (self.x, self.y)
        self.coordinate = ((self.x - 100) / 100, (self.y - 100) / 100)

    def moveLeft(self):
        self.x -= 100
        self.point = (self.x, self.y)
        self.coordinate = ((self.x - 100) / 100, (self.y - 100) / 100)

    def draw(self, win):
        num = pygame.font.SysFont('comicsans', 50)
        numText = num.render(str(self.value), 1, (255, 255, 255))
        pygame.draw.rect(win, self.color, [self.x, self.y, self.w, self.h])
        win.blit(numText, (self.x + self.w//2-numText.get_width()//2, self.y + self.h//2-numText.get_height()//2))
        pygame.draw.rect(win, (0,0,0), [self.x, self.y, self.w, self.h], 2)

def redrawGameWindow():
    if not won:
        pygame.draw.rect(win, (0, 0, 0), [0, 0, 600, 600])
    else:
        pygame.draw.rect(win, (0, 160, 0), [0, 0, 600, 600])
    pygame.draw.rect(win, (255, 255, 255), [100, 100, 400, 400])
    for t in tiles:
        t.draw(win)
    # win.blit(bg, (0, 0))
    font = pygame.font.SysFont('comicsans', 50)
    # scoreText = font.render(str(p1score), 1, (255, 255, 255))
    # win.blit(score1, (sw - (score1.get_width()) - 20, 30))
    # pong.draw(win)
    pygame.display.update()

won = False
tiles = []
vals = []
for x in range(15):
    vals.append(x+1)
for i in range(15):
    #tiles.append(Tile(i + 1, 100 + 100 * numbers[i][0], 100 + 100 * numbers[i][1]))
    tiles.append(Tile(vals.pop(random.randrange(0,len(vals))), 100 + 100*numbers[i][0], 100 + 100 * numbers[i][1]))
run = True
while run:
    clock.tick(40)
    #tiles[0].y = 400
    #tiles[0].x = 400
    #tiles[0].point = (tiles[0].x, tiles[0].y)
    #tiles[0].coordinate = ((tiles[0].x - 100) / 100, (tiles[0].y - 100) / 100)

    poss = numbers.copy()
    for t in tiles:
        #print(t.coordinate, len(poss))
        #print(poss)
        if t.coordinate in poss:
            poss.remove(t.coordinate)
    if len(poss) > 0:
        emptyTile = poss[0]
    #print(emptyTile)

    # check for win
    #print(len(numbers))
    #match
    wrong = False
    for t in tiles:
        if t.coordinate != numbers[t.value-1]:
            t.color = (0, 100, 200)
            wrong = True
        else:
            t.color = (0,140,0)
    if not wrong:
        #print("WON")
        won = True
    else:
        won = False

    mousex, mousey = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    temp = (9,0)
    if click != (0, 0, 0):
        #print('clicked!')
        for t in tiles:
            if mousex >= t.x and mousex <= t.x + t.w:
                if mousey >= t.y and mousey <= t.y + t.h:
                    # print('Tile found')
                    moveDir = (t.coordinate[0] - emptyTile[0], t.coordinate[1] - emptyTile[1])
                    print(moveDir)
                    if moveDir == (1, 0):
                        temp = t.coordinate
                        t.moveLeft()
                        emptyTile = temp
                    elif moveDir == (0, 1):
                        temp = t.coordinate
                        t.moveUp()
                        emptyTile = temp
                    elif moveDir == (0, -1):
                        temp = t.coordinate
                        t.moveDown()
                        emptyTile = temp
                    elif moveDir == (-1, 0):
                        temp = t.coordinate
                        t.moveRight()
                        emptyTile = temp
                    else:
                        print('none')
                    poss = numbers



    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        tiles.clear()
        for x in range(15):
            vals.append(x + 1)
        for i in range(15):
            tiles.append(
                Tile(vals.pop(random.randrange(0, len(vals))), 100 + 100 * numbers[i][0], 100 + 100 * numbers[i][1]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.mouse.get_pressed():
            for t in tiles:
                pass#if pygame.mouse.get_presse
    redrawGameWindow()
pygame.quit()
