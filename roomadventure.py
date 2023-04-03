#Name: Caiden Ledet
#Date: datetime.now()
#Description: Room Adventure Revolutions

from tkinter import *

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
        


class Game(Frame):
    
    EXIT_ACTIONS = ["quit", "exit", "bye", "q"]
    
    #Statuses
    STATUS_DEFAULT = "I don't understand. Try [verb] [noun]. Valid verbs are go, look, take."
    STATUS_DEAD = "You are dead"
    STATUS_BAD_EXIT = "Invalid Exit."
    STATUS_ROOM_CHANGE = "Room Changed"
    STATUS_GRABBED = "Item Grabbed."
    STATUS_BAD_GRABS = "I can't grab that."
    STATUS_BAD_ITEM = "I don't see that."
    
    WIDTH = 800
    HEIGHT = 600
    
    def __init__(self, parent) -> None:
        self.inventory = []
        Frame.__init__(self,parent)
        self.pack(fill=BOTH, expand=1)
    
    def setup_game(self):
        
        #create rooms
        r1 = Room("Room 1", "room1.gif")
        r2 = Room("Room 2", "room2.gif")
        r3 = Room("Room 3", "room3.gif")
        r4 = Room("Room 4", "room4.gif")
        
        #add exits
        r1.add_exit("east", r2)
        r1.add_exit("south", r3)
        
        r2.add_exit("west", r1)
        r2.add_exit("south", r4)
        
        r3.add_exit("north", r1)
        r3.add_exit("east", r4)
        
        r4.add_exit("north",r2)
        r4.add_exit("west", r3)
        r4.add_exit("south", None)  #death
        
        #add items
        r1.add_item("chair", "something about wicker and legs")
        r1.add_item("bigger chair", "more wicker and more legs")
        
        r2.add_item("fireplace", "made of fire. grab the fire.")
        r2.add_item("more_chairs", "anothe chair named more")
        
        r3.add_item("desk","It is made of wicker also")
        r3.add_item("dimsdale_dimmadome", "Owned by Doug zDimmadome, owner of Dimsdale Dimmadome.")
        r3.add_item("chair", "the og chair")
        
        r4.add_item("croissant", "made of butter. No flour.")
        
        #add grabs to rooms
        
        
        #set current room to the starting room
        
        
        pass
    
    def setup_gui(self):
        pass
    
    def set_room_image(self):
        pass
    
    def set_status(self):
        pass
    
    def clear_entry(self):
        pass
    
    def handle_go(self):
        pass
    
    def handle_look(self):
        pass
    
    def handle_take(self):
        pass
    
    def play(self):
        pass
    
    def process(self, event):
        pass