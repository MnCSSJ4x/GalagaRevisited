import os

import pygame
from pygame.locals import *
from pygame import mixer

pygame.init()

screen_width = 600
screen_height = 600

#background screen and icon
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Button Demo')

icon=pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)

background=pygame.image.load('Splash.png')

#background sound
mixer.music.load('Background.mp3')
mixer.music.play(-1)

font = pygame.font.SysFont('Calibri', 16)

# define colours
bg = (0, 0, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# define global variable
clicked = False
counter = 0

music_count=0
class button():
    # colours for button and text
    button_col = (0, 0, 160)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = white
    width = 200
    height = 50

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):

        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        # add shading to button
        pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # add text to button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action


again = button(75, 200, 'There was no walking away')
quit = button(325, 200, ' My luck had finally run out')

run = True
while run:

    screen.fill(bg)
    screen.blit(background,(0,0))

    if again.draw_button():
        mixer.music.pause()
        os.system('main.exe')
        music_count+=1
       

    if quit.draw_button():
        run = False
    if music_count:
        mixer.music.unpause()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
