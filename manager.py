from tkinter import *

from PokemonBattle import PokemonBattle
from PokemonSelect import PokemonSelect
from pokemon import PokemonRoster
from moves import MovesRoster

class BattleManager(object):
    
    def __init__ (self):
        self.root = Tk()
        self.current_screen = None
        self.pokemon_roster = None
        self.player = None
        self.computer = None
    
    def setup_character_selection (self):
        
        self.root.title ("Choose Your Pokemon!")
        
        self.character_roster = PokemonRoster("digimon.txt")
        self.movesdict = MovesRoster("pokemonmoves.txt")
        

        # Changes the window's title
        self.root.title ("Select your character!")
        # Reads battle_characters.txt to create a CharacterRoster.
        self.character_roster = PokemonRoster("digimon.txt")
        # Creates and displays a Character Selection screen
        self.current_screen = PokemonSelect(master = self.root, roster = self.character_roster, callback_on_selected = self.onclose_character_selection)
           
    def onclose_character_selection (self, selected_char_index):
              
        selected_char_index = int (selected_char_index)
        
        # Gets the player's chosen Character
        self.player = self.character_roster.get_and_remove_character(selected_char_index)
        
        # Gets a different random Character for the computer.
        self.computer = self.character_roster.get_random_character()
        
        # Destroys the Character Selection window
        self.current_screen.destroy()

        # Continue on - set up the Battle screen!
        self.setup_battle()


    def setup_battle(self):

        # Changes the window's title
        self.root.title ("Battle!")

        # Creates and displays a Battle screen
        self.current_screen = PokemonBattle(master= self.root, player1 = self.player, player2 = self.computer, Move = self.movesdict, callback_on_exit = self.onclose_battle)

    def onclose_battle (self):

        # Destroy the entire program's window, which includes the Battle screen.
        self.root.destroy()
        
def main():
    # Create the battle manager, which creates the tkinter window.
    battle = BattleManager()
    # The program begins with the Character Selection screen!
    battle.setup_character_selection()
    # Run the program!
    battle.root.mainloop()
 
main()