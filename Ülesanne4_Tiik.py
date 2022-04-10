import pygame, sys, random   #pygame, sys ja random importimine faili
pygame.init()  #pygame käivitamine


screenX = 640  #akna pikkus
screenY = 480  #akna laius
screen=pygame.display.set_mode([screenX,screenY]) #akna suuruse tegemine, antud juhul 640x480
pygame.display.set_caption("Ülesanne4") #kuvab ekraani nime
bg = pygame.image.load("bg_rally.jpg") # laadib lahti taustapildi
screen.blit(bg,[0,0]) # määrab ära pildi asukoha, antud juhul terve ekraan                                           
clock = pygame.time.Clock() #teeb mängu vähe realistlikumaks

punane = pygame.image.load("f1_red.png")  # laadib lahti punase auto pildi
punane = pygame.transform.scale(punane, [50, 100]) #muudab punase auto mõõtmeid, et auto sobituks ilusti ekraanile               
screen.blit(punane,[295,370]) #määrab ära punase auto asukoha

sinine = pygame.image.load("f1_blue.png") #laadib lahti sinise auto pildi
sinine = pygame.transform.scale(sinine, [50, 100])  # muudab sinise auto mõõtmeid, et auto mahuks ilusti ekraanile

skoor = 0 # Muutuja "skoor" algväärtus on 0.
font = pygame.font.Font(pygame.font.match_font('Daytona'), 30) # defineerib ära skoori kirja fonti ja suuruse
text = font.render("SKOOR: " + str(skoor), True, [255,255,255])  #muutuja text omistab väärtuse "font.render", ehk ekraanile kuvatakse skoor

# kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 3

coords = []  # koordinaatide loomine
for i in range(2): #alustab for tsükklit ja omistab 2 objekti
    posX = random.randint(140, 445)   #muutuja juhuslik koht x teljel
    posY = random.randint(1, screenY)  #muutuja juhuslik koht y teljel
    coords.append([posX, posY])  #poistsioonide omastamine

gameover = False  #muutuja "gameover" omistab väärtuse "False"
while not gameover:  # algab while tsükkel, juhul kui ei ole "gameover"
    # mängu ristist sulgemise jaoks:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
    # fps
    clock.tick(120) #määrab ära ekraaniliikumise kiiruse, ehk siis antud juhul 120 kaadrit sekundis
    
    for i in range(len(coords)): #i omistab koordinaadid vastavalt objektide arvule
        screen.blit(sinine, [coords[i][0], coords[i][1], 20, 20])  #sinist autot liigutatakse juhuslikult saadud koordinaatide abil
        coords[i][1] += 1 #muutuja väärtuseks enda väärtus +1

        if coords[i][1] > screenY:  # kui sinine auto jõuab alla, siis muudetakse auto alguspunkti
            skoor += 10 # Muutuja "skoor" väärtust inkrementeeritakse 10 võrra.
            coords[i][1] = random.randint(-20, -15) # valitakse suvaliselt uued väärtused Y teljel
            coords[i][0] = random.randint(140, 445) # valitakse juhuslikud väärtused X telje vahemikus, kuhu auto tekib

    screen.blit(text, [525, 20])  # Aknal kuvatakse muutujale "text" omistatud väärtus (koordinaatidel x=525 ja y=20).
    text = font.render("SKOOR: " + str(skoor), True, [255, 255, 255]) # arvutab kokku mitu skoori saadud on, ning kuvatakse see siis ekraanil
    pygame.display.flip() #ekraani värskendamine
    screen.blit(bg, [0, 0]) #joonistatakse taust uuesti üle
    screen.blit(punane, [295, 370]) #joonistatakse punane auto uuesti üle

pygame.quit()

