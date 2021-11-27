import sys
from pygame import mixer
import pygame
from pygame.locals import *
import numpy as np
from gl import Renderer, Model
import shaders


pygame.init()
global_start=False
gray = (119, 118, 110)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 200, 0)

techo = (78, 182, 162)
piso = (31, 33, 29)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)
blue = (0, 0, 255)
pause = False

display_width = 600
display_height = 600
gamedisplays = pygame.display.set_mode((display_width, display_height),pygame.NOFRAME)
pygame.display.set_caption('Proyecto 4')
clock = pygame.time.Clock()

intro_background = pygame.image.load('fondo2.png')
instruction_background = pygame.image.load('fondo2.png')

mixer.music.load('./sounds/intro.mp3')
mixer.music.set_volume(0.8)
mixer.music.play(-1)


       
def game_loop():
    
    
        
       

    width = 960
    height = 540

    deltaTime = 0.0

    pygame.init()
    screen = pygame.display.set_mode(
        (width, height), pygame.DOUBLEBUF | pygame.OPENGL|pygame.NOFRAME)
    
    clock = pygame.time.Clock()

    rend = Renderer(screen)
    rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

    face = Model('BugsBunny.obj', 'bunny.bmp')
    face.position.z = -3
    face.position.y=-0.5
    mixer.music.load('./sounds/bugsbunny.mp3')
    mixer.music.play(1)
        
    rend.scene.append(face)
    clicking=False
    
    


    isRunning = True
    while isRunning:
        
     
        keys = pygame.key.get_pressed()

        # Traslacion de camara
        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[K_d]:
            
            if rend.camPosition.x < 2:
                rend.camPosition.x += 1 * deltaTime
            
                
        if keys[K_a]:
            if rend.camPosition.x >-2:
                rend.camPosition.x -= 1 * deltaTime
            
        if keys[K_w]:
            if rend.camPosition.z<2:
                
                rend.camPosition.z += 1 * deltaTime
        if keys[K_s]:
            if rend.camPosition.z>-2:
                rend.camPosition.z -= 1 * deltaTime
        if keys[K_q]:
            if rend.camPosition.y>-2:
                rend.camPosition.y -= 1 * deltaTime
        if keys[K_e]:
            if rend.camPosition.y<2:
                rend.camPosition.y += 1 * deltaTime

        if keys[K_LEFT]:
            if rend.valor > 0:
                rend.valor -= 0.1 * deltaTime

        if keys[K_RIGHT]:
            if rend.valor < 0.2:
                rend.valor += 0.1 * deltaTime
        if keys[K_r]:
            rend.camPosition.x=0
            rend.camPosition.y=0
            rend.camPosition.z=0
            rend.camRotation.y=0
        
        for event in pygame.event.get():
            
           
            if event.type == MOUSEBUTTONDOWN:
                btn=pygame.mouse.get_pressed()
                clicking=False
                if event.button==1:
                    clicking=True
                    mx,my=pygame.mouse.get_pos()
                    
                    if clicking:
                        
                        
                        rend.camPosition.x=mx/960
                        rend.camPosition.y=my/540
                        
                if event.button ==4:
                    clicking=True
                    rend.camPosition.z -= 1 * deltaTime
                    
                if event.button ==5:
                    clicking=True
                    rend.camPosition.z += 1 * deltaTime    
                    
                if event.button ==3:
                    clicking=True
                    
                    rend.camRotation.y += 30 * deltaTime
        
        # Rotacion de camara
        if keys[K_z]:
            rend.camRotation.y += 15 * deltaTime
        if keys[K_x]:
            rend.camRotation.y -= 15 * deltaTime
        # Texturas
        if keys[K_1]:
          
            mixer.music.load('./sounds/bugsbunny.mp3')
            mixer.music.play(1)
            rend.scene.remove(face)
            rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

            face = Model('BugsBunny.obj', 'bunny.bmp')
            face.position.z = -3
            face.position.y=-0.5

            rend.scene.append(face)
        #Cazador
        if keys[K_2]:
            mixer.music.load('./sounds/cazador.mp3')
            mixer.music.play(1)
            rend.scene.remove(face)
            rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

            face = Model('cazador.obj', 'cazador.bmp')
            face.position.z = -3
            face.position.y=-0.5

            rend.scene.append(face)
        #Lucas
        if keys[K_3]:
            mixer.music.load('./sounds/lucas.mp3')
            mixer.music.play(1)
            rend.scene.remove(face)
            rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

            face = Model('lucas.obj', 'lucas.bmp')
            face.position.z = -3
            face.position.y=-0.5

            rend.scene.append(face)
        #Porki       
        if keys[K_4]:
            mixer.music.load('./sounds/porki.mp3')
            mixer.music.play(1)
            rend.scene.remove(face)
            rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

            face = Model('porki.obj', 'porki.bmp')
            face.position.z = -3
            face.position.y=-0.5

            rend.scene.append(face)
        if keys[K_5]:
            mixer.music.load('./sounds/claudio.mp3')
            mixer.music.play(1)
            rend.scene.remove(face)
            rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

            face = Model('claudio.obj', 'claudio.bmp')
            face.position.z = -3
            face.position.y=-0.5

            rend.scene.append(face)
        
        
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                isRunning = False

            elif ev.type == pygame.KEYDOWN:
                
                if ev.key == pygame.K_ESCAPE:
                    isRunning = False

                if ev.key == K_t:
                    rend.filledMode()
                if ev.key == K_y:
                    rend.wireframeMode()
               

        rend.tiempo += deltaTime
        deltaTime = clock.tick(60) / 1000

        rend.render()

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def text_objects(text, font, color):
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()


def introduction():
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background, (0, 0))
        button('', 25, 25, 550, 550, piso, piso, None)
        largetext = pygame.font.Font('freesansbold.ttf', 80)
        smalltext = pygame.font.Font('freesansbold.ttf', 20)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)

        TextSurf, TextRect = text_objects('CONTROLES', mediumtext, techo)
        TextRect.center = ((300), (50))
        gamedisplays.blit(TextSurf, TextRect)
        ptextSurf, ptextRect = text_objects('1-5 : CAMBIAR DE PERSONAJE', smalltext, techo)
        ptextRect.center = ((200), (100))

        stextSurf, stextRect = text_objects('W : ALEJARSE', smalltext, techo)
        stextRect.center = ((200), (150))
        htextSurf, hTextRect = text_objects('A : ACERCARSE', smalltext, techo)
        hTextRect.center = ((200), (200))
        atextSurf, atextRect = text_objects('S : ATRAS', smalltext, techo)
        atextRect.center = ((200), (250))
        rtextSurf, rTextRect = text_objects('D : DERECHA', smalltext, techo)
        rTextRect.center = ((200), (300))
        q_btn, q_btn_r = text_objects('Q : BAJAR CAMARA', smalltext, techo)
        q_btn_r.center = ((200), (350))
        gamedisplays.blit(q_btn, q_btn_r)
        e_btn, e_btn_r = text_objects('E : SUBIR CAMARA', smalltext, techo)
        e_btn_r.center = ((200), (400))
        gamedisplays.blit(e_btn, e_btn_r)
        girar_a, girar_b = text_objects('Z-X : GIRAR CAMARA', smalltext, techo)
        girar_b.center = ((200), (450))
        gamedisplays.blit(e_btn, e_btn_r)
        r_a, r_b = text_objects('R : REINICIAR CAMARA', smalltext, techo)
        r_b.center = ((200), (500))
        gamedisplays.blit(e_btn, e_btn_r)
        t_r, t_a = text_objects('MOUSE : MOVER CAMARA', smalltext, techo)
        t_a.center = ((200), (550))
        gamedisplays.blit(t_r, t_a)
        gamedisplays.blit(stextSurf, stextRect)
        gamedisplays.blit(htextSurf, hTextRect)
        gamedisplays.blit(atextSurf, atextRect)
        gamedisplays.blit(rtextSurf, rTextRect)
        gamedisplays.blit(ptextSurf, ptextRect)
        gamedisplays.blit(girar_a, girar_b)
        gamedisplays.blit(r_a, r_b)
        button("ATRAS", 450, 500, 100, 50, techo, piso, 'inicio')

        pygame.display.update()
        clock.tick(30)


def intro_loop():
    introduction = True

    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background, (0, 0))

        button("INICIO", 220, 175, 150, 50, techo, piso, 'play')
        button("SALIR", 220, 375, 150, 50, techo, piso, 'quit')
        button("CONTROLES", 220, 275, 150, 50, techo, piso, 'intro')


        pygame.display.update()
        clock.tick(30)


def paused():
    global pause
    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_background, (0, 0))
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)
        button('', 25, 25, 550, 550, piso, piso, None)
        title_pause, title_pause_r = text_objects("PAUSA", mediumtext, techo)
        title_pause_r.center = ((display_width//2), (display_height//2))
        gamedisplays.blit(title_pause, title_pause_r)
        button("CONTINUAR", 25, 400, 150, 50, techo, piso, 'resume')
        button("REINICIAR", 225, 400, 150, 50, techo, piso, 'play')
        button("MENU", 425, 400, 150, 50, techo, piso, 'inicio')
        pygame.display.update()
        clock.tick(30)


def resume():
    global pause
    pause = False

def button(msg, x, y, w, h, ic, ac, action=None):
    selected = mixer.Sound('click.wav')
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gamedisplays, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == 'play':
                selected.play()
                game_loop()
              

            if action == 'intro':
                selected.play()
                introduction()
            if action == 'inicio':
                selected.play()
                intro_loop()
                

                intro_loop()
            if action == 'pause':
                selected.play()
                paused()
            if action == 'resume':
                selected.play()
                resume()
            if action == 'quit':
                selected.play()
                pygame.quit()
                quit()
                sys.exit()

    else:
        pygame.draw.rect(gamedisplays, ic, (x, y, w, h))
    smalltext = pygame.font.Font('freesansbold.ttf', 20)
    textsurf, textrect = text_objects(msg, smalltext, black)
    textrect.center = ((x+(w/2)), (y+(h/2)))
    gamedisplays.blit(textsurf, textrect)


intro_loop()
