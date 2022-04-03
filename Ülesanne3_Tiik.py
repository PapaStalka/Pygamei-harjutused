import pygame #importib faili pygame-i
#
pygame.init() #käivitab pygamei
red = [255, 0, 0] # punase värvi rgb kood
green = [153, 255, 153] # helerohelise värvi rgb kood
screen=pygame.display.set_mode([640,480])  # tekitab akna suurusega 640x480
pygame.display.set_caption("Ülesanne 3") # kuvab ekraani nime
screen.fill(green) # muudab taustavärvi roheliseks
pygame.display.flip() # värskendab ekraani

def ruudustik(ruudusuurus, joonte_varv, veergude_arv, ridade_arv): # hakatakse defineerima funktsiooni "ruudustik"
    ridade_arv = (ridade_arv * 20) # tehakse argumendi väärtus piksliteks, ehk 1 rida on 20 pikslit
    veergude_arv = (veergude_arv * 20) # tehakse argumendi väärtus piksliteks, ehk 1 veerg on 20 pikslit
    for x in range(0, ridade_arv, ruudusuurus): # alustatakse tsüklit, kuni täidetakse ära terve terve ridade arv ruudustiku suuruses
        for y in range(0, veergude_arv, ruudusuurus): # alustatakse tsüklit, kuni täidetakse ära terve terve veergude arv ruudustiku suuruses
            ruut = pygame.Rect(x, y, ruudusuurus, ruudusuurus) # joonistatava ruudu andmed
            pygame.draw.rect(screen, joonte_varv, ruut, 1) # joonistatakse ekraanile ruudud
            
ruudustik(20, red, 24, 32) # kutsub välja funktsiooni, ning joonistatakse ekraanile ruudustik
pygame.display.flip() # värskendab ekraani

from sys import exit #impordib sys-ist pygamei exit-i
while True: # alustab while tsükklit
        for event in pygame.event.get(): # registreerib kõik kasutaja sündmused
            if event.type == pygame.QUIT: # seab paika tingumuse et kui kasutaja sündmus on võrdeline pygamei sulgemisega, siis
                pygame.quit() # suleb pygame-i akna
                exit() # lõpetab tsükli
