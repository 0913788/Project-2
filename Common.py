from random import randint

from Node import *

##COLORS
white = (255, 255, 255)
red = (225, 0, 0)
green = (0, 215, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
block_color = (53, 115, 255)


def text_objects(text, font, color=None):
    if color == None:
        textSurface = font.render(text, True, black)
    else:
        textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def Rol():
    x = randint(1, 6)
    return x


def Turn_list(List):
    newlist = Empty
    while not List.IsEmpty:
        if not List.IsEmpty:
            newlist = Node(List.Value, newlist)
        List = List.Tail
    return newlist


def Return_player(player_kleur):
    if player_kleur == 6:
        return 0, 1, 1, 1
    elif player_kleur == 7:
        return 1, 0, 1, 1
    elif player_kleur == 8:
        return 1, 1, 0, 1
    else:
        return 1, 1, 1, 0
