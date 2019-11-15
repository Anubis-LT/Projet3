#! /usr/bin/env python3
# coding: utf-8

"""We import Pygame to create the game screen and the messages"""
import pygame as pg
import sys

sys.path.append("./")
from resources.filepy.constants     import *
from resources.filepy.level         import Level
from resources.filepy.characters    import Macgyver,Structure_map
from resources.filepy.display       import Display


class Game:
    """Class which coordonates all the classes to create a loop game with methods,\
    and initializes Pygame"""

    def __init__(self):

        # Choice level number of F1 to F5
        spath = Level()
        self.structure_map  = Structure_map(spath.pathfile)
        self.levelnumber    = spath.numberLevel

        """Pygame initialization, screen and messages creation, classes calling"""
        pg.init()
        pg.font.init()

        # Display
        sizeScreen          = int(SIZE_SPRITES * NB_SPRITES)
        self.screen         = pg.display.set_mode((sizeScreen, sizeScreen))
        self.title          = pg.display.set_caption(TITLE+"             LEVEL : "+str(self.levelnumber))
        self.icon           = pg.image.load(ICON).convert_alpha()
        pg.display.set_icon(self.icon)

        self.message        = pg.font.SysFont(None, 30)
        self.win            = self.message.render('YOU WIN ! You are out of the maze', True, (255, 255, 255))
        self.lost           = self.message.render('YOU LOST ! The guardian captured you', True, (255, 255, 255))

        self.display        = Display()
        self.macgyver       = Macgyver(self.structure_map)
        self.playing        = False
        self.clock          = pg.time.Clock()


    def start(self):
        """Method which runs the game, with the map display,
        the keyboard controls and the victory conditions"""
        self.playing = True
        while self.playing:
            self.display.display_map(self.structure_map, self.screen)
            self.keyboard_events()
            self.items_counter()
            self.endings()
            self.clock.tick(30)


    def endings(self):
        """Method called if MG is in front of the boss with or without all the items
        Printing a win or loss message and ending game"""
        if self.structure_map.map_array[self.macgyver.y][self.macgyver.x + 1] == 'G':

            if self.macgyver.items_collected == 3:
                self.rect = pg.draw.rect(self.screen, (18, 99, 18), [0, 300, 600, 50])
                self.screen.blit(self.win, (115, 315))
            else:
                self.rect = pg.draw.rect(self.screen, (155, 0, 0), [0, 300, 600, 50])
                self.screen.blit(self.lost, (110, 315))

            pg.display.update()
            pg.time.wait(1500)
            self.playing = False


    def keyboard_events(self):
        """Method for keyboard controllers during the game,
        implemented into the game.start() method"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.macgyver.move_up(self.structure_map)
                elif event.key == pg.K_DOWN:
                    self.macgyver.move_down(self.structure_map)
                elif event.key == pg.K_RIGHT:
                    self.macgyver.move_right(self.structure_map)
                elif event.key == pg.K_LEFT:
                    self.macgyver.move_left(self.structure_map)
                elif event.type == pg.K_ESCAPE:
                    self.playing = False

    def items_counter(self):
        """Method to display the items counter,
        by using the Macgyver class to count the items number"""
        self.counter_message = pg.font.SysFont(None, 25)
        self.counter = self.counter_message.render('Items : ' + str(self.macgyver.items_collected)+' / 3', True,\
        ((255,255,255)))
        self.screen.blit(self.counter, (500, 15))
        pg.display.update()