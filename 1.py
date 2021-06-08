import sys
import time
import random
import pygame

pygame.init()
gray = (119, 118, 110)
black = (0, 0, 0)
white = (225, 225, 225)
yellow = (252, 190, 3)
bright_yellow = (252, 206, 66)
green = (30, 250, 0)
bright_green = (71, 242, 48)
blue = (5, 245, 245)
bright_blue = (73, 242, 242)
display_width = 800
display_height = 600

gamedisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('car game')
clock = pygame.time.Clock()
caring = pygame.image.load('car6.png')
background_pic = pygame.image.load('grass.jpg')
yellow_Strip = pygame.image.load('road.jpg')
white_strip = pygame.image.load('white_Strip.png')
road = pygame.image.load('road1.jpg')
road1 = pygame.image.load('road2.jpg')
car_width = 70
pause = False
intro_background = pygame.image.load("backgro1.jpg")
instruc_background = pygame.image.load("backgro.png")
pause_background = pygame.image.load("backgro3.jpg")


def paused():
    global pause
    pause=True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        gamedisplay.blit(instruc_background, (0, 0))
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        textsurf, textrect = text_objects("PAUSED", largetext)
        textrect.center = (400, 100)
        gamedisplay.blit(textsurf, textrect)
        button("CONTINUE", 110, 420, 150, 50, green, bright_green, "unpause")
        button("RESTART", 550, 420, 150, 50, yellow, bright_yellow, "play")
        button("MAIN MENU", 300, 420, 200, 50, blue, bright_blue, "menu")
        pygame.display.update()
        clock.tick(50)


def unpaused():
    global pause
    pause = False


def introduction():
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.blit(instruc_background, (0, 0))
        largetext = pygame.font.Font("freesansbold.ttf", 80)
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        mediumtext = pygame.font.Font("freesansbold.ttf", 40)
        textsurf, textrect = text_objects("This is a car game in which you need dodge the coming car", smalltext)
        textrect.center = (400, 150)
        Textsurf, Textrect = text_objects("INSTRUCTION", largetext)
        Textrect.center = (400, 70)
        gamedisplay.blit(Textsurf, Textrect)
        gamedisplay.blit(textsurf, textrect)
        stextsurf, stextrect = text_objects("ARROW LEFT : LEFT TURN ", smalltext)
        stextrect.center = (180, 300)
        htextsurf, htextrect = text_objects("ARROW RIGHT : RIGHT TURN ", smalltext)
        htextrect.center = (180, 350)
        atextsurf, atextrect = text_objects("A: ACCELERATOR ", smalltext)
        atextrect.center = (180, 400)
        rtextsurf, rtextrect = text_objects("B : BREAK", smalltext)
        rtextrect.center = (180, 450)
        ptextsurf, ptextrect = text_objects("P : PAUSE ", smalltext)
        ptextrect.center = (180, 500)
        ctextsurf, ctextrect = text_objects("CONTROLS ", mediumtext)
        ctextrect.center = (400, 230)
        gamedisplay.blit(ctextsurf, ctextrect)  # controls
        gamedisplay.blit(ptextsurf, ptextrect)  # pause
        gamedisplay.blit(stextsurf, stextrect)  # Arrow left
        gamedisplay.blit(htextsurf, htextrect)  # Arrow right
        gamedisplay.blit(atextsurf, atextrect)  # Accerlerator
        gamedisplay.blit(rtextsurf, rtextrect)  # break
        button("BACK", 600, 400, 100, 50, blue, bright_blue, "menu")
        pygame.display.update()
        clock.tick(30)


def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.blit(intro_background, (0, 0))
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        textsurf, textrect = text_objects("CAR GAME", largetext)
        textrect.center = (400, 100)
        gamedisplay.blit(textsurf, textrect)
        button("START", 150, 520, 100, 50, green, bright_green, "play")
        button("QUIT", 550, 520, 100, 50, yellow, bright_yellow, "quit")
        button("INSTRUCTION", 300, 520, 200, 50, blue, bright_blue, "intro")
        pygame.display.update()
        clock.tick(50)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "intro":
                introduction()
            elif action == "menu":
                intro_loop()
            elif action == "pause":
                paused()
            elif action == "unpause":
                unpaused()


    else:
        pygame.draw.rect(gamedisplay, ic, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 28)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    gamedisplay.blit(textsurf, textrect)


def score_sysytem(passed, score):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Passed " + str(passed), True, white)
    score = font.render("Score " + str(score), True, white)
    gamedisplay.blit(text, (0, 50))
    gamedisplay.blit(score, (0, 10))


def obstacle(obs_startx, obs_starty, obs):
    if obs == 0:
        obs_pic = pygame.image.load('bb.png')
    elif obs == 1:
        obs_pic = pygame.image.load('gg.png')
    elif obs == 2:
        obs_pic = pygame.image.load('red.png')
    elif obs == 3:
        obs_pic = pygame.image.load('car6.png')
    elif obs == 4:
        obs_pic = pygame.image.load('blue1.png')
    elif obs == 5:
        obs_pic = pygame.image.load('white1.png')
    elif obs == 6:
        obs_pic = pygame.image.load('pur1.png')
    elif obs == 7:
        obs_pic = pygame.image.load('yell1.png')
    gamedisplay.blit(obs_pic, (obs_startx, obs_starty))


def text_objects(text, font):
    textsurface = font.render(text, True, white)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((display_width / 2), (display_height / 2))
    gamedisplay.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("YOU CRASHED")


def background():
    gamedisplay.blit(background_pic, (0, 0))
    gamedisplay.blit(background_pic, (0, 100))
    gamedisplay.blit(background_pic, (0, 200))
    gamedisplay.blit(background_pic, (0, 400))

    gamedisplay.blit(background_pic, (630, 0))
    gamedisplay.blit(background_pic, (630, 100))
    gamedisplay.blit(background_pic, (630, 300))
    gamedisplay.blit(background_pic, (630, 400))

    gamedisplay.blit(yellow_Strip, (290, 0))
    gamedisplay.blit(yellow_Strip, (290, 200))
    gamedisplay.blit(yellow_Strip, (290, 400))

    gamedisplay.blit(road, (140, 0))
    gamedisplay.blit(road, (140, 200))
    gamedisplay.blit(road, (140, 400))

    gamedisplay.blit(road, (540, 0))
    gamedisplay.blit(road, (540, 200))
    gamedisplay.blit(road, (540, 400))

    gamedisplay.blit(white_strip, (160, 0))
    gamedisplay.blit(white_strip, (160, 200))
    gamedisplay.blit(white_strip, (160, 400))

    gamedisplay.blit(white_strip, (630, 0))
    gamedisplay.blit(white_strip, (630, 200))
    gamedisplay.blit(white_strip, (630, 400))

    gamedisplay.blit(road1, (240, 0))
    gamedisplay.blit(road1, (240, 200))
    gamedisplay.blit(road1, (240, 400))

    gamedisplay.blit(road1, (500, 0))
    gamedisplay.blit(road1, (500, 200))
    gamedisplay.blit(road1, (500, 400))


def car(x, y):
    gamedisplay.blit(caring, (x, y))


def game_loop():
    global pause
    x = (display_width * 0.46)
    y = (display_height * 0.76)
    x_change = 0
    obstacal_speed = 9
    obs = 0
    y_change = 0
    obs_startx = random.randrange(160, (display_width - 330))  # (200, (display_width - 200))
    obs_starty = -750
    obs_width = 70
    obs_height = 139

    passed = 0
    level = 0
    score = 0

    y2=7
    fps=12

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_a:
                    obstacal_speed += 2
                if event.key == pygame.K_b:
                    obstacal_speed -= 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gamedisplay.fill(gray)

        rel_y= y2% background_pic.get_rect().width
        gamedisplay.blit(background_pic,(0,rel_y-background_pic.get_rect().width))
        gamedisplay.blit(background_pic, (630, rel_y - background_pic.get_rect().width))
        if rel_y < 800:
            gamedisplay.blit(background_pic,(0,rel_y+80))
            gamedisplay.blit(background_pic, (0, rel_y + 180))
            gamedisplay.blit(background_pic, (0, rel_y + 280))
            gamedisplay.blit(background_pic, (0, rel_y + 380))
            gamedisplay.blit(background_pic, (630, rel_y + 80))
            gamedisplay.blit(background_pic, (630, rel_y + 180))
            gamedisplay.blit(background_pic, (630, rel_y + 280))
            gamedisplay.blit(background_pic, (630, rel_y+380))

            gamedisplay.blit(yellow_Strip, (290, rel_y))
            gamedisplay.blit(yellow_Strip, (290, rel_y + 100))
            gamedisplay.blit(yellow_Strip, (290, rel_y + 200))
            gamedisplay.blit(yellow_Strip, (290, rel_y + 300))
            gamedisplay.blit(yellow_Strip, (290, rel_y + 400))
            gamedisplay.blit(yellow_Strip, (290, rel_y - 200))
            gamedisplay.blit(yellow_Strip, (290, rel_y - 100))


            gamedisplay.blit(road, (140, rel_y + 100))
            gamedisplay.blit(road, (140, rel_y + 200))
            gamedisplay.blit(road, (140, rel_y + 400))
            gamedisplay.blit(road, (140, rel_y - 100))
            gamedisplay.blit(road, (140, rel_y - 200))
            gamedisplay.blit(road, (540, rel_y + 100))
            gamedisplay.blit(road, (540, rel_y + 200))
            gamedisplay.blit(road, (540, rel_y + 400))
            gamedisplay.blit(road, (540, rel_y - 100))
            gamedisplay.blit(road, (540, rel_y - 200))

            gamedisplay.blit(road1, (240, rel_y + 100))
            gamedisplay.blit(road1, (240, rel_y + 200))
            gamedisplay.blit(road1, (240, rel_y + 400))
            gamedisplay.blit(road1, (240, rel_y - 100))
            gamedisplay.blit(road1, (240, rel_y - 200))
            gamedisplay.blit(road1, (500, rel_y + 100))
            gamedisplay.blit(road1, (500, rel_y + 200))
            gamedisplay.blit(road1, (500, rel_y + 400))
            gamedisplay.blit(road1, (500, rel_y - 100))
            gamedisplay.blit(road1, (500, rel_y - 200))



            gamedisplay.blit(white_strip, (160, rel_y + 100))
            gamedisplay.blit(white_strip, (160, rel_y + 200))
            gamedisplay.blit(white_strip, (160, rel_y + 400))
            gamedisplay.blit(white_strip, (160, rel_y - 100))
            gamedisplay.blit(white_strip, (160, rel_y - 200))

            gamedisplay.blit(white_strip, (630, rel_y + 100))
            gamedisplay.blit(white_strip, (630, rel_y + 200))
            gamedisplay.blit(white_strip, (630, rel_y + 400))
            gamedisplay.blit(white_strip, (630, rel_y - 100))
            gamedisplay.blit(white_strip, (630, rel_y - 200))
            #gamedisplay.blit(white_strip, (630, rel_y + 30))
        y2+=obstacal_speed


        #background() here we comment this cause we wanna moving objects
        obs_starty -= (obstacal_speed / 4)
        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacal_speed
        car(x, y)

        score_sysytem(passed, score)
        if x > 650 - car_width or x < 150:
            crash()
        if x > display_width - (car_width + 150) or x < 150:
            crash()
        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(200, (display_width - 330))
            obs = random.randrange(0, 8)
            passed = passed + 1
            score = passed * 10
            if int(passed) % 10 == 0:
                level = level + 1
                obstacal_speed += 2
                largetext = pygame.font.Font("freesansbold.ttf", 80)
                textsurf, textrect = text_objects("LEVEL" + str(level), largetext)
                textrect.center = ((display_width / 2), (display_height / 2))
                gamedisplay.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y < obs_starty + obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x + car_width > obs_startx and x + car_width < obs_startx + obs_width:
                crash()

        button("Pause", 670, 0, 120, 50, blue, bright_blue, "pause")
        pygame.display.update()
        clock.tick(60)


intro_loop()
game_loop()
pygame.quit()
quit()
