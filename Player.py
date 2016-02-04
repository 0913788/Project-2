import pygame

global screen, offset, camera1, player1, player2, player3, player4, Board, canvas


class Player:
    def __init__(self, naam, kleur, locatie, texture, fightTexture, face_text):

        self.Naam = naam
        self.Kleur = kleur
        self.Levenspunten = 100
        self.Conditie = 15
        self.Locatie = locatie
        self.FightTexture = self.Convert(fightTexture)
        self.Texture = pygame.image.load(texture).convert_alpha()
        self.FaceTexture = self.Face_convert(face_text)
        self.Richting = None
        self.Damage = self.Define_dmg(kleur)
        self.Keuzes = self.Create_keuze(kleur)
        self.Ai = 0
        self.Player = True
        self.NextTexture, self.TurnTexture = self.turntexture()
        self.dead = False

    def Create_keuze(self, kleur):
        keuzes = []
        if kleur == 6:
            x = 1
        elif kleur == 7:
            x = 2
        elif kleur == 8:
            x = 3
        else:
            x = 4
        for i in range(6):
            img = pygame.image.load("content/players/keuzes/{}.{}.png".format(x, i + 1))
            img = pygame.transform.scale(img, (200, 150))
            keuzes.append(img)
        return keuzes

    def Face_convert(self, texture):
        img = pygame.image.load(texture).convert_alpha()
        img = pygame.transform.scale(img, (150, 150))
        return img

    def Convert(self, texture):
        img = pygame.image.load(texture).convert_alpha()
        img = pygame.transform.scale(img, (280, 300))
        return img

    def Define_dmg(self, kleur):
        if kleur == 6:
            damage = [(1, 9, 19, 1, 2, 3), (5, 11, 15, 2, 3, 5), (7, 12, 16, 2, 3, 4), (2, 4, 6, 1, 2, 3),
                      (10, 20, 30, 2, 5, 8), (8, 13, 17, 3, 4, 5)]
        elif kleur == 7:
            damage = [(8, 13, 17, 3, 4, 5), (10, 20, 30, 2, 5, 8), (5, 11, 15, 2, 3, 5), (3, 9, 19, 1, 2, 3),
                      (2, 4, 6, 1, 2, 3), (7, 12, 16, 2, 3, 4)]
        elif kleur == 8:
            damage = [(5, 11, 15, 2, 3, 5), (3, 9, 19, 1, 2, 3), (2, 4, 6, 1, 2, 3), (7, 12, 16, 2, 3, 4),
                      (8, 13, 17, 3, 4, 5), (10, 20, 30, 3, 3, 3)]
        else:
            damage = [(10, 20, 30, 2, 5, 8), (8, 13, 17, 3, 4, 5), (3, 9, 19, 1, 2, 3), (5, 11, 15, 2, 3, 5),
                      (7, 12, 16, 2, 3, 4), (2, 4, 6, 1, 2, 3)]
        return damage

    def Convert(self, texture):
        img = pygame.image.load(texture).convert_alpha()
        img = pygame.transform.scale(img, (280, 300))
        return img

    def turntexture(self):
        # content/Turn/Player_x.png
        if self.Kleur == 6:
            image = pygame.image.load("content/Turn/Player_1.png").convert_alpha()
            image2 = pygame.image.load("content/Turn/Next_player_1.png").convert_alpha()
        elif self.Kleur == 7:
            image = pygame.image.load("content/Turn/Player_2.png").convert_alpha()
            image2 = pygame.image.load("content/Turn/Next_player_2.png").convert_alpha()
        elif self.Kleur == 8:
            image = pygame.image.load("content/Turn/Player_3.png").convert_alpha()
            image2 = pygame.image.load("content/Turn/Next_player_3.png").convert_alpha()
        else:
            image = pygame.image.load("content/Turn/Player_4.png").convert_alpha()
            image2 = pygame.image.load("content/Turn/Next_player_4.png").convert_alpha()
        image = pygame.transform.scale(image, (200, 100))
        image2 = pygame.transform.scale(image2, (200, 100))
        return image2, image

    def draw(self, screen, offset):
        _width = int(34)
        screen.blit(pygame.transform.scale(self.Texture, (_width, _width)),
                    (_width + self.Locatie.Position.X * offset,
                     _width + self.Locatie.Position.Y * offset))
