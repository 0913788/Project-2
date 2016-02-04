##Imports

import webbrowser

from Common import *
from HP_CP import *
from Player import *
from Sfighters import *
from Tile import *

##COLORS
white = (255, 255, 255)
red = (225, 0, 0)
green = (0, 215, 0)
blue = (0, 0, 255)
yellow = (204, 204, 0)
black = (0, 0, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
block_color = (53, 115, 255)

##_INIT
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

size = width, height = 1000, 900
display_width = 1000
display_height = 900

screen = pygame.display.set_mode(size)
gameDisplay = pygame.display.get_surface()
canvas = pygame.display.get_surface()
camera1 = pygame.Rect(0, 0, 700, 700)
camera2 = pygame.Rect(20, 700, 500, 180)
camera3 = pygame.Rect(700, 20, 280, 660)
camera3_1 = pygame.Rect(700, 20, 280, 165)
camera3_2 = pygame.Rect(700, 185, 280, 165)
camera3_3 = pygame.Rect(700, 350, 280, 165)
camera3_4 = pygame.Rect(700, 515, 280, 165)
camera4 = pygame.Rect(700, 700, 280, 180)
camera5 = pygame.Rect(103, 280, 230, 30)
camera6 = pygame.Rect(103, 350, 230, 30)
camera7 = pygame.Rect(365, 350, 230, 30)
hp_dict = hp_image()
cp_dict = cp_image()
mid_camera = pygame.Rect(80, 80, 539, 539)

mid_starter = pygame.Rect(95, 95, 244, 510)
mid_starter_rol_line = pygame.Rect(125, 500, 75, 75)
mid_starter_rol = pygame.Rect(127, 502, 71, 71)
mid_starter_dmg_line = pygame.Rect(240, 500, 75, 75)
mid_starter_dmg = pygame.Rect(242, 502, 71, 71)

mid_target = pygame.Rect(360, 95, 244, 510)
mid_target_rol_line = pygame.Rect(390, 500, 75, 75)
mid_target_rol = pygame.Rect(392, 502, 71, 71)
mid_target_dmg_line = pygame.Rect(505, 500, 75, 75)
mid_target_dmg = pygame.Rect(507, 502, 71, 71)

pygame.display.set_caption('Survivor by group 1')
GameIcon = pygame.image.load("Content/_fight.png").convert()
pygame.display.set_icon(GameIcon)

dobbel1 = pygame.image.load('Content\Dobbel_1.png').convert()
dobbel2 = pygame.image.load('Content\Dobbel_2.png').convert()
dobbel3 = pygame.image.load('Content\Dobbel_3.png').convert()
dobbel4 = pygame.image.load('Content\Dobbel_4.png').convert()
dobbel5 = pygame.image.load('Content\Dobbel_5.png').convert()
dobbel6 = pygame.image.load('Content\Dobbel_6.png').convert()
Fightmid = pygame.image.load("content/fight_moment.png").convert_alpha()

Super_fighters = create_fighters()

offset = 60
board_size = 11
Board, p1, p2, p3, p4 = build_square_matrix(board_size, offset)

Mid_Fight_Text = pygame.font.SysFont("comicsansms", 50)
Mid_Fight_Text2 = pygame.font.SysFont("comicsansms", 30)
camera3_info_text = pygame.font.SysFont("comicsansms", 18)

aantal_spelers = 0


## CONSTRUCTORS
def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pause = False


def button(msg, x, y, w, h, ic, ac, action=None, a=None, b=None, c=None, d=None, e=None, f=None, g=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (mouse[0] < x + w and mouse[0] > x) and (mouse[1] < y + h and mouse[1] > y):
        pygame.draw.rect(canvas, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if g != None:
                action(a, b, c, d, e, f, g)
            elif f != None:
                action(a, b, c, d, e, f)
            elif e != None:
                action(a, b, c, d, e)
            elif d != None:
                action(a, b, c, d)
            elif c != None:
                action(a, b, c)
            elif b != None:
                action(a, b)
            elif a != None:
                action(a)
            else:
                action()
    else:
        pygame.draw.rect(canvas, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("verdana", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    canvas.blit(textSurf, textRect)


##PRINTS
def Reprint():
    global loops
    screen.fill(black)
    Board.Reset(loops)
    Board.Draw(screen)
    canvas.fill((255, 255, 255), camera2)
    canvas.fill((255, 255, 255), camera3)
    canvas.fill((255, 255, 255), camera4)
    loops += 1


def Rol_text(placement):
    TextSurf, TextRect = text_objects("Rol:", Mid_Fight_Text2)
    gameDisplay.blit(TextSurf, placement)
    pygame.display.flip()


def Dmg_text(placement):
    TextSurf, TextRect = text_objects("Dmg:", Mid_Fight_Text2)
    gameDisplay.blit(TextSurf, placement)
    pygame.display.flip()


def Def_text(placement):
    TextSurf, TextRect = text_objects("Def:", Mid_Fight_Text2)
    gameDisplay.blit(TextSurf, placement)
    pygame.display.flip()


def TurnPicture():
    if beurt != None:
        canvas.blit(beurt.Value.TurnTexture, (510, 680))
    if beurt.Tail.IsEmpty:
        canvas.blit(players.Value.NextTexture, (510, 790))
    else:
        canvas.blit(beurt.Tail.Value.NextTexture, (510, 790))


def Move_print(a, b, c, d):
    player = beurt.Value
    w, x, y, z = Return_player(player.Kleur)
    _width = int(34)
    while a + b + c + d != 0:
        if a > 0:
            a -= 1
            X_plus_move = _width
            for i in range(_width - 3):
                Reprint()
                if player.Kleur == 1:
                    print_players(0, 1, 1, 1)
                elif player.Kleur == 2:
                    print_players(1, 0, 1, 1)
                elif player.Kleur == 3:
                    print_players(1, 1, 0, 1)
                elif player.Kleur == 4:
                    print_players(1, 1, 1, 0)
                screen.blit(pygame.transform.scale(player.Texture, (_width, _width)),
                            (X_plus_move + player.Locatie.Position.X * offset,
                             _width + player.Locatie.Position.Y * offset))
                X_plus_move += 2
                print_players(w, x, y, z)
                pygame.display.update(camera1)
                clock.tick(100)

        elif b > 0:
            b -= 1
            Y_plus_move = _width
            for i in range(_width - 3):
                Reprint()
                if player.Kleur == 1:
                    print_players(0, 1, 1, 1)
                elif player.Kleur == 2:
                    print_players(1, 0, 1, 1)
                elif player.Kleur == 3:
                    print_players(1, 1, 0, 1)
                elif player.Kleur == 4:
                    print_players(1, 1, 1, 0)
                screen.blit(pygame.transform.scale(player.Texture, (_width, _width)),
                            (_width + player.Locatie.Position.X * offset,
                             Y_plus_move + player.Locatie.Position.Y * offset))
                Y_plus_move += 2
                print_players(w, x, y, z)
                pygame.display.update(camera1)
                clock.tick(100)
        elif c > 0:
            c -= 1
            X_min_move = _width
            for i in range(_width - 3):
                Reprint()
                if player.Kleur == 1:
                    print_players(0, 1, 1, 1)
                elif player.Kleur == 2:
                    print_players(1, 0, 1, 1)
                elif player.Kleur == 3:
                    print_players(1, 1, 0, 1)
                elif player.Kleur == 4:
                    print_players(1, 1, 1, 0)
                screen.blit(pygame.transform.scale(player.Texture, (_width, _width)),
                            (X_min_move + player.Locatie.Position.X * offset,
                             _width + player.Locatie.Position.Y * offset))
                X_min_move -= 2
                print_players(w, x, y, z)
                pygame.display.update(camera1)
                clock.tick(100)
        elif d > 0:
            d -= 1
            Y_min_move = _width
            for i in range(_width - 3):
                Reprint()
                if player.Kleur == 1:
                    print_players(0, 1, 1, 1)
                elif player.Kleur == 2:
                    print_players(1, 0, 1, 1)
                elif player.Kleur == 3:
                    print_players(1, 1, 0, 1)
                elif player.Kleur == 4:
                    print_players(1, 1, 1, 0)
                screen.blit(pygame.transform.scale(player.Texture, (_width, _width)),
                            (_width + player.Locatie.Position.X * offset,
                             Y_min_move + player.Locatie.Position.Y * offset))
                Y_min_move -= 2
                print_players(w, x, y, z)
                pygame.display.update(camera1)
                clock.tick(100)


def print_players(x, y, z, a):
    if x == 1 and player1.Value.dead == False:
        player1.Value.draw(screen, offset)
    if y == 1 and player2.Value.dead == False:
        player2.Value.draw(screen, offset)
    if z == 1 and player3.Value.dead == False:
        player3.Value.draw(screen, offset)
    if a == 1 and player4.Value.dead == False:
        player4.Value.draw(screen, offset)


def print_players_info():
    klaar = False
    while not klaar:
        if not player1.Value.dead:
            a, b = text_objects("{}:".format(player1.Value.Naam), camera3_info_text)
            canvas.blit(a, (725, 35))
            a, b = text_objects("HP :  {}".format(player1.Value.Levenspunten), camera3_info_text)
            canvas.blit(a, (830, 70))
            a, b = text_objects("Conditie :  {}".format(player1.Value.Conditie), camera3_info_text)
            canvas.blit(a, (830, 100))
        else:
            a, b = text_objects("{} has died...".format(player1.Value.Naam), camera3_info_text)
            canvas.blit(a, (725, 35))
        if not player2.Value.dead:
            a, b = text_objects("{}:".format(player2.Value.Naam), camera3_info_text)
            canvas.blit(a, (725, 200))
            a, b = text_objects("HP :  {}".format(player2.Value.Levenspunten), camera3_info_text)
            canvas.blit(a, (830, 235))
            a, b = text_objects("Conditie :  {}".format(player2.Value.Conditie), camera3_info_text)
            canvas.blit(a, (830, 265))
        else:
            a, b = text_objects("{} has died...".format(player2.Value.Naam), camera3_info_text)
            canvas.blit(a, (725, 200))
        if not player3.Value.dead:
            a, b = text_objects("{}:".format(player3.Value.Naam), camera3_info_text)
            canvas.blit(a, (725, 365))
            a, b = text_objects("HP :  {}".format(player3.Value.Levenspunten), camera3_info_text)
            canvas.blit(a, (830, 400))
            a, b = text_objects("Conditie :  {}".format(player3.Value.Conditie), camera3_info_text)
            canvas.blit(a, (830, 430))
        else:
            a, b = text_objects("{} has died...".format(player3.Value.Naam), camera3_info_text)
            canvas.blit(a, (725, 365))
        if not player4.Value.dead:
            a, b = text_objects("{}:".format(player4.Value.Naam), camera3_info_text)
            canvas.blit(a, (725, 530))
            a, b = text_objects("HP :  {}".format(player4.Value.Levenspunten), camera3_info_text)
            canvas.blit(a, (830, 565))
            a, b = text_objects("Conditie :  {}".format(player4.Value.Conditie), camera3_info_text)
            canvas.blit(a, (830, 595))
        else:
            a, b = text_objects("{} has died...".format(player4.Value.Naam), camera3_info_text)
            canvas.blit(a, (725, 530))

        klaar = True


def print_rol(type, dmg):
    if type == "target":
        TextSurf, TextRect = text_objects("{}".format(dmg), Mid_Fight_Text)
        TextRect = ((410), (495))
        gameDisplay.blit(TextSurf, TextRect)
    else:
        TextSurf, TextRect = text_objects("{}".format(dmg), Mid_Fight_Text)
        TextRect = ((145), (495))
        gameDisplay.blit(TextSurf, TextRect)
    canvas.fill(white, camera2)
    pygame.display.flip()
    loop_pause(15)


def print_dmg(type, rol):
    if type == "target":
        TextSurf, TextRect = text_objects("{}".format(rol), Mid_Fight_Text)
        TextRect = ((515), (495))
        gameDisplay.blit(TextSurf, TextRect)
    else:
        TextSurf, TextRect = text_objects("{}".format(rol), Mid_Fight_Text)
        TextRect = ((250), (495))
        gameDisplay.blit(TextSurf, TextRect)
    canvas.fill(white, camera2)
    pygame.display.flip()
    loop_pause(15)


##Pre-Game
def Set_music(height):
    height *= 0.1
    pygame.mixer.music.set_volume(height)


def Player_select(aantal):
    global players, player1, player2, player3, player4, aantal_spelers
    players = Empty
    Pawn = ["Player 1", "Player 2", "Player 3", "Player 4"]
    for i in range(4):
        if i == 0 and aantal > 0:
            name = "Player1"
            players = Node(Player(name, 6, p1, "Content/__pawn_green.png", "content/players/player_green.png",
                                  "content/superfighters/{}.png".format(Pawn[i])), players)
            player1 = players
            aantal_spelers += 1
        elif i == 0 and aantal == 0:
            players = Node(Player("CPU-1", 6, p1, "Content/__pawn_green.png", "content/players/CPU_green.png",
                                  "content/superfighters/{}.png".format(Pawn[i])),
                           players)
            players.Value.Ai = 1
            player1 = players
        if i == 1 and aantal > 1:
            name = "Player2"
            players = Node(Player(name, 7, p2, "Content/__pawn_yellow.png", "content/players/player_yellow.png",
                                  "content/superfighters/{}.png".format(Pawn[i])),
                           players)
            player2 = players
            aantal_spelers += 1
        elif i == 1 and aantal <= 1:
            players = Node(Player("CPU-2", 7, p2, "Content/__pawn_yellow.png", "content/players/CPU_yellow.png",
                                  "content/superfighters/{}.png".format(Pawn[i])),
                           players)
            players.Value.Ai = 1
            player2 = players
        if i == 2 and aantal > 2:
            name = "Player3"
            players = Node(Player(name, 8, p3, "Content/__pawn_blue.png", "content/players/player_blue.png",
                                  "content/superfighters/{}.png".format(Pawn[i])), players)
            player3 = players
            aantal_spelers += 1
        elif i == 2 and aantal <= 2:
            players = Node(Player("CPU-3", 8, p3, "Content/__pawn_blue.png", "content/players/CPU_blue.png",
                                  "content/superfighters/{}.png".format(Pawn[i])),
                           players)
            players.Value.Ai = 1
            player3 = players
        if i == 3 and aantal > 3:
            name = "Player4"
            players = Node(Player(name, 9, p4, "Content/__pawn_red.png", "content/players/player_red.png",
                                  "content/superfighters/{}.png".format(Pawn[i])), players)
            player4 = players
            aantal_spelers += 1
        elif i == 3 and aantal <= 3:
            players = Node(Player("CPU-4", 9, p4, "Content/__pawn_red.png", "content/players/CPU_red.png",
                                  "content/superfighters/{}.png".format(Pawn[i])), players)
            players.Value.Ai = 1
            player4 = players


##Game Elements
def Change_turn():
    global players, beurt
    canvas.fill(white, camera2)
    beurt = beurt.Tail
    loop_pause(20)
    if beurt.IsEmpty:
        beurt = players
    TurnPicture()
    loop_pause(45)
    pygame.display.update(camera4)


def Rol():
    x = randint(1, 6)
    if x == 1:
        canvas.blit(dobbel1, [780, 735])
    elif x == 2:
        canvas.blit(dobbel2, [780, 735])
    elif x == 3:
        canvas.blit(dobbel3, [780, 735])
    elif x == 4:
        canvas.blit(dobbel4, [780, 735])
    elif x == 5:
        canvas.blit(dobbel5, [780, 735])
    else:
        canvas.blit(dobbel6, [780, 735])
    pygame.mixer.music.load("content/soundeffects/diceroll.wav")
    pygame.mixer.music.play(0, 0)
    pygame.display.update(camera4)
    return x


def Bewegen(player):
    global beurt
    x = Rol()
    canvas.fill((255,255,255), camera2)
    loop_pause(45)
    for i in range(x):
        if player.Locatie.Next == 1 or player.Locatie.Position == "(0,0)":
            Move_print(1, 0, 0, 0)
            player.Richting = 1
            player.Locatie = player.Locatie.Right
        elif player.Locatie.Next == 2 or player.Locatie.Position == "(10,0)":
            Move_print(0, 1, 0, 0)
            player.Richting = 2
            player.Locatie = player.Locatie.Down
        elif player.Locatie.Next == 3 or player.Locatie.Position == "(10,10)":
            Move_print(0, 0, 1, 0)
            player.Richting = 3
            player.Locatie = player.Locatie.Left
        elif player.Locatie.Next == 4 or player.Locatie.Position == "(0,10)":
            Move_print(0, 0, 0, 1)
            player.Richting = 4
            player.Locatie = player.Locatie.Up
        else:
            if player.Richting == 1:
                Move_print(1, 0, 0, 0)
                player.Locatie = player.Locatie.Right
            elif player.Richting == 2:
                Move_print(0, 1, 0, 0)
                player.Locatie = player.Locatie.Down
            elif player.Richting == 3:
                Move_print(0, 0, 1, 0)
                player.Locatie = player.Locatie.Left
            elif player.Richting == 4:
                Move_print(0, 0, 0, 1)
                player.Locatie = player.Locatie.Up
        pygame.mixer.music.load("content/soundeffects/pawnmove.wav")
        pygame.mixer.music.play(0, 0)
        if player.Kleur == 6 and player.Locatie == p1:
            if player.Levenspunten < 90:
                player.Levenspunten += 10
            else:
                player.Levenspunten = 100
            player.Conditie = 15
            pygame.mixer.music.load("content/soundeffects/addlifepoints.wav")
            pygame.mixer.music.play(0, 0)
            loop_pause(60)
        elif player.Kleur == 7 and player.Locatie == p2:
            if player.Levenspunten < 90:
                player.Levenspunten += 10
            else:
                player.Levenspunten = 100
            player.Conditie = 15
            pygame.mixer.music.load("content/soundeffects/addlifepoints.wav")
            pygame.mixer.music.play(0, 0)
            loop_pause(60)
        elif player.Kleur == 8 and player.Locatie == p3:
            if player.Levenspunten < 90:
                player.Levenspunten += 10
            else:
                player.Levenspunten = 100
            player.Conditie = 15
            pygame.mixer.music.load("content/soundeffects/addlifepoints.wav")
            pygame.mixer.music.play(0, 0)
        elif player.Kleur == 9 and player.Locatie == p4:
            if player.Levenspunten < 90:
                player.Levenspunten += 10
            else:
                player.Levenspunten = 100
            player.Conditie = 15
            pygame.mixer.music.load("content/soundeffects/addlifepoints.wav")
            pygame.mixer.music.play(0, 0)
            print(player.Levenspunten)
        if i != x:
            loop_pause(45)
        else:
            loop_pause(90)
        print_players(1, 1, 1, 1)
        pygame.display.update(camera1)
    Bepaal_actie(player)
    Change_turn()


def Bepaal_actie(player):
    global players
    player_target, position = Return_same_location(players, player.Locatie.Position, player.Kleur)
    if player.Locatie.Type == 10:
        Fight(player, Return_random_element(Super_fighters))
    elif player.Locatie.Type != player.Kleur and player.Locatie.Type in [6, 7, 8, 9]:
        Fight(player, Return_bepaalde_player(player.Locatie.Type))
    elif player.Locatie.Position in position:
        Fight(player, player_target)


##FIGHT
def Fight(starter, target):
    if target.Value.dead == False:
        TurnPicture()
        pygame.mixer.music.load("content/soundeffects/fightstart.wav")
        pygame.mixer.music.play(0, 0)
        canvas.blit(Fightmid, (200, 290))
        pygame.display.update(camera1)
        loop_pause(70)

        largeText = pygame.font.SysFont("comicsansms", 20)
        TextSurf, TextRect = text_objects('DEFENDER', largeText)
        TextRect = ((800), (22))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects('ATTACKER', largeText)
        TextRect = ((800), (352))
        gameDisplay.blit(TextSurf, TextRect)

        canvas.blit(starter.FightTexture, (700, 50))
        canvas.blit(target.Value.FightTexture, (700, 380))
        pygame.display.update(camera3)
        loop_pause(70)
        canvas.fill((0, 0, 0), mid_camera)
        canvas.fill((255, 255, 255), mid_target)
        canvas.blit(target.Value.FaceTexture, (405, 125))

        largeText = pygame.font.SysFont("calibri", 20)
        TextSurf, TextRect = text_objects(target.Value.Naam, largeText)
        TextRect.center = ((display_width / 2.05), (display_height / 8))
        gameDisplay.blit(TextSurf, TextRect)
        canvas.fill((255, 255, 255), mid_starter)
        canvas.blit(starter.FaceTexture, (115, 120))
        largeText = pygame.font.SysFont("calibri", 20)
        TextSurf, TextRect = text_objects(starter.Naam, largeText)
        TextRect.center = ((display_width / 5), (display_height / 8))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update(camera1)
        canvas.blit(hp_dict["HP_{}".format(starter.Levenspunten)], (103, 280))
        canvas.blit(cp_dict["CP_{}".format(starter.Conditie)], (103, 350))
        if target.Value.Player:
            canvas.blit(hp_dict["HP_{}".format(target.Value.Levenspunten)], (365, 280))
            if target.Value.Conditie < 0:
                target.Value.Conditie = 0
            canvas.blit(cp_dict["CP_{}".format(target.Value.Conditie)], (365, 350))
        canvas.fill(black, mid_starter_rol_line)
        canvas.fill(white, mid_starter_rol)
        canvas.fill(black, mid_starter_dmg_line)
        canvas.fill(white, mid_starter_dmg)
        canvas.fill(black, mid_target_rol_line)
        canvas.fill(white, mid_target_rol)
        canvas.fill(black, mid_target_dmg_line)
        canvas.fill(white, mid_target_dmg)
        print_players(1, 1, 1, 1)
        Rol_text(((135), (450)))
        Rol_text(((400), (450)))
        Def_text(((250), (450)))
        Dmg_text(((510), (450)))
        loop_pause(20)

        if starter.Ai == 0 and target.Value.Ai == 0:
            Player_vs_player_fight(starter, target)
        elif starter.Ai == 0 and target.Value.Ai == 1:
            Player_defense_fight(starter, target)
        elif starter.Ai == 1 and target.Value.Ai == 0:
            Player_attack_fight(starter, target)
        elif starter.Ai == 1 and target.Value.Ai == 1:
            Ai_fight(starter, target)

    Change_turn()
    game_loop(False)


def Player_attack_fight(starter, target, first_roll=None, choice=None):
    loop_pause(45)
    if first_roll == None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        manual()
                    if event.key == pygame.K_SPACE:
                        Player_attack_fight(starter, target, True)

            largeText = pygame.font.SysFont("comicsansms", 22)
            TextSurf, TextRect = text_objects("{} Roll the dice:".format(target.Value.Naam), largeText)
            TextRect.center = ((140), (725))
            gameDisplay.blit(TextSurf, TextRect)
            button("Gooi dobbelsteen", 40, 760, 200, 100, red, green, Player_attack_fight, starter, target, True)
            pygame.display.flip()
            clock.tick(10)

    elif choice == None:
        x = Rol()
        print_rol("target", x)
        canvas.fill((255, 255, 255), camera2)
        canvas.blit(target.Value.Keuzes[x - 1], (260, 705))
        loop_pause(60)
        buttons = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        manual()

            if target.Value.Conditie - target.Value.Damage[x - 1][3] >= 0:
                button("keuze 1", 40, 725, 200, 40, red, green, Player_attack_fight, starter, target, x, 0)
                buttons += 1
            else:
                button("keuze1", 40, 725, 200, 40, red, red)
            if target.Value.Conditie - target.Value.Damage[x - 1][4] >= 0:
                button("keuze 2", 40, 770, 200, 40, red, green, Player_attack_fight, starter, target, x, 1)
                buttons += 1
            else:
                button("keuze2", 40, 725, 200, 40, red, red)
            if target.Value.Conditie - target.Value.Damage[x - 1][5] >= 0:
                button("keuze 3", 40, 815, 200, 40, red, green, Player_attack_fight, starter, target, x, 2)
                buttons += 1
            else:
                button("keuze3", 40, 725, 200, 40, red, red)
            pygame.display.flip()
            if buttons == 0:
                loop_pause(45)
                Player_attack_fight(starter, target, x, 3)
            clock.tick(10)
    canvas.fill(white, camera2)
    if choice < 3:
        dmg = target.Value.Damage[first_roll - 1][choice]
        target.Value.Conditie -= target.Value.Damage[first_roll - 1][choice + 3]
    else:
        dmg = 0
    print_dmg("target", dmg)
    loop_pause(60)
    y = Rol()
    loop_pause(30)
    print_rol("", y)

    choice = []
    for i in range(3):
        if (starter.Conditie - starter.Damage[y - 1][i + 3]) >= 0:
            choice.append(i)

    if len(choice) == 0:
        starter_dmg = 0
    elif len(choice) == 1:
        starter_dmg = starter.Damage[y - 1][choice[0]]
        starter.Conditie -= starter.Damage[y - 1][choice[0] + 3]
    else:
        rand = randint(0, len(choice) - 1)
        starter.Conditie -= starter.Damage[y - 1][rand + 3]
        starter_dmg = starter.Damage[y - 1][rand]

    print_dmg("", starter_dmg)
    loop_pause(60)
    Calc_parameters(starter, target, starter_dmg, dmg)


##
def Player_defense_fight(starter, target, first_roll=None, dmg=None, choice=None):
    # print Tegenstander rol
    loop_pause(30)
    if choice != None:
        if choice <= 2:
            starter_dmg = starter.Damage[first_roll - 1][choice]
            starter.Conditie -= starter.Damage[first_roll - 1][choice + 3]
        else:
            starter_dmg = 0
        print_dmg("", starter_dmg)
        loop_pause(90)
        Calc_parameters(starter, target, starter_dmg, dmg)

    if first_roll == None:
        y = Rol()
        loop_pause(30)
        print_rol("target", y)
        if target.Value.Player == True:
            choice = []
            for i in range(3):
                if (target.Value.Conditie - target.Value.Damage[y - 1][i + 3]) >= 0:
                    choice.append(i)

            if len(choice) == 0:
                dmg = 0
            elif len(choice) == 1:
                dmg = target.Value.Damage[y - 1][choice[0]]
                target.Value.Conditie -= target.Value.Damage[y - 1][choice[0]]
            else:
                rand = randint(0, len(choice) - 1)
                target.Value.Conditie -= target.Value.Damage[y - 1][rand + 3]
                dmg = target.Value.Damage[y - 1][rand]
        else:
            dmg = target.Value.Damage[y - 1]
        loop_pause(30)
        print_dmg("target", dmg)

    if first_roll == True:
        x = Rol()

    if first_roll == None:
        loop_pause(30)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        manual()
                    if event.key == pygame.K_SPACE:
                        Player_defense_fight(starter, target, True, dmg)

            canvas.fill((255, 255, 255), camera2)
            largeText = pygame.font.SysFont("comicsansms", 22)
            TextSurf, TextRect = text_objects("{} Roll the dice:".format(starter.Naam), largeText)
            TextRect.center = ((140), (725))
            gameDisplay.blit(TextSurf, TextRect)
            button("Gooi dobbelsteen", 40, 760, 200, 100, red, green, Player_defense_fight, starter, target, True, dmg)
            pygame.display.flip()
            clock.tick(10)
    elif choice == None:
        loop_pause(30)
        print_rol("", x)
        canvas.fill((255, 255, 255), camera2)
        canvas.blit(starter.Keuzes[x - 1], (260, 705))
        buttons = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        manual()
            if starter.Conditie - starter.Damage[x - 1][3] >= 0:
                button("keuze 1", 40, 725, 200, 40, red, green, Player_defense_fight, starter, target, x, dmg, 0)
                buttons += 1
            else:
                button("keuze1", 40, 725, 200, 40, red, red)
            if starter.Conditie - starter.Damage[x - 1][4] >= 0:
                button("keuze 2", 40, 770, 200, 40, red, green, Player_defense_fight, starter, target, x, dmg, 1)
                buttons += 1
            else:
                button("keuze2", 40, 770, 200, 40, red, red)
            if starter.Conditie - starter.Damage[x - 1][5] >= 0:
                button("keuze 3", 40, 815, 200, 40, red, green, Player_defense_fight, starter, target, x, dmg, 2)
                buttons += 1
            else:
                button("keuze3", 40, 815, 200, 40, red, red)
            pygame.display.flip()
            if buttons == 0:
                loop_pause(45)
                Player_defense_fight(starter, target, x, dmg, 3)

            clock.tick(10)


def Player_vs_player_fight(starter, target, tar_first_roll=None, tar_choice=None, dmg=None, start_first_roll=None,
                           start_choice=None):
    loop_pause(30)
    if start_choice != None:
        if start_choice in [0, 1, 2]:
            starter.Conditie -= starter.Damage[start_first_roll - 1][start_choice + 3]
            starter_dmg = starter.Damage[start_first_roll - 1][start_choice]
        else:
            starter_dmg = 0
        canvas.fill(white, camera2)
        loop_pause(20)
        print_dmg("", starter_dmg)
        pygame.display.flip()
        loop_pause(90)
        Calc_parameters(starter, target, starter_dmg, dmg)

    if tar_first_roll == True and tar_first_roll != False:
        y = Rol()
    if start_first_roll == True and start_first_roll != False:
        x = Rol()
    if tar_choice in [0, 1, 2] and dmg == None:
        target.Value.Conditie -= target.Value.Damage[tar_first_roll - 1][tar_choice + 3]
        dmg = target.Value.Damage[tar_first_roll - 1][tar_choice]
    elif tar_choice == 3:
        dmg = 0
    go = True
    if tar_first_roll == None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        manual()
                    if event.key == pygame.K_SPACE:
                        Player_vs_player_fight(starter, target, True)

            canvas.fill((255, 255, 255), camera2)
            largeText = pygame.font.SysFont("comicsansms", 22)
            TextSurf, TextRect = text_objects("{} Roll the dice:".format(target.Value.Naam), largeText)
            TextRect.center = ((140), (725))
            gameDisplay.blit(TextSurf, TextRect)
            button("Gooi dobbelsteen", 40, 760, 200, 100, red, green, Player_vs_player_fight, starter, target, True)
            pygame.display.flip()
            clock.tick(10)

    elif tar_choice == None:
        print_rol("target", y)
        loop_pause(30)
        canvas.fill((255, 255, 255), camera2)
        canvas.blit(target.Value.Keuzes[y - 1], (260, 705))
        buttons = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        manual()

            if (target.Value.Conditie - target.Value.Damage[y - 1][3]) < 0:
                button("keuze1", 40, 725, 200, 40, red, red)
            else:
                button("keuze 1", 40, 725, 200, 40, red, green, Player_vs_player_fight, starter, target, y, 0)
                buttons += 1
            if (target.Value.Conditie - target.Value.Damage[y - 1][4]) < 0:
                button("keuze2", 40, 770, 200, 40, red, red)
            else:
                button("keuze 2", 40, 770, 200, 40, red, green, Player_vs_player_fight, starter, target, y, 1)
                buttons += 1
            if (target.Value.Conditie - target.Value.Damage[y - 1][5]) < 0:
                button("keuze3", 40, 815, 200, 40, red, red)
            else:
                button("keuze 3", 40, 815, 200, 40, red, green, Player_vs_player_fight, starter, target, y, 2)
                buttons += 1
            pygame.display.flip()
            if buttons == 0:
                loop_pause(60)
                Player_vs_player_fight(starter, target, y, 3)
            clock.tick(10)
    elif start_first_roll == None:
        print_dmg("target", dmg)
        canvas.fill((255, 255, 255), camera4)
        canvas.fill((255, 255, 255), camera2)
        loop_pause(30)
        while go:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        manual()
                    if event.key == pygame.K_SPACE:
                        Player_vs_player_fight(starter, target, False, False, dmg, True)

            largeText = pygame.font.SysFont("comicsansms", 22)
            TextSurf, TextRect = text_objects("{} Roll the dice:".format(starter.Naam), largeText)
            TextRect.center = ((140), (725))
            gameDisplay.blit(TextSurf, TextRect)
            button("Gooi dobbelsteen", 40, 760, 200, 100, red, green, Player_vs_player_fight, starter, target, False,
                   False, dmg, True)
            pygame.display.flip()

            clock.tick(10)
    elif start_choice == None:
        print_rol(True, x)
        loop_pause(30)
        canvas.fill((255, 255, 255), camera2)
        canvas.blit(starter.Keuzes[x - 1], (260, 705))
        buttons = 0
        while go:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        manual()
            if (starter.Conditie - starter.Damage[x - 1][3]) >= 0:
                button("keuze 1", 40, 725, 200, 40, red, green, Player_vs_player_fight, starter, target, False, False,
                       dmg,
                       x, 0)
                buttons += 1
            else:
                button("keuze2", 40, 725, 200, 40, red, red)
            if (starter.Conditie - starter.Damage[x - 1][4]) >= 0:
                button("keuze 2", 40, 770, 200, 40, red, green, Player_vs_player_fight, starter, target, False, False,
                       dmg, x, 1)
                buttons += 1
            else:
                button("keuze2", 40, 770, 200, 40, red, red)
            if (starter.Conditie - starter.Damage[x - 1][5]) >= 0:
                button("keuze 3", 40, 815, 200, 40, red, green, Player_vs_player_fight, starter, target, False, False,
                       dmg, x, 2)
                buttons += 1
            else:
                button("keuze3", 40, 815, 200, 40, red, red)
            pygame.display.flip()
            if buttons == 0:
                loop_pause(60)
                Player_vs_player_fight(starter, target, False, False, dmg, x, 3)
            clock.tick(10)


def Ai_fight(starter, target):
    x = Rol()
    print_rol("target", x)

    if target.Value.Player == True:
        choice = []
        for i in range(3):
            if (target.Value.Conditie - target.Value.Damage[x - 1][i + 3]) >= 0:
                choice.append(i)

        if len(choice) == 0:
            dmg = 0
        elif len(choice) == 1:
            dmg = target.Value.Damage[x - 1][choice[0]]
            target.Value.Conditie -= target.Value.Damage[x - 1][choice[0]]
        else:
            rand = randint(0, len(choice) - 1)
            target.Value.Conditie -= target.Value.Damage[x - 1][rand + 3]
            dmg = target.Value.Damage[x - 1][rand]
    else:
        dmg = target.Value.Damage[x - 1]
    print_dmg("target", dmg)
    loop_pause(90)
    y = Rol()
    print_rol("", y)

    choice = []
    for i in range(3):
        if (starter.Conditie - starter.Damage[y - 1][i + 3]) >= 0:
            choice.append(i)

    if len(choice) == 0:
        starter_dmg = 0
    elif len(choice) == 1:
        starter_dmg = starter.Damage[y - 1][choice[0]]
        starter.Conditie -= starter.Damage[y - 1][choice[0] + 3]
    else:
        rand = randint(0, len(choice) - 1)
        starter.Conditie -= starter.Damage[y - 1][rand + 3]
        starter_dmg = starter.Damage[y - 1][rand]

    print_dmg("", starter_dmg)
    loop_pause(90)
    Calc_parameters(starter, target, starter_dmg, dmg)


def Calc_parameters(starter, target, start_dmg, target_dmg):
    if target_dmg - start_dmg <= 0:
        i = 1  # TODO
    else:
        starter.Levenspunten = starter.Levenspunten - (target_dmg - start_dmg)
        if starter.Levenspunten <= 0:
            starter.dead = True
            pygame.mixer.music.load("content/soundeffects/dead1.wav")
            pygame.mixer.music.play(1, 0.0)
            loop_pause(25)
            Dead(starter.Kleur)
            game_loop(False)
        else:
            canvas.fill((255, 255, 255), camera5)
            canvas.blit(hp_dict["HP_{}".format(starter.Levenspunten)], (103, 280))
            pygame.display.update(camera5)
    if target.Value.Player:
        canvas.fill((255,255,255), camera7)
        if target.Value.Conditie<0:
            target.Value.Conditie=0
        canvas.blit(cp_dict["CP_{}".format(target.Value.Conditie)], (365, 350))
        pygame.display.update(camera7)

    canvas.fill((255,255,255), camera6)
    canvas.blit(cp_dict["CP_{}".format(starter.Conditie)], (103, 350))
    pygame.display.update(camera6)

    loop_pause(60)
    Change_turn()
    game_loop(False)


##Returns
def Return_same_location(List, player_location, player_kleur):
    locations = []
    while not List.IsEmpty:
        if List.Value.Locatie.Position == player_location and List.Value.Kleur != player_kleur:
            locations.append(List.Value.Locatie.Position)
            return List, locations
        List = List.Tail
    return None, []


def Dead(Lijst, player_kleur):
    pass


def Return_random_element(List):
    for i in range(randint(0, 17)):
        List = List.Tail
    return List


def Return_bepaalde_player(tile_kleur):
    if tile_kleur == 6:
        return player1
    elif tile_kleur == 7:
        return player2
    elif tile_kleur == 8:
        return player3
    else:
        return player4


## Dood process
def Dead(player_kleur):
    global beurt, players
    List = It_remove_dead(players, player_kleur)
    players = List
    length, kleuren = lengthNamen(players)
    death_screen(player_kleur, 30)
    beurt = Bepaal_beurt(players, player_kleur, length, kleuren)


def It_remove_dead(List, kleur):
    if List.IsEmpty:
        return Empty
    elif List.Value.Kleur == kleur:
        return It_remove_dead(List.Tail, kleur)
    elif List.Value.Kleur != kleur:
        return Node(List.Value, It_remove_dead(List.Tail, kleur))


def lengthNamen(List):
    count = 0
    kleuren = []
    while not List.IsEmpty:
        count += 1
        kleuren.append(List.Value.Kleur)
        List = List.Tail
    return count, kleuren


def TailList(aantal):
    if aantal == 1:
        return players.Tail
    if aantal == 2:
        return players.Tail.Tail


def Bepaal_beurt(List, kleur, length, levend):
    if kleur == 9 or kleur == 6:
        return List
    elif kleur == 8:
        if 9 in levend:
            return TailList(length - 1)
        else:
            return List
    else:
        if 6 in levend and 8 in levend:
            return TailList(length - 2)
        return List


##Loops
def loop_pause(aantal):
    count = 0
    while count < aantal:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_screen()
                if event.key == pygame.K_h:
                    manual()

        count = count + 1
        clock.tick(60)


def pause_screen():
    global pause

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        largeText = pygame.font.SysFont("comicsansms", 40)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((350), (150))
        gameDisplay.blit(TextSurf, TextRect)

        button("Sounds:", 90, 220, 150, 50, white, white)
        button("On", 250, 220, 50, 50, red, white, Set_music, 1)
        button("Off", 375, 220, 50, 50, red, white, Set_music, 0)

        button("Continue", 90, 500, 150, 50, green, bright_green, game_loop, False)
        button("Back to menu", 275, 500, 150, 50, green, bright_green, game_intro)
        button("Quit Game", 460, 500, 150, 50, red, bright_red, quitgame)

        pygame.display.update(mid_camera)
        clock.tick(15)


def winning_screen(kleur):
    global pause

    canvas.fill(white, mid_camera)

    if kleur == 6:
        b = pygame.image.load("content/__pawn_green.png")
        b = pygame.transform.scale(b, (175, 175))
        canvas.blit(b, (275, 260))
    elif kleur == 7:
        y = pygame.image.load("content/__pawn_yellow.png")
        y = pygame.transform.scale(y, (175, 175))
        canvas.blit(y, (275, 260))
    elif kleur == 8:
        g = pygame.image.load("content/__pawn_blue.png")
        g = pygame.transform.scale(g, (175, 175))
        canvas.blit(g, (275, 260))
    elif kleur == 9:
        r = pygame.image.load("content/__pawn_red.png")
        r = pygame.transform.scale(r, (175, 175))
        canvas.blit(r, (275, 260))

    pygame.mixer.music.load("content/soundeffects/winningscreen.wav")
    pygame.mixer.music.play(0, 0)
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_intro()

        largeText = pygame.font.SysFont("comicsansms", 40)
        TextSurf, TextRect = text_objects("{} is de winnaar!".format(players.Value.Naam), largeText)
        TextRect.center = ((350), (200))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play again", 150, 500, 150, 50, green, bright_green, game_loop, "reset")
        button("Play again", 150, 500, 150, 50, green, bright_green, game_intro)
        button("Quit Game", 400, 500, 150, 50, red, bright_red, quitgame)

        pygame.display.update(mid_camera)
        clock.tick(10)


def game_intro():
    pygame.mixer.music.load("Content/Rocky Theme Tune (8 Bit Remix).wav")
    pygame.mixer.music.play(-1, 0)
    gameDisplay.fill(white)
    backdrop = pygame.image.load("content/logo.png")
    gameDisplay.blit(backdrop, (0, 0))


    bg = pygame.image.load("Content/boxing glove 2.png").convert_alpha()
    ab = pygame.image.load("Content/boxing glove1.png").convert_alpha()

    bg = pygame.transform.scale(bg, (225, 240))
    ab = pygame.transform.scale(ab, (225, 240))

    gameDisplay.blit(bg, (580, 450))
    gameDisplay.blit(ab, (190, 450))

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        logo = pygame.image.load("content/logootje.png")
        logo = pygame.transform.scale(logo, (700, 143))
        canvas.blit(logo,(170,200))

        button("Start Game", 225, 400, 150, 50, green, bright_green, game_loop, True)
        button("Quit Game", 425, 500, 150, 50, red, bright_red, quitgame)
        button("Help", 625, 400, 150, 50, green, bright_green, manual)
        button("settings", 425, 400, 150, 50, green, bright_green, settings)

        pygame.display.update()
        clock.tick(15)


def settings():
    global pause
    gameDisplay.fill(white)

    txt = pygame.font.SysFont("verdana", 25)
    largeText = pygame.font.SysFont("verdana", 50)
    close_down = False

    while not close_down:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        canvas.fill(white)
        button("back", 25, 500, 150, 50, green, bright_green, game_intro)
        button("Players:", 125, 150, 150, 50, white, white)
        button("1", 320, 150, 75, 50, red, white, Player_select, 1)
        button("2", 445, 150, 75, 50, red, white, Player_select, 2)
        button("3", 570, 150, 75, 50, red, white, Player_select, 3)
        button("4", 695, 150, 75, 50, red, white, Player_select, 4)

        button("Music:", 125, 220, 150, 50, white, white)
        button("On", 320, 220, 75, 50, red, white, Set_music, 1)
        button("Off", 445, 220, 75, 50, red, white, Set_music, 0)

        TextSurf, TextRect = text_objects("settings", largeText)
        TextRect.center = ((display_width / 6), (display_height / 10))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Spelers:", largeText)
        TextRect.center = ((125), (325))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("{}".format(player1.Value.Naam), txt, green)
        TextRect.center = ((365), (325))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("{}".format(player2.Value.Naam), txt, yellow)
        TextRect.center = ((365), (375))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("{}".format(player3.Value.Naam), txt, blue)
        TextRect.center = ((365), (425))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("{}".format(player4.Value.Naam), txt, red)
        TextRect.center = ((365), (475))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(15)


def manual():
    webbrowser.open_new(r'content\Manual.pdf')


def death_screen(kleur, aantal):
    global pause
    count = 0

    canvas.fill(white, mid_camera)
    if kleur == 6:
        b = pygame.image.load("content/__pawn_green.png")
        b = pygame.transform.scale(b, (175, 175))
        canvas.blit(b, (275, 260))
    elif kleur == 7:
        y = pygame.image.load("content/__pawn_yellow.png")
        y = pygame.transform.scale(y, (175, 175))
        canvas.blit(y, (275, 260))
    elif kleur == 8:
        g = pygame.image.load("content/__pawn_blue.png")
        g = pygame.transform.scale(g, (175, 175))
        canvas.blit(g, (275, 260))
    elif kleur == 9:
        r = pygame.image.load("content/__pawn_red.png")
        r = pygame.transform.scale(r, (175, 175))
        canvas.blit(r, (275, 260))

    while count < aantal:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_intro()

        largeText = pygame.font.SysFont("comicsansms", 40)
        TextSurf, TextRect = text_objects("{} Died!".format(beurt.Value.Naam), largeText)
        TextRect.center = ((350), (200))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update(mid_camera)
        count += 1
        clock.tick(15)


def game_loop(start=None):
    ai_count = 0
    global pause, loops, beurt, players, aantal_spelers
    if start == "reset":
        players = None
        Player_select(aantal_spelers)
    if start  or start == "reset":
        pygame.mixer.music.stop()
        if players.Value.Kleur != 6:
            players = Turn_list(players)
        beurt = players
        loops = 0
        Reprint()
        print_players(1, 1, 1, 1)
        pygame.display.flip()
    Reprint()
    print_players(1, 1, 1, 1)
    pygame.display.flip()
    if players.Tail.IsEmpty:
        winning_screen(players.Value.Kleur)
    TurnPicture()
    gameExit = False
    largeText = pygame.font.SysFont("comicsansms", 22)
    loop_pause(45)
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_screen()
                if event.key == pygame.K_h:
                    manual()
                if event.key == pygame.K_SPACE:
                    Bewegen(beurt.Value)

        canvas.fill(white,camera2)
        if beurt.Value.Ai == 1 and ai_count > 45:
            Bewegen(beurt.Value)
        if beurt.Value.Ai==0:
            TextSurf, TextRect = text_objects("{} Roll the dice:".format(beurt.Value.Naam), largeText)
            TextRect.center = ((140), (725))
            gameDisplay.blit(TextSurf, TextRect)
            button("Gooi dobbelsteen", 40, 760, 200, 100, red, green, Bewegen, beurt.Value, )
        print_players_info()
        TurnPicture()
        pygame.display.flip()
        if loops == 5:
            loops = 0
        ai_count += 1
        clock.tick(10)


## START
Set_music(1)
Player_select(0)
game_intro()
