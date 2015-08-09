from tkinter import *
from tkinter.ttk import * 
from random import randrange
from time import time

master = Tk()
c = Canvas(master, width=1000, height=600)
c.pack()

i = randrange(0, 4)
j = randrange(0, 4)

distances = [64, 128, 256, 512]
widths = [4, 8, 16, 32]

CLICKED = False

counter = 1
idx = 0
current = [2, 4, 6, 8]

def log(distance, width, selection_number, time):
    file = open("log.txt", 'a')
    file.write("Sam " + str(distance) + " " + str(width) + " " + str(selection_number) + " " + str(round(time, 1)) + "\n")

def clicked(arg):
    global start
    total_time = (time() - start) * 1000
    print(total_time)
    global distances
    global widths
    global i
    global j
    global rect1
    global rect2
    global c
    global CLICKED

    global counter
    global idx
    global current

    log(distances[j], widths[i], counter, total_time)

    c.delete(ALL)

    # apply same distance and width in order of 2, 4, 6, 8 times, then restart
    if counter == current[idx]:
        counter = 0
        idx = (idx + 1) % 4
        # reseed widths and distances
        i = randrange(0, 4)
        j = randrange(0, 4)

    counter += 1

    if CLICKED:
        rect1 = c.create_rectangle(300, 0, 300+widths[i], 600, outline="blue", fill="blue")
        rect2 = c.create_rectangle(300+distances[j], 0, 300+distances[j]+widths[i], 600, outline="green", fill="green")
        start = time()
        CLICKED = False
        c.tag_bind(rect2, "<ButtonPress-1>", clicked)

    elif CLICKED == False:
        rect1 = c.create_rectangle(300, 0, 300+widths[i], 600, outline="green", fill="green")
        rect2 = c.create_rectangle(300+distances[j], 0, 300+distances[j]+widths[i], 600, outline="blue", fill="blue")
        start = time()
        CLICKED = True
        c.tag_bind(rect1, "<ButtonPress-1>", clicked)

rect1 = c.create_rectangle(300, 0, 300+widths[i], 600, outline="blue", fill="blue")
rect2 = c.create_rectangle(300+distances[j], 0, 300+distances[j]+widths[i], 600, outline="green", fill="green")


c.tag_bind(rect2, "<ButtonPress-1>", clicked)
# c.create_rectangle(left, top, right, bottom, fill="blue")

start = time()
master.mainloop()