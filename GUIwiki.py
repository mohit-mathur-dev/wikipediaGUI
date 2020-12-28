# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 08:30:49 2020

@author: Mohit Mathur
"""

from tkinter import *
from tkinter import Scrollbar
import wikipedia

top = Tk()
top.geometry('300x300')
top.title('SUMMERY WIKIPEDIA')
top.configure(background='GREY')

frame = Frame(top,bg='#A9A9A9')

def show():
    entry = E.get()
    answer.delete(1.0,END)
    try:   #TRY use for remove the error
        answer_value = wikipedia.summary(entry)
        answer.insert(INSERT,answer_value)
    except:
        answer.insert(INSERT,'please enter correct keyword or check your internet connection')
        answer.insert(INSERT,answer_value)
        
l = Label(frame, text='WIKI LITE', relief=GROOVE, font=('arial',15))
l.pack()

E = Entry(frame, width=25, font=('arial',15),bd=6)
E.pack()

b = Button(frame,text = 'search',bd=5,bg='BLACK',width=20,fg = 'WHITE',command=show)
b.pack()

frame.pack()

bottomframe = Frame(top)

scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT,fill =Y)


answer = Text(bottomframe,width = 30,bd=6,height=10,wrap = WORD,yscrollcommand = scroll.set)
answer.pack()

scroll.config(command=answer.yview)
bottomframe.pack()

top.mainloop()