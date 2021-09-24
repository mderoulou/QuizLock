#!/usr/bin/python3
import signal
import sys
import pygame
import os
from Xlib import display, X
import random
import time

CURRENT_DAY = 3

questions = { 3:
    [
        ["day03-0.png", "write"],
        ["day03-1.png", "main"],
    ],
    4 : [
        
    ]
}


def signal_handler(sig, frame):
    print("Answer the question, don't try to avoid it!")

signal.signal(signal.SIGABRT, signal_handler)
signal.signal(signal.SIGALRM, signal_handler)
signal.signal(signal.SIGCHLD, signal_handler)
signal.signal(signal.SIGCONT, signal_handler)
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTSTP, signal_handler)

keys = {pygame.K_a : "a",
        pygame.K_b : "b",
        pygame.K_c : "c",
        pygame.K_d : "d",
        pygame.K_e : "e",
        pygame.K_f : "f",
        pygame.K_g : "g",
        pygame.K_h : "h",
        pygame.K_i : "i",
        pygame.K_j : "j",
        pygame.K_k : "k",
        pygame.K_l : "l",
        pygame.K_m : "m",
        pygame.K_n : "n",
        pygame.K_o : "o",
        pygame.K_p : "p",
        pygame.K_q : "q",
        pygame.K_r : "r",
        pygame.K_s : "s",
        pygame.K_t : "t",
        pygame.K_u : "u",
        pygame.K_v : "v",
        pygame.K_w : "w",
        pygame.K_x : "x",
        pygame.K_y : "y",
        pygame.K_z : "z",
        pygame.K_SPACE : " ",
        pygame.K_BACKSPACE : "\r",
        pygame.K_0 : "0",
        pygame.K_1 : "1",
        pygame.K_2 : "2",
        pygame.K_3 : "3",
        pygame.K_4 : "4",
        pygame.K_5 : "5",
        pygame.K_6 : "6",
        pygame.K_7 : "7",
        pygame.K_8 : "8",
        pygame.K_9 : "9",
        pygame.K_KP0 : "0",
        pygame.K_KP1 : "1",
        pygame.K_KP2 : "2",
        pygame.K_KP3 : "3",
        pygame.K_KP4 : "4",
        pygame.K_KP5 : "5",
        pygame.K_KP6 : "6",
        pygame.K_KP7 : "7",
        pygame.K_KP8 : "8",
        pygame.K_KP9 : "9",
}


class Overlay:
    def __init__(self):
        time.sleep(1)
        self.question = questions[CURRENT_DAY][random.randint(0, len(questions[CURRENT_DAY])-1)]
        self.questionImg = pygame.image.load("questions/" + self.question[0])
        self.response = self.question[1]
        self.start = 0
        self.width, self.height = 1920, 1080
        dsp = display.Display()
        root = dsp.screen().root
        raw = root.get_image(0, 0, self.width, self.height, X.ZPixmap, 0xffffffff)
        self.backGround = pygame.image.fromstring(raw.data, (self.width, self.height), "RGBA")
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (0, 0)
        os.environ['SDL_VIDEO_CENTERED'] = '0'
        imgdata = pygame.surfarray.array3d(self.backGround)
        imgdata = imgdata[:,:,::-1]
        self.backGround = pygame.surfarray.make_surface(imgdata)

        pygame.init()
        curRez = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.SCALED + pygame.NOFRAME + pygame.FULLSCREEN, 32, vsync=1)

        self.text = ""
        self.running = True
        self.font = pygame.font.SysFont(None, 40)
        
    def checkAnswer(self):
        if (self.text.lstrip() == self.response):
            self.screen.fill((0, 0, 0, 0))
            self.screen.blit(self.backGround, (0, 0))
            fontText = self.font.render(self.text, True, (140, 124, 255))
            self.screen.blit(fontText, (self.width/2 - fontText.get_size()[0]/2, self.height*3/4-fontText.get_size()[1]/2))
            self.text = "Good Job"
            
            fontText = self.font.render(self.text, True, (255, 255, 255))   
            self.screen.blit(fontText, (self.width/2 - fontText.get_size()[0]/2, self.height*2.5/4-fontText.get_size()[1]/2))
            
            self.screen.blit(self.questionImg, (self.width/2 - self.questionImg.get_size()[0]/2, self.height/2 - self.questionImg.get_size()[1]/2))
            pygame.display.flip()
            time.sleep(1)
            sys.exit(0)
    
    def handleEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.start:
                    self.start = time.time()
            elif event.type == pygame.KEYDOWN:
                if event.key in keys.keys():
                    if not self.start:
                        self.start = time.time()
                        break
                    if keys[event.key] == '\r':
                        if len(self.text) == 0:
                            continue
                        self.text = self.text[:-1]
                        self.checkAnswer()
                    elif len(self.text) > 0 and keys[event.key] == '\n':
                        self.checkAnswer()
                    else:
                        self.text += keys[event.key]
                        self.checkAnswer()

    def run(self):
        while (self.running):
            #try:
            self.handleEvent()
            self.screen.fill((0, 0, 0, 0))
            self.screen.blit(self.backGround, (0, 0))
            
            if self.start:
                #draw Informations
                lockText = self.font.render("A epitech, il faut lock son PC !", True, (255, 0, 0))
                pos = (self.width/2 - lockText.get_size()[0]/2, self.height*1/4-lockText.get_size()[1]/2)
                pygame.draw.rect(self.screen, (0, 0, 0), (pos[0]-5, pos[1]-5, lockText.get_size()[0]+10, lockText.get_size()[1]+10))
                self.screen.blit(lockText, pos)

                #draw text input
                fontText = self.font.render(self.text, True, (255, 255, 255))
                pos = (self.width/2 - fontText.get_size()[0]/2, self.height*3/4-fontText.get_size()[1]/2)
                pygame.draw.rect(self.screen, (0, 0, 0), (pos[0]-5, pos[1]-5, fontText.get_size()[0]+10, fontText.get_size()[1]+10))
                self.screen.blit(fontText, pos)
                
                #draw Question
                pos = (self.width/2 - self.questionImg.get_size()[0]/2, self.height/2 - self.questionImg.get_size()[1]/2)
                pygame.draw.rect(self.screen, (255, 0, 0), (pos[0]-5, pos[1]-5, self.questionImg.get_size()[0]+10, self.questionImg.get_size()[1]+10))
                self.screen.blit(self.questionImg, pos)

            pygame.display.flip()
            pygame.time.Clock().tick(60)

            if self.start and time.time() - self.start >= 60*15:
                sys.exit(0)
            #except:
            #    pass
            

if __name__ == "__main__":
    Overlay().run()