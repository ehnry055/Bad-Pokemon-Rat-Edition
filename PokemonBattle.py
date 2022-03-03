import time
import random
from bag import PokeBag
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
        self.totalhp1 = player1.HP
        self.totalhp2 = player2.HP

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets(self):
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
        
        self.starting_menu()

        Label(self, text = self.player1.name+"\t lvl 50").grid(row = 0, column = 1, sticky = N)
        Label(self, text = self.player2.name+"\t lvl 50").grid(row = 0, column = 2, sticky = N)

        for i in range(1, 3):
            if i == 1:
                p = self.player1
            else:
                p = self.player2

            character = PhotoImage(file="imagination/" + str(p.standard_image))
            image = Label(self, image = character, )
            image.photo = character

            image.grid(row = 1, column = i, padx= (75, 75), sticky = W)

        self.hp1 = Label(self, text = f"{self.player1.HP}/{self.totalhp1} HP")
        self.hp1.grid(row = 3, column = 1, sticky = N)

        self.hp2 = Label(self, text = f"{self.player2.HP}/{self.totalhp2} HP")
        self.hp2.grid(row = 3, column = 2, sticky = N)


        self.desc1 = Label(self, text= "")
        self.desc1.grid(row= 8, column = 1, sticky = W)
        
        self.desc2 = Label(self, text= "")
        self.desc2.grid(row= 9, column = 1, sticky = W)

        self.winner = Label(self, text= "", fg = "Blue")
        self.winner.grid(row= 10, column = 1, sticky = W)

    def starting_menu(self):
        self.option1 = Button(self, text = "Attack", command = (self.menu_attack))
        self.option1.grid(row = 5, column = 1, sticky = N)

        self.option2 = Button(self, text = "Bag", command = (self.menu_bag))
        self.option2.grid(row = 5, column = 2, sticky = N)

        self.option3 = Button(self, text = "Pokemon", command = (self.menu_select))
        self.option3.grid(row = 6, column = 1, sticky = N)

        self.option4 = Button(self, text = "Run", command = (self.menu_run))
        self.option4.grid(row = 6, column = 2, sticky = N)

    def menu_attack(self):
        self.option1.destroy()
        self.option2.destroy()
        self.option3.destroy()
        self.option4.destroy()

        self.move1 = Button(self, text = self.player1.Move1, fg = "Red", command = (lambda : self.attack_clicked(self.Move[self.player1.Move1], self.player1.Move1)))
        self.move1.grid(row = 5, column = 1, sticky = N)

        self.move2 = Button(self, text = self.player1.Move2, fg = "Red", command = (lambda : self.attack_clicked(self.Move[self.player1.Move2], self.player1.Move2)))
        self.move2.grid(row = 5, column = 2, sticky = N)

        self.move3 = Button(self, text = self.player1.Move3, fg = "Red", command = (lambda : self.attack_clicked(self.Move[self.player1.Move3], self.player1.Move3)))
        self.move3.grid(row = 6, column = 1, sticky = N)

        self.move4 = Button(self, text = self.player1.Move4, fg = "Red", command = (lambda : self.attack_clicked(self.Move[self.player1.Move4], self.player1.Move4)))
        self.move4.grid(row = 6, column = 2, sticky = N)

        self.back_button = Button(self, text = "Back", fg = "Red", command = (self.back))
        self.back_button.grid(row = 9, column = 2, sticky = E)

    def back(self):
        self.move1.destroy()
        self.move2.destroy()
        self.move3.destroy()
        self.move4.destroy()
        self.back_button.destroy()

        self.starting_menu()

    def menu_bag(self):

        #self.root.title("Bag")
        #self.current_screen = PokeBag(master = self.root, end = self.end)
        pass

    def menu_select(self):
        pass

    def menu_run(self):
        self.option1.destroy()
        self.option2.destroy()
        self.option3.destroy()
        self.option4.destroy()

        self.winner["text"] = "There's no running away in a trainer battle!"

        self.ok = Button(self, text = "Back", fg = "Red", command = (self.other_ok))
        self.ok.grid(row = 9, column = 2, sticky = E)

    def other_ok(self):
        self.winner["text"] = ""
        self.ok.destroy()
        self.starting_menu()

   
    def attack_clicked(self, moves, movename):

        def player1_attack(self, moves, movename):
            self.desc1["text"] = f"{self.player1.attack(self.player2, moves, movename)}"

            if self.player2.HP <= 0:
                self.player2.HP = 0
                self.desc2["text"] = ""
                self.hp2["text"] = f"{self.player2.HP}/{self.totalhp2} HP"

                self.winner["text"] = f"{self.player2.name} fainted!"

                Button(self, text = "Exit!", fg = "Red", command = self.exit_clicked).grid(row = 9, column = 2, sticky = N)
            else:
                self.hp2["text"] = f"{self.player2.HP}/{self.totalhp2} HP"

        def player2_attack(self):
            moves_name_list = [self.player2.Move1, self.player2.Move2, self.player2.Move3, self.player2.Move4]
            number = random.randint(0, 3)
            self.desc2["text"] = f"{self.player2.attack(self.player1, self.Move[moves_name_list[number]], moves_name_list[number])}"

            if self.player1.HP <= 0:
                self.player1.HP = 0
                self.desc1["text"] = ""
                self.hp1["text"] = f"{self.player1.HP}/{self.totalhp1} HP"
                self.winner["text"] = f"{self.player1.name} fainted!"
            
                Button(self, text = "Exit", fg = "Red", command = self.exit_clicked).grid(row = 9, column = 2, sticky = E)

            self.hp1["text"] = f"{self.player1.HP}/{self.totalhp1} HP"
        
        if self.player1.Speed >= self.player2.Speed:
            a = player1_attack(self, moves, movename)
            b = player2_attack(self)
        else:
            a = player2_attack(self)
            b = player1_attack(self, moves, movename)


    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()