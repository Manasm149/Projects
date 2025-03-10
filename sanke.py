import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class Cube:
    rows = 20
    w = 500
    
    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i, j = self.pos
        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class Snake:
    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body = [self.head]
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.dirnx, self.dirny = -1, 0
            elif keys[pygame.K_RIGHT]:
                self.dirnx, self.dirny = 1, 0
            elif keys[pygame.K_UP]:
                self.dirnx, self.dirny = 0, -1
            elif keys[pygame.K_DOWN]:
                self.dirnx, self.dirny = 0, 1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows - 1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1: c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows - 1)
                else: c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.head = Cube(pos)
        self.body = [self.head]
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
        new_pos = (tail.pos[0] - dx, tail.pos[1] - dy)
        new_cube = Cube(new_pos, dx, dy)
        self.body.append(new_cube)

    def draw(self, surface):
        for i, c in enumerate(self.body):
            c.draw(surface, eyes=(i == 0))


def draw_grid(w, rows, surface):
    size_between = w // rows
    for i in range(rows):
        x = size_between * i
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, x), (w, x))


def redraw_window(surface):
    global rows, width, s, snack
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows, item):
    positions = {cube.pos for cube in item.body}
    while True:
        x, y = random.randrange(rows), random.randrange(rows)
        if (x, y) not in positions:
            return x, y


def message_box(subject, content):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(subject, content)
    root.destroy()


def main():
    global width, rows, s, snack
    width, rows = 500, 20
    win = pygame.display.set_mode((width, width))
    s = Snake((255, 0, 0), (10, 10))
    snack = Cube(random_snack(rows, s), color=(0, 255, 0))
    clock = pygame.time.Clock()
    
    while True:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        if s.body[0].pos == snack.pos:
            s.add_cube()
            snack = Cube(random_snack(rows, s), color=(0, 255, 0))
        
        if any(cube.pos in [c.pos for c in s.body[i+1:]] for i, cube in enumerate(s.body)):
            print('Score:', len(s.body))
            message_box('You Lost!', 'Play again...')
            s.reset((10, 10))
        
        redraw_window(win)


main()
