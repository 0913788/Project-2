import pygame
import time

global screen,offset,camera1,player1,player2,player3,player4,Board,canvas

class Player:
    def __init__(self,naam,kleur,locatie,texture,fightTexture,face_text):
        self.Naam=naam
        self.Kleur = kleur
        self.Levenspunten = 100
        self.Conditie = 15
        self.Locatie =locatie
        self.FightTexture=self.Convert(fightTexture)
        self.Texture =pygame.image.load(texture).convert_alpha()
        self.FaceTexture = self.Face_convert(face_text)
        self.Richting=None
        self.Keuzes = self.Create_keuze(kleur)
        self.Damage=self.Define_dmg(kleur)
        self.Ai=0
        self.Player=True
        self.TurnTexture = self.turntexture()


        # pygame.transform.scale(self.Texture(200,200))
    def Keys(self):
        keys = pygame.key.get_pressed()
        return keys

    def turntexture(self):
        # content/Turn/Player_x.png
        if   self.Kleur == 6:
            image =  pygame.image.load("content/Turn/Player_1.png").convert()
        elif self.Kleur == 7:
            image = pygame.image.load("content/Turn/Player_2.png").convert()
        elif self.Kleur == 8:
            image = pygame.image.load("content/Turn/Player_3.png").convert()
        else:
            image = pygame.image.load("content/Turn/Player_4.png").convert()
        return image


    def Define_dmg(self,kleur):
        if kleur == 6:
            damage=[(1,9,19,1,2,3),(5,11,15,2,3,5),(7,12,16,2,3,4),(2,4,6,1,2,3),(10,20,30,2,5,8),(8,13,17,3,4,5)]
        elif kleur == 7:
            damage=[(8,13,17,3,4,5),(10,20,30,2,5,8),(5,11,15,2,3,5),(3,9,19,1,2,3),(2,4,6,1,2,3),(7,12,16,2,3,4)]
        elif kleur == 8:
            damage=[(5,11,15,2,3,5),(3,9,19,1,2,3),(2,4,6,1,2,3),(7,12,16,2,3,4),(8,13,17,3,4,5),(10,20,30,3,3,3)]
        else:
            damage=[(10,20,30,2,5,8),(8,13,17,3,4,5),(3,9,19,1,2,3),(5,11,15,2,3,5),(7,12,16,2,3,4),(2,4,6,1,2,3)]
        return damage

    def Convert(self,texture):
        img = pygame.image.load(texture).convert_alpha()
        img = pygame.transform.scale(img,(280,300))
        return img

    def Fight(self,target):
        pass

    def draw(self, screen, offset):
       _width = int(34)
       screen.blit(pygame.transform.scale(self.Texture, (_width, _width)),
                (_width + self.Locatie.Position.X * offset,
                _width + self.Locatie.Position.Y * offset))
    
    def Face_convert(self, texture):
        img = pygame.image.load(texture).convert_alpha()
        img = pygame.transform.scale(img, (150, 150))
        return img

