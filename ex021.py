# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

from pygame import mixer # pip3 install pygame

mixer.init()
mixer.music.load('ex021.ogg')
mixer.music.play()
input()
