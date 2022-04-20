import pygame # pygame importimine faili
pygame.init() # pygame käivitamine

screenX = 640 # Akna pikkus.
screenY = 480 # Akna laius.
screen=pygame.display.set_mode([screenX,screenY]) # Teeb akna suurusega 640x480.
pygame.display.set_caption("Ülesanne 6 - Tiik") # Seab paika akna pealkirja, antud juhul "Ülesanne 5 - Tiik"
clock = pygame.time.Clock() # Lisatakse mängu realistlik ajalahendus

# ball-i kiirus ning asukoht.
posX, posY = 0, 0 
speedX, speedY = 3, 4

#Taustamuusika
pygame.mixer.music.load('01 - Super Mario Bros.mp3') #laadib lahti taustamuusika
pygame.mixer.music.play(-1) # jääb heli lõpmatult kordama.

ball = pygame.Rect(posX, posY, 20, 20) # luuakse rect objekt, mille asukohaks on posX, ja posY ning pilt salvestatakse suurusega 20x20.
ball1 = pygame.image.load("ball.webp") # laadib lahti ball-i pildi.
ball1 = pygame.transform.scale(ball1, [ball.width, ball.height]) # ball-i pildi suurust kohandatakse, ning uueks väärtuseks saadakse 20x20.

# pad-i kiirus ning asukoht
posX1, posY1 = 0, (screenY/1.5) # Muutuja posX2 ja posY2 väärtused on 0.
speedX1 = 0 # Muutuja speedX2 väärtus on 2.

pad = pygame.Rect(posX1, posY1, 120, 20) # luuakse rect objekt, mille asukohaks on posX1, ja posY1 ning pilt salvestatakse suurusega 120x20.
pad1 = pygame.image.load("pad.webp") # laadib lahti pad-i pildi
pad1 = pygame.transform.scale(pad1, [pad.width, pad.height]) # pad-i pildi suurust kohandatakse, ning uueks väärtuseks saadakse 120x20.

skoor = 0 # muutuja skoor omistab väärtuse 0

font = pygame.font.Font(pygame.font.match_font('Daytona'), 30) # defineerib ära muutuja skoori kirja fonti ja suuruse
text = font.render("SKOOR: " + str(skoor), True, [255,255,255]) #muutuja text omistab väärtuse "font.render", ehk ekraanile kuvatakse skoor, ning tektsi värv on valge

gameover = False # muutuja running omistab väärtuse True ehk tõene.
while (gameover == False): # alustab while tsüklit, kuniks running väärtus on tõene ehk True.
    clock.tick(60)  # määrab ära ekraaniliikumise kiiruse, ehk siis antud juhul 60 kaadrit sekundis
    screen.fill([173, 216, 230])  # värvib ära tausta, ning antud rgb koodiga tuleb taustavärviks helesinine.
    # mängu sulgemine ristist.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        
        #mängu juhtimine noolte abil
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT: 
                speedX1 = 5 
            elif event.key == pygame.K_LEFT:
                speedX1 = -5 
        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT: 
                speedX1 = 0 
        
    
    screen.blit(text, [520, 20])  # taustal kuvatakse mängu skoori, koordinaatidel 540x20
    text = font.render("SKOOR: " + str(skoor), True, [255, 255, 255])  #muutuja text omistab väärtuse "font.render", ehk ekraanile kuvatakse skoor, ning tektsi värv on valge.

    
    ball = pygame.Rect(posX, posY, 20, 20) # Tsüklis luuakse rect objekt, mille asukohaks on posX, ja posY ning pilt salvestatakse suurusega 20x20..
    screen.blit(ball1, ball) # ekraanil kuvatakse palli pilt mille parameetriks on muutuja ball1

    # Palli kiirus ning asukoht.
    posX += speedX # muutuja posX väärtust suurendatakse muutuja speedX väärtuse võrra.
    posY += speedY # muutuja posY väärtust suurendatakse muutuja speedY väärtuse võrra.

    # Palli kokkupõrke tuvastamine ning suuna muutmine
    if posX > screenX - ball1.get_rect().width or posX < 0: #kui posX on suurem screenX ja ball1.get_rect().width vahest, või posX on väiksem kui 0
        speedX = -speedX # muudetakse muutuja speedX väärtus negatiivseks, ehk asi hakkab toimuma teistpidi

    if posY < 0: #kui posY on väiksem kui 0
        speedY = -speedY # muudetakse muutuja speedY väärtus negatiivseks, ehk asi hakkab toimuma teistpidi
    if posY > screenY: #kui posY on suurem kui screenY, saab mäng läbi.
        text2 = font.render("Game Over!", True, [255, 255, 255]) # muutuja text2 omistab väärtuse "font.render" ehk ekraanile kuvatakse sõne "Game Over!"
        screen.blit(text2, [250, 250]) # kuvab ekraanile text2 väärtuse, ning asukohaks on 250x250.
        
    pad = pygame.Rect(posX1, posY1, 120, 20) # Tsüklis luuakse rect objekt, mille asukohaks on posX1, ja posY1 ning pilt salvestatakse suurusega 120x20.
    screen.blit(pad1, pad) # ekraanil kuvatakse pad-i pilt mille parameetriks on muutuja pad1

    posX1 += speedX1 # muutuja posX1 väärtust suurendatakse muutuja speedX1 väärtuse võrra.

    # aluse kokkupõrke tuvastamine ning suuna muutmine.
    if posX1 > screenX - pad1.get_rect().width or posX1 < 0: #kui posX2 on suurem screenX ja pad1.get_rect().width vahest, või posX1 on väiksem kui 0
        speedX1 = 0 # # muudetakse muutuja speedX1 väärtus nulliks

    # aluse ja palli vaheline kokkupõrge, suuna muutmine, ja skoori suurenemine 1 võrra.
    if ball.colliderect(pad) and speedY > 0: # kui balli ja pad-i vahel toimub kokkupõrge, ning speedY väärtus on suurem kui 0
        skoor += 1 # suureneb muutuja skoor väärtus 1 võrra.
        speedY = -speedY # muudetakse muutuja speedY väärtus negatiivseks, ehk asi hakkab toimuma teistpidi

    pygame.display.flip() # Akent värskendatakse.
pygame.quit()