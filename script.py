#!/usr/bin/python3
import signal
import sys
import pygame
import os

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
        pygame.K_BACKSPACE : "\r",
        pygame.K_KP_ENTER : "\n"
}


class Overlay:
    def __init__(self):
        pygame.init()
        # self.screen = pygame.display.set_mode([1920, 1080], pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode([800, 600], pygame.NOFRAME)
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
                    elif len(self.text) > 0 and keys[event.key] == '\n':
                        self.checkAnswer()
                    else:
                        self.text += keys[event.key]

    def run(self):
        while (self.running):
            #try:
            self.handleEvent()
            self.screen.fill(TRANSPARENT)
            self.screen.blit(self.font.render(self.text, True, (140, 124, 255)), (20, 20))
            # pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)
            pygame.display.flip()
            pygame.time.Clock().tick(60)
            #except:
            #    pass
            

from Xlib import display, X

W,H = 200,200
dsp = display.Display()
root = dsp.screen().root
raw = root.get_image(0, 0, W,H, X.ZPixmap, 0xffffffff)

print(raw)

if __name__ == "__main__":
    Overlay().run()