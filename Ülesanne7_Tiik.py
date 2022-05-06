import pygame, sys, random # moodulite pygame, sys ja random importimine faili

pygame.init() # pygame käivitamine

screenX = 640 # akna pikkus                                            
screenY = 480 # akna laius                                           
screen = pygame.display.set_mode([screenX, screenY]) # teeb akna muutujate screenX ja screenY antud väärtustega
pygame.display.set_caption("Ülesanne7 Tiik") # Paneb paika akna pealkirja
screen.fill([173, 216, 230]) # Värvib tausta helesiniseks

raadius = 10 # muutuja raadius omistab väärtuse 10 ehk 10px
värv0 = 0 # värvikoodi miinimum väärtus
värv1 = 255 # värvikoodi maksimum väärtus

while True: # alustab while tsükklit
    pos = pygame.mouse.get_pos() # muutuja pos omistab väärtuseks hiire asukoha
    # Mängu sulgemine ristist
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if events.type == pygame.MOUSEBUTTONDOWN: # kui klikitakse hiire nupul ja lastakse see lahti
            värv = (random.randint(värv0, värv1), random.randint(värv0, värv1), random.randint(värv0, värv1)) # Genereeritakse igakord suvaline värv
            pygame.draw.circle(screen, värv, pos, raadius, 1) # joonistatakse ekraanile ring, mis vahetab peale igat hiire klõpsu värvi
            raadius += 3 # Peale igat hiire klikki muutub ringi raadius 3 pikslit suuremaks
    pygame.display.update() # uuendatakse ekraani
pygame.quit() # suletakse mäng