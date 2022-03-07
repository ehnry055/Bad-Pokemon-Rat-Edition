from tkinter import *


class PokemonSelect(Frame):
    def __init__ (self, master, roster, callback_on_selected):
        super().__init__(master)
       
        self.roster = roster
        
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets()
        
    def create_widgets (self):

        self.character_index = StringVar()
        self.character_index.set(None)

        Label(self, text = "HP\tATK\tDEF\tSPD").grid(row = 0, column = 2, sticky = W)
        Label(self,text = "HP\tATK\tDEF\tSPD").grid(row = 0, column = 6, sticky= E)

        for i in range(self.roster.get_number_of_characters()-4):
            Radiobutton(self, text = self.roster.character_list[i].name, variable = self.character_index, value = i).grid(row = 2 + i, column = 0, sticky = W)
            imageSmall = PhotoImage(file="imagination/" + self.roster.character_list[i].standard_image)
            w = Label(self, image = imageSmall, )
            w.photo = imageSmall
            w.grid(row = 2 + i, column = 1, sticky = W)

            Label(self, text = f"{self.roster.character_list[i].HP}\t{self.roster.character_list[i].Atk}\t{self.roster.character_list[i].Def}\t{self.roster.character_list[i].Speed}").grid(row = 2+i, column = 2, sticky = W)

        for i in range(4, 8): #hardcoded so adjust when longer character list. 
            Radiobutton(self, text = self.roster.character_list[i].name, variable = self.character_index, value = i).grid(row = 2 + i - 4, column = 4, sticky = E)
            imageSmall = PhotoImage(file="imagination/" + self.roster.character_list[i].standard_image)
            w = Label(self, image = imageSmall, )
            w.photo = imageSmall
            w.grid(row = 2 + i - 4, column = 5, sticky = E)

            Label(self, text = f"{self.roster.character_list[i].HP}\t{self.roster.character_list[i].Atk}\t{self.roster.character_list[i].Def}\t{self.roster.character_list[i].Speed}").grid(row = 2+i-4, column = 6, sticky = E)

        Button(self, text = "Pokemon Selected!", fg = "Red", command = self.selected_clicked).grid(row = 8, column = 8, sticky = E)

    def selected_clicked(self):
        
        self.callback_on_selected(self.character_index.get())
