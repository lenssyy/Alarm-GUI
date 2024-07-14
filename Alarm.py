from tkinter import *
import time
import pyglet

window = Tk()
window.title('Alarm')
window.geometry('500x500')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)


hour_lb = Label(
    frame,
    text='Часы:  '
)
hour_lb.grid(row=3, column=1)


minute_lb = Label(
    frame,
    text='Минуты: '
)
minute_lb.grid(row=4, column=1)


hour_en = Entry(
    frame,
)
hour_en.grid(row=3, column=2)


minute_en = Entry(
    frame
)
minute_en.grid(row=4, column=2)

def alarm():
    i = True
    while True:
        hour = str(hour_en.get())
        minute = str(minute_en.get())
        tim = str(time.strftime("%H:%M", time.localtime()))
        if tim == f'{hour}:{minute}' and i:
            sound = pyglet.media.load('Melody1.mp3')
            sound.play()
            i = False
        else:
            time.sleep(1)

kn = Button(
    frame,
    text='Завести будильник',
    command=alarm
)
kn.grid(row=5, column=2)


window.mainloop()