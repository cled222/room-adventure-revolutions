#added this new file in order to split up the actual game file with the room and item properties
class Room:
    """A Room has a name and a filepath that points to a .gif image"""
    
    def __init__(self, name:str, image_filepath:str) -> None:
        self.name = name
        self.image = image_filepath
        self.exits = {}
        self.items = {}
        self.grabs = []
        
        

    def add_exit(self, label:str, room:'Room'):
        self.exits[label] = room
        
    def add_item(self, label:str, desc:str):
        self.items[label] = desc
        
    def add_grabs(self, label:str):
        self.grabs.append(label)
        
    def del_grabs(self, label:str):
        self.grabs.remove(label)
        
    def __str__(self) -> str:
        result = f"You are in {self.name}\n"
        
        result+= "You see: "
        
        for item in self.items.keys():
            result += item + " "
        result += "\n"
        
        result += "Exits: "
        for exit in self.exits.keys():
            result += exit + " "
        result += "\n"
        
        return result
#the Item class takes care of the name and descriptions of the items to be imported into the game class 
class Item:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        
    #room 1
chair = Item("chair", "something about wicker and legs")
bigger_chair = Item("bigger chair", "more wicker and more legs")

#room 2
fireplace = Item("fireplace", "made of fire. grab the fire.")
more_chairs = Item("more_chairs", "another chair named more")

#room 3
desk = Item("desk","It is made of wicker also")
dimsdale_dimmadome = Item("dimsdale_dimmadome", "Owned by Doug zDimmadome, owner of Dimsdale Dimmadome.")
chair = Item("chair", "the og chair")

#room 4
croissant = Item("croissant", "made of butter. No flour.")
your_mother = Item("your_mother", "ur mom haha")
pbj = Item("pbj", "blech peanut butter is disgusting... nutella >>>>")

#room 5
potato = Item("potato", "POTATOOOOOOOOOOOOOOOOOOOOO")
windows = Item("windows", "wow look!! windows!! is that... daylight?!?! imagine being outside... *cough cough*")