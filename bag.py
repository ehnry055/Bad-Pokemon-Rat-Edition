from tkinter import *

class PokeBag(Frame):
    def __init__ (self, master, end):
        super().__init__(master)

        self.end = end

        self.create_widgets()
        self.grid()
    
    def create_widgets(self):

        self.item1 = Button(self, text = "Potion", command = (self.potion))
        self.item1.grid(row = 0, column = 0, sticky = W)