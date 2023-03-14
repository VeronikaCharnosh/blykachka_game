'''game'''

class Station:
    '''
    '''
    def __init__(self,name):
        self.name = name
        self.description = ""
        self.linked_stations = {}
        self.character = None
        self.item = None
        # self.defeated = 0
    def set_description(self, description):
        self.description = description

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item

    def link_station(self, station, direction):
        self.linked_stations[direction] = station

    def get_details(self):
        print(f"Ти прибув на зупинку {self.name}")
        print(self.description)
        for direction in self.linked_stations:
            station = self.linked_stations[direction]
            print(f"{station.name} зупинка, яка знаходиться {direction} від тебе")

    def get_character(self):
        return self.character
    
    def get_item(self):
        return self.item
    
    def move(self, direction):
        if direction in self.linked_stations:
            return self.linked_stations[direction]
        else:
            print("Ти не можеш туди прибути")
            return self

class Character:
    '''
    '''
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = ''
    def get_name(self):
        return self.name
    def set_conversation(self, conversation):
        self.conversation = conversation
    def describe(self):
        print(self.name + " тут!")
        print(self.description)
    def talk(self):
        if self.conversation:
            print(f'{self.name} промовляє: {self.conversation}')
        else:
            print('Тишина...')



class Companion(Character):
    '''
    '''
    def __init__(self, name, description):
        super().__init__(name, description)
        self.conversation = ''
    

class Enemy(Character):
    '''
    '''
    defeated = 0
    def __init__(self, name, description):
        super().__init__(name, description)
        self.weakness = None
        self.conversation = ''
    def set_conversation(self, conversation):
        self.conversation = conversation
    def set_weakness(self, weakness):
        self.weakness = weakness
    # def describe(self):
    #     print(self.name + " тут!")
    #     print(self.description)
    # def talk(self):
    #     if self.conversation:
    #         print(f'{self.name} промовляє: {self.conversation}')
    #     else:
    #         print('Тишина...')
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
        print("Ти бачиш " + self.name + ". " + self.description)
