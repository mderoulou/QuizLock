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

print('Press Ctrl+C')

"""class Overlay: # ce truc marchera pas sur linux
    def __init__(self, WindowTitle):
        self.figuresToDraw = []
        print("init overlay...", end="", flush=True)
        #Get Target Window And Rect
        self.targetHwnd = win32gui.FindWindow(None, WindowTitle)
        if not self.targetHwnd:
            sys.exit(f"Window Not Found: {WindowTitle}")
        self.targetRect = self.GetTargetWindowRect()
        print("done")

        #Init Pygame
        print("init pygame...", end="", flush=True)
        os.environ['SDL_VIDEO_WINDOW_POS'] = str(self.targetRect.x) + "," + str(self.targetRect.y)
        #pygame.init()
        print("here")
        self.screen = pygame.display.set_mode((self.targetRect.w, self.targetRect.h), pygame.NOFRAME)
        self.hWnd = pygame.display.get_wm_info()['window']
        win32gui.SetWindowLong(self.hWnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(self.hWnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(self.hWnd, win32api.RGB(*TRANSPARENT), 0, win32con.LWA_COLORKEY)
        win32gui.BringWindowToTop(self.hWnd)
        win32gui.SetWindowPos(self.hWnd, TOPMOST, 0, 0, 0, 0, NOMOVE | NOSIZE)
        self.window = True
        print("done")


    def GetTargetWindowRect(self):
        rect = win32gui.GetWindowRect(self.targetHwnd)
        ret = Vector(rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1])
        return ret

    def handle(self):
        win32gui.SetWindowPos(self.hWnd, TOPMOST, self.targetRect.x, self.targetRect.y, 0, 0, NOMOVE | NOSIZE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.window = False
        if self.targetRect != self.GetTargetWindowRect():
            self.targetRect = self.GetTargetWindowRect()
            win32gui.SetWindowPos(self.hWnd, TOPMOST, 0, 0, 0, 0, NOMOVE | NOSIZE)
            win32gui.MoveWindow(self.hWnd, self.targetRect.x, self.targetRect.y, self.targetRect.w, self.targetRect.h, True)

        pygame.display.update()
        pygame.time.Clock().tick(60)
        self.screen.fill(TRANSPARENT)"""
# Mais y'aura moy d'en faire un equivalente ?
# aucune idée
# sinnon on doit pouvoir faire un truc qui se met en full screen et force le focus

class Overlay:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([1920, 1080], pygame.FULLSCREEN)
        self.running = True
    
    def handleEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass

    def run(self):
        while (self.running):
            try:
                self.handleEvent()
                pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)
                pygame.display.flip()
            except:
                pass
            

if __name__ == "__main__":
    Overlay().run()