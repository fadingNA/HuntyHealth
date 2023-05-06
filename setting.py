import pygame
import pygame
import os
import time
import random

pygame.font.init()
WIDTH, HEIGHT = 1280, 720
FPS = 60
clock = pygame.time.Clock()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HuntyHealth")

# Player ship
PLAYER_BAG = pygame.transform.scale(pygame.image.load(os.path.join('assest', "shoppingBag.png")), (150, 150))
# playerS
playerS_HAMBURGER = pygame.transform.scale(pygame.image.load(os.path.join("assest", "burger.png")), (50, 50))
playerS_CARROT = pygame.transform.scale(pygame.image.load(os.path.join("assest", "carrot.jpg")), (50, 50))
playerS_CABBAGE = pygame.transform.scale(pygame.image.load(os.path.join("assest", "cabage.jpg")), (50, 50))
playerS_salmon = pygame.transform.scale(pygame.image.load(os.path.join("assest", "salmon.png")), (50, 50))
playerS_TOMATOES = pygame.transform.scale(pygame.image.load(os.path.join("assest", "tomato.jpg")), (50, 50))
playerS_CORN = pygame.transform.scale(pygame.image.load(os.path.join("assest",'corn.png')), (50,50))
# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assest", 'bg.jpg')), (WIDTH, HEIGHT))
BG_start_game = pygame.transform.scale(pygame.image.load(os.path.join("assest", 'wallper_start.jpg')), (WIDTH,HEIGHT))

#Side bar
sidebar_img = pygame.transform.scale(pygame.image.load(os.path.join("assest","sidebar.png")),(81,637))

