import pygame  #importib faili pygame-i
pygame.init() #käivitab pygamei
screen=pygame.display.set_mode([300,300]) # tekitab akna suurusega 300x300
pygame.display.set_caption("Lumemees - Karlos Tiik") # kuvab ekraani nime
screen.fill([0,0,0]) #muudab taustavärvi mustaks

pygame.draw.circle(screen, [255, 255, 255], [150, 75], 30, 0) # joonistab ekraanile valge ringi, koordinaatidega 150, 75 ja raadiuseks on 30
pygame.draw.circle(screen, [255, 255, 255], [150, 140], 40, 0) # joonistab ekraanile valge ringi, koordinaatidega 150 ja 140, ning raadius on 40
pygame.draw.circle(screen, [255, 255, 255], [150, 225], 50, 0) # joonistab ekraanile valge ringi, koordinaatidega 150 ja 225, ning raadiuseks on 50
pygame.draw.circle(screen, [0, 0, 0], [140, 70], 5, 0) # joonistab ekraanile musta ringi, esimese valge ringi peale, koordinaatidega 140 ja 70, ning raadiuseks on 5
pygame.draw.circle(screen, [0, 0, 0], [160, 70], 5, 0) # joonistab ekraanile musta ringi, esimese valge ringi peale, koordinaatidega 160 ja 70, ning raadiuseks on 5
pygame.draw.polygon(screen, (255, 0, 0), [(145, 80), (155, 80), (150, 95)]) # joonistab ekraanile punase kolmnurga, valge ringi peale
pygame.display.flip() # värskendab ekraani

from sys import exit #impordib sys-ist pygamei exit-i
while True: # alustab while tsükklit
        for event in pygame.event.get(): # registreerib kõik kasutaja sündmused
            if event.type == pygame.QUIT: # seab paika tingumuse et kui kasutaja sündmus on võrdeline pygamei sulgemisega, siis
                pygame.quit() # suleb pygame-i akna
                exit() # lõpetab tsükli