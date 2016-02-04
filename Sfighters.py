from Node import *
import pygame


class Superfighter:
    def __init__(self, naam, damage, texture,mid_text):
        self.Naam = naam
        self.Damage = damage
        self.FightTexture = self.Convert(texture)
        self.MidTexture=self.Mid_convert(mid_text)
        self.FaceTexture = self.Face_convert(face_text)
        self.Ai=True
        self.Player=False
    
    def Face_convert(self, texture):
        img = pygame.image.load(texture).convert_alpha()
        img = pygame.transform.scale(img, (150, 150))
        return img
    
    def Mid_convert(self,texture):
        img =pygame.image.load(texture).convert_alpha()
        img = pygame.transform.scale(img,(150,150))
        return img

    def Convert(self,texture):
        img =pygame.image.load(texture).convert_alpha()
        img = pygame.transform.scale(img,(280,300))
        return img



def create_fighters():
    name_fighter = ['Terry crews','Jason Statham','Wesley Sniper','Jet Ri','Steve Seagal','Super Merio',
                 'Vin Dieser', 'Chack Norris', 'The roch','James Bend','Ernold Schwarzenegger','Steve Urkel','Dexter',
                'Pariz Hilten','John Cena','Agua Man','Jackie Chen','Bruce Hee']

    damage_fighter = [(10,15,25,20,15,10),(15,17,19,21,23,26),(10,12,14,16,14,12),(10,30,12,25,14,23),(10,15,12,11,25,20),
                      (10,10,30,30,15,15),(20,25,30,25,20,15),(15,28,27,25,29,30),(13,28,30,17,10,7),(25,15,15,7,20,25),
                      (25,25,20,15,15,10),(10,5,12,11,15,8),(9,8,7,15,13,9),(12,8,7,15,13,9),(10,6,25,7,8,11),(12,15,9,7,7,13),
                      (12,10,15,9,10,25),(20,15,5,7,8,26)]

    Texture = ["terry_crews","jason_statham","wesley_sniper","jet_ri","steve_seagal","super_merio","vin_dieser","chack_norris"
        ,"the_roch","james_bend","ernold_schwarzenegger","steve_urkel","dexter","pariz_hilten","john_cena","agua_man","jackie_chen","bruce_hee"]
        
    Face = ["Terry Crews", "Jason Statham", "Wesely Sniper", "Jet Ri", "Steven Seagal", "Super Merio", "Vin Dieser",
            "Chack Norris", "The Roch"
        , "james bend", "ernold swarzenegger", "steve urkel", "dexter", "pariz hilten", "john cena", "agua man",
            "jackie chen", "bruce hee"]

    super_fighters = Empty
    for i in range(len(name_fighter and damage_fighter)):
        super_fighters = Node(Superfighter(name_fighter[i],damage_fighter[i],"content/superfighters/{}.png".format(Texture[i]),"content/superfighters/Mid_fight/Wesely Sniper.png","content/superfighters/Mid_fight/{}.png".format(Face[i])), super_fighters)

    return super_fighters
