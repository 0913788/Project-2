import pygame
from Node import *

class Point:
  def __init__(self, x, y):
    self.X = x
    self.Y = y

  def __str__(self):
      return "({},{})".format(self.X,self.Y)

class Tile:
    def __init__(self, position, type, moveable, texture, offset):
        self.Position = position
        self.Type = type
        self.Moveable = moveable

        self.DefaultTexture = pygame.image.load(texture).convert()
        self.Offset = offset

        self.Right=None
        self.Up= None
        self.Left= None
        self.Down = None
        self.Next = None

        self.Printed = False
        self.Loops =  None


    def Draw(self, screen):
        if self.Printed==True:
            return

        _width = int(self.Offset / 3)
        if self.Type==2:
            dim=-20
        elif self.Type ==5:
            dim=519
        else: dim = 39

        screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width + dim)),
                    (_width + self.Position.X * self.Offset, _width + self.Position.Y * self.Offset))

        self.Printed=True

        if (self.Up!=None and self.Up.Printed!=True):
            self.Up.Draw(screen)
        elif (self.Left!=None and self.Left.Printed!=True):
            self.Left.Draw(screen)
        elif (self.Down!=None and self.Down.Printed!=True):
            self.Down.Draw(screen)
        elif (self.Right!=None and self.Right.Printed!=True):
            self.Right.Draw(screen)


    def Reset(self,loops):
        if self.Printed == True:
           self.Printed =False
        if self.Loops == loops:
            return

        if self.Up != None and self.Up.Loops!=loops:
            self.Loops=loops
            self.Up.Reset(loops)
        elif self.Left != None and self.Left.Loops!=loops:
            self.Loops=loops
            self.Left.Reset(loops)

        elif self.Down != None and self.Down.Loops!=loops:
            self.Loops=loops
            self.Down.Reset(loops)

        elif self.Right != None and self.Right.Loops!=loops:
            self.Loops=loops
            self.Right.Reset(loops)
        else:
            self.Loops=loops
            self.Reset(loops)

def build_square_matrix(dimension, offset):
    board=None
    p1=None
    p2=None
    p3=None
    p4=None

    above = None
    prev_node = None

    for row in range(dimension):
        for column in range(dimension):


            if (row == 0 and column==1) or (row==0 and column==0) or (row==1 and column==0):
                node=Tile(Point(column,row), 0, True, "Content\_green_pixel.png",offset)

            elif (row == 0 and column==dimension-1) or (row == 1 and column==dimension-1) or (row == 0 and column==dimension-2):
                node=Tile(Point(column,row), 0, True, "Content\_gray_pixel.png",offset)

            elif (row == dimension-2 and column==dimension-1) or (row == dimension-1 and column==dimension-1) or (row == dimension-1 and column==dimension-2):
                node=Tile(Point(column,row), 0, True, "Content\_blue_pixel.png",offset)

            elif (row == dimension-1 and column==0) or (row == dimension-2and column==0) or (row == dimension-1 and column==1):
                node=Tile(Point(column,row), 0, True, "Content\_red_pixel.png",offset)

            elif row==(dimension-1)/2 and column==(dimension-1)/2:
                node=Tile(Point(column,row), 2, True, "Content\_fight.png",offset)
            elif (row==0 or row == (dimension-1)/2) and (column==0 or column==(dimension-1)/2):
                node=Tile(Point(column,row), 1, True, "Content\_fight.png",offset)
            elif (row==dimension-1 or row == (dimension-1)/2) and (column==dimension-1 or column==(dimension-1)/2):
                node=Tile(Point(column,row), 1, True, "Content\_fight.png",offset)

            elif (row == 0 or row == dimension-1) or (column == 0 or column == dimension-1):
                node=Tile(Point(column,row), 0, True, "Content\white_pixel.png",offset)

            elif row==1 and column==1:
                node=Tile(Point(column,row), 5, False, "content\_ring.png",offset)

            else:
                node=Tile(Point(column,row), 2, False, "Content\white_pixel.png",offset)

            if row == 0 and column == 0:
                p1,board = node, node
                node.Next=1
            if row == 0 and column == dimension-1:
                p2 = node
                node.Next=2
            if row == dimension-1 and column == dimension-1:
                p3 = node
                node.Next=3
            if row == dimension-1 and column == 0:
                p4 = node
                node.Next=4

            if column == 0:
                prev_node = node
            else:
                prev_node.Right = node
                node.Left = prev_node
                prev_node = node

            if(row > 0):
                node.Up = above
                above.Down = node
                above= above.Right

        while prev_node.Left != None:
            prev_node = prev_node.Left
        above = prev_node


    return board,p1, p2, p3, p4
