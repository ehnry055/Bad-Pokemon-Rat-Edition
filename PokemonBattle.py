from tkinter import *

class PokemonBattle(Frame):
    def __init__ (self, master, player1, player2, Move, callback_on_exit):
        super().__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2
        self.Move = Move

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
        
        self.button = Button(self, text = "Scratch", fg = "Red", command = self.attack_clicked)
        self.button.grid(row = 0, column = 1, sticky = N)

        self.button = Button(self, text = "Tackle", fg = "Red", command = self.attack_clicked)
        self.button.grid(row = 0, column = 2, sticky = N)

        self.button = Button(self, text = "Pound", fg = "Red", command = self.attack_clicked)
        self.button.grid(row = 1, column = 1, sticky = N)

        self.button = Button(self, text = "Flamethrower", fg = "Red", command = self.attack_clicked)
        self.button.grid(row = 1, column = 2, sticky = N)

        Label(self, text = "You").grid(row = 3, column = 1, sticky = N)
        Label(self, text = "Computer").grid(row = 3, column = 2, sticky = N)

        for i in range(1, 3):
            if i == 1:
                p = self.player1
            else:
                p = self.player2

            character = PhotoImage(file="images/" + str(p.large_image))
            image = Label(self, image = character, )
            image.photo = character
            image.grid(row = 4, column = i, sticky = W)

        self.totalhp1 = self.player1.HP
        self.totalhp2 = self.player2.HP

        self.hp1 = Label(self, text = f"{self.player1.HP}/{self.totalhp1} HP")
        self.hp1.grid(row = 5, column = 1, sticky = N)

        self.hp2 = Label(self, text = f"{self.player2.HP}/{self.totalhp2} HP")
        self.hp2.grid(row = 5, column = 2, sticky = N)

        self.desc1 = Label(self, text= "")
        self.desc1.grid(row= 0, column = 2, sticky = N)
        
        self.desc2 = Label(self, text= "")
        self.desc2.grid(row= 1, column = 2, sticky = N)

        self.winner = Label(self, text= "", fg = "Blue")
        self.winner.grid(row= 2, column = 2, sticky = N)
            
        
    def attack_clicked(self):
         
        self.desc1["text"] = f"{self.player1.attack(self.player2, self.Move)}"
        self.desc2["text"] = f"{self.player2.attack(self.player1, self.Move)}"

        self.hp1["text"] = f"{self.player1.HP}/{self.totalhp1} HP"
        self.hp2["text"] = f"{self.player2.HP}/{self.totalhp2} HP"

        if self.player1.HP <= 0 or self.player2.hit_points <= 0:
            if self.player1.HP <= 0:
                self.winner["text"] = f"{self.player2.name} is victorious!"
            if self.player2.HP <= 0:
                self.winner["text"] = f"{self.player1.name} is victorious!"
        
            self.button.destroy()
            Button(self, text = "Exit!", fg = "Red", command = self.exit_clicked).grid(row = 0, column = 1, sticky = N)



    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()