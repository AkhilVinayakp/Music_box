import pygame
import os
import tkinter as tkr
from tkinter.filedialog import askdirectory

# creating the window
box = tkr.Tk()
box.title('MUSIC BOX')
# setting the size using geometry
box.geometry("450x350")
# modules
# directory
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

# playlist
playlist = tkr.Listbox(box, font="Cambria 14 bold", selectmode=tkr.SINGLE)
for item in song_list:
    position = 0
    playlist.insert(position, item)
    position += 1

# initialize pygame
pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def resume():
    pygame.mixer.music.unpause()


b_play = tkr.Button(box, height=3, width=3, text="play", command=play())


box.mainloop()
