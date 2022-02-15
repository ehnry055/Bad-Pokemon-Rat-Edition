class MovesRoster(object):
    def __init__ (self, file_name):
        '''
        This method intializes a new CharacterRoster object, setting up a property character_list 
        and filling it with new Character objects.
        The Character objects are defined in the file file_name; each line describes the properties of a single character.
        The file is in comma separated format.  Each line of the file includes:
            <Name>,<Hit Points>,<Strength>,<Dexterity>
        '''
        self.moves_dict = {}

        
        text_file = open(file_name)

        for line in text_file:
                move_damage = line.split(",")
                move = move_damage[0]
                damage = move_damage[1]
                damage = damage.strip()
                self.moves_dict[move] = damage