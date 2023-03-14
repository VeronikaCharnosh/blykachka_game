'''game'''

class Room:
    '''
    '''
    def __init__(self,name):
        self.name = name
        self.description = ""
        self.linked_rooms = {}
        self.character = None
        self.item = None
        # self.defeated = 0
    def set_description(self, description):
        self.description = description

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item

    def link_room(self, room, direction):
        self.linked_rooms[direction] = room

    def get_details(self):
        print(f"You are in the {self.name}")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.name} is on the {direction}")

    def get_character(self):
        return self.character
    
    def get_item(self):
        return self.item
    
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("No move on this way")
            return self
    # def get_defeated(self):
    #     print(defeated)
    #     return defeated
# defeated = 0 
class Enemy:
    '''
    '''
    defeated = 0
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.weakness = None
        
        self.conversation = ''
    def set_conversation(self, conversation):
        self.conversation = conversation
    def set_weakness(self, weakness):
        self.weakness = weakness
    def describe(self):
        print(self.name + " is here!")
        print(self.description)
    def talk(self):
        if self.conversation:
            print(f'{self.name} says: {self.conversation}')
        else:
            print('Sience')
    def fight(self, weapon):
        if weapon == self.weakness:
            Enemy.defeated += 1
            return True
        return False
    def get_defeated(self):
        # print(self.defeated)
        return Enemy.defeated

class Item:
    '''
    '''
    def __init__(self,name):
        self.name = name
    def set_description(self, description):
        self.description = description
    def get_name(self):
        return self.name
    def describe(self):
        print("You see a " + self.name + ". " + self.description)
