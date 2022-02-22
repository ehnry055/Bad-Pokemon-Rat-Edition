import random
from tkinter import *
from pokemon import Pokemon

class PokemonBattle(Frame):
    def __init__ (self, master, player1, player2, Move, callback_on_exit):
        super().__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2
        self.Move = Move.moves_dict

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.HP
        self.player2_max_hp = player2.HP

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
        
        self.button = Button(self, text = self.player1.Move1, fg = "Red", command = (lambda : self.attack_clicked(self.Move[self.player1.Move1], self.player1.Move1)))
        self.button.grid(row = 5, column = 1, sticky = N)

        self.button = Button(self, text = self.player1.Move2, fg = "Red", command = (lambda : self.attack_clicked(self.Move[self.player1.Move2], self.player1.Move2)))

        self.button.grid(row = 5, column = 2, sticky = N)

        self.button = Button(self, text = self.player1.Move3, fg = "Red", command = (lambda : self.attack_clicked(self.Move[self.player1.Move3], self.player1.Move3)))
        self.button.grid(row = 6, column = 1, sticky = N)

        self.button = Button(self, text = self.player1.Move4, fg = "Red", command = (lambda : self.attack_clicked(self.Move[self.player1.Move4], self.player1.Move4)))
        self.button.grid(row = 6, column = 2, sticky = N)

        Label(self, text = self.player1.name).grid(row = 0, column = 1, sticky = N)
        Label(self, text = self.player2.name).grid(row = 0, column = 2, sticky = N)

        for i in range(1, 3):
            if i == 1:
                p = self.player1
            else:
                p = self.player2

            add = 0
            character = PhotoImage(file="imagination/" + str(p.standard_image))
            image = Label(self, image = character, )
            image.photo = character

            image.grid(row = 1, column = i, padx= (50, 50), sticky = W)


        self.totalhp1 = self.player1.HP
        self.totalhp2 = self.player2.HP

        self.hp1 = Label(self, text = f"{self.player1.HP}/{self.totalhp1} HP")

        self.hp1.grid(row = 3, column = 1, sticky = N)

        self.hp2 = Label(self, text = f"{self.player2.HP}/{self.totalhp2} HP")
        self.hp2.grid(row = 3, column = 2, sticky = N)


        self.desc1 = Label(self, text= "")
        self.desc1.grid(row= 8, column = 1, sticky = N)
        
        self.desc2 = Label(self, text= "")
        self.desc2.grid(row= 9, column = 1, sticky = N)

        self.winner = Label(self, text= "", fg = "Blue")
        self.winner.grid(row= 10, column = 1, sticky = N)
   
    def attack_clicked(self, moves, movename):
        self.desc1["text"] = f"{self.player1.attack(self.player2, moves, movename)}"
        self.hp1["text"] = f"{self.player1.HP:.1f}/{self.totalhp1} HP"


        moves_name_list = [self.player2.Move1, self.player2.Move2, self.player2.Move3, self.player2.Move4]
        number = random.randint(0, 4)
        self.desc2["text"] = f"{self.player2.attack(self.player1, self.Move[moves_name_list[number]], moves_name_list[number])}"
        self.hp2["text"] = f"{self.player2.HP:.1f}/{self.totalhp2} HP"

        if self.player1.HP <= 0 or self.player2.HP <= 0:
            if self.player1.HP <= 0:
                self.player1.HP = 0
                self.winner["text"] = f"{self.player1.name} fainted!"
            if self.player2.HP <= 0:
                self.player2.HP = 0
                self.winner["text"] = f"{self.player2.name} fainted!"
        
            
            Button(self, text = "Exit!", fg = "Red", command = self.exit_clicked).grid(row = 9, column = 2, sticky = E)

    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()