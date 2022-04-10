import pygame  #importib faili pygame-i
#GitHUBi link https://github.com/PapaStalka/Pygamei-harjutused/blob/2a79116743b53c302345f1ee8681d868076a6259/%C3%9Clesanne1_Tiik

#Foor
pygame.init() #käivitab pygamei
screen=pygame.display.set_mode([300,300]) # tekitab akna suurusega 300x300
pygame.display.set_caption("Foor - Karlos Tiik") # kuvab ekraani nime
screen.fill([0,0,0]) # muudab taustavärvi mustaks
pygame.draw.rect(screen, [127, 127, 127], [100, 10, 100, 275], 2) #joonistab ekraanile ristküliku suurusega 150x300, täpselt keskele, ning joonepaksus on 2 ja värvus hall
pygame.draw.circle(screen, [255, 0, 0], [150, 60], 39, 0) # joonistab ekraanile rohelist värvi ringi, raadiusega 45, ning värvib ringi seest ära
pygame.draw.circle(screen, [255, 255, 0], [150, 145], 39, 0) # joonistab ekraanile kollast värvi ringi, rohelise ringi alla, ning värvib selle seest ära
pygame.draw.circle(screen, [0, 255, 0], [150, 235], 39, 0) # joonistab ekraanile punast värvi ringi, kollase ringi alla, ristküliku sisse, ning värvib selle seest ära.
pygame.display.flip() # värskendab ekraani

from sys import exit #impordib sys-ist pygamei exit-i
while True: # alustab while tsükklit
        for event in pygame.event.get(): # registreerib kõik kasutaja sündmused
            if event.type == pygame.QUIT: # seab paika tingumuse et kui kasutaja sündmus on võrdeline pygamei sulgemisega, siis
                pygame.quit() # suleb pygame-i akna
                exit() # lõpetab tsükli