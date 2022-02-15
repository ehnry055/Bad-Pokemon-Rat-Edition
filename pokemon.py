import random

from setuptools import setup
from moves import MovesRoster
class Pokemon(object):
    
    def __init__ (self, name, HP, Atk, Def, Speed, standard_image, move1, move2, move3, move4):

        self.name = name
        self.HP = HP
        self.Atk = Atk
        self.Def = Def
        self.Speed = Speed
        self.Move1 = move1
        self.Move2 = move2
        self.Move3 = move3
        self.Move4 = move4
        setup = MovesRoster("pokemonmoves.txt")
        self.Move = setup.moves_dict

        self.standard_image = standard_image
        
    def attack(self, enemy):
        damage = ((22 * self.Move[1] * (self.Atk / self.Def)) / 50) + 2
        enemy.HP -= damage 
        return self.name + "uses" + self.Move[0] + "!"
        
    def get_death_message(self):
        ''' Returns (NOT print) a death message. It should include self's name '''
        return self.name + "fainted!"
                
    def __str__ (self):
        ''' Return (NOT print) a string that includes the name, hit points, strength, and dexterity of this object (self). '''
        return self.name + "; HP: " + str(self.HP) + "; ATK: " + str(self.Atk) + "; DEF: " + str(self.Def) + "; SPD: " + str(self.Speed)       
        
class PokemonRoster(object):
    def __init__ (self, file_name):
        '''
        This method intializes a new CharacterRoster object, setting up a property character_list 
        and filling it with new Character objects.
        The Character objects are defined in the file file_name; each line describes the properties of a single character.
        The file is in comma separated format.  Each line of the file includes:
            <Name>,<Hit Points>,<Strength>,<Dexterity>
        '''
        self.character_list = []

        
        text_file = open(file_name,"r")
        
        for line in text_file:
            line = line.strip()
            my_fields = line.split(",")
            character = Pokemon(my_fields[0], int(my_fields[1]), int(my_fields[2]), int(my_fields[3]), int(my_fields[4]), (my_fields[5]), (my_fields[6]), (my_fields[7]), (my_fields[8]), (my_fields[9]))
            self.character_list.append(character)
    
    def print_roster(self):
        '''
        Prints a numbered list of all Characters in the roster.
        Use str() on each Character object to utilize the __str__ method.
        NOTE: This method isn't used by GUIs.
        '''
        for i in range(len(self.character_list)):
            print(str(i) +": " + str(self.character_list[i]))        
    
    def get_and_remove_character (self, i):
        ''' 
        Gets and returns the "ith" Character from the list, then removes the 
        character from the list.  (Removal so prevents the user and computer from 
        using the same character).
        '''
        ch = self.character_list[i]
        self.character_list.remove(self.character_list[i])
        return ch
    
    def get_random_character (self):
        ''' Gets and returns a random character from the list (for the computer). '''
        return random.choice(self.character_list)
    
    def get_number_of_characters (self):
        ''' Returns the number of Characters in the roster. '''
        return len(self.character_list)

