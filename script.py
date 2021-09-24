#!/usr/bin/python3
import signal
import sys
import pygame
import os
from Xlib import display, X

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
}


class Overlay:
    def __init__(self):
        W,H = 1920,1080
        dsp = display.Display()
        root = dsp.screen().root
        raw = root.get_image(0, 0, W,H, X.ZPixmap, 0xffffffff)
        self.backGround = pygame.image.fromstring(raw.data, (W, H), "RGBA")
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (-100, -100)
        os.environ['SDL_VIDEO_CENTERED'] = '0'
        pygame.image.save(self.backGround, "img.jpg")
        self.backGround = pygame.image.load("img.jpg")


        pygame.init()
        curRez = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.screen = pygame.display.set_mode((W, H), pygame.SCALED + pygame.NOFRAME + pygame.FULLSCREEN, 32, vsync=1)
        #pygame.display.toggle_fullscreen()
        pygame.display.flip()

        self.text = ""
        self.response = "toto"
        #self.screen = pygame.display.set_mode([800,600])
        self.running = True
        self.font = pygame.font.SysFont(None, 24)
        
    def checkAnswer(self):
        if (self.text == self.response):
            sys.exit(0)
    
    def handleEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
            if event.type == pygame.KEYDOWN:
                if event.key in keys.keys():
                    if len(self.text) > 0 and keys[event.key] == '\r':
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
            self.screen.blit(self.font.render(self.text, True, (140, 124, 255)), (20, 20))
            #pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)
            pygame.display.flip()
            pygame.time.Clock().tick(60)
            #except:
            #    pass
            

if __name__ == "__main__":
    Overlay().run()