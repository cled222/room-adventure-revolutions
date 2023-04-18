#Name: Caiden Ledet
#Date: datetime.now()
#Description: Room Adventure Revolutions


from tkinter import *
from Roomclass import *

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
        basement = Room("Basement", "basement_pic.gif")
        
        #add exits
        r1.add_exit("east", r2)
        r1.add_exit("south", r3)
        
        r2.add_exit("west", r1)
        r2.add_exit("south", r4)
        
        r3.add_exit("north", r1)
        r3.add_exit("east", r4)
        r3.add_exit("basement", basement)
        
        r4.add_exit("north",r2)
        r4.add_exit("west", r3)
        r4.add_exit("south", None)  #death
        
        #add items
        r1.add_item(chair.name, chair.description)
        r1.add_item(bigger_chair.name, bigger_chair.description)
        
        r2.add_item(fireplace.name, fireplace.description)
        r2.add_item(more_chairs.name, more_chairs.description)
        
        r3.add_item(desk.name, desk.description)
        r3.add_item(dimsdale_dimmadome.name, dimsdale_dimmadome.description)
        r3.add_item(chair.name, chair.description)
        
        r4.add_item(croissant.name, croissant.description)
        
        #add grabs to rooms
        r1.add_grabs("key")
        
        r2.add_grabs("fire")
        
        r3.add_grabs("doug")
        
        r4.add_grabs("butter")
        #set current room to the starting room

        self.current_room = r1 
        
        
    def setup_gui(self):
        #input element
        self.player_input = Entry(self, bg="white", fg="black")
        self.player_input.bind("<Return>", self.process)
        self.player_input.pack(side=BOTTOM, fill=X)
        self.player_input.focus()
        
        #image container and default image
        img = None  #represents actual image
        self.image_container = Label(self, width = Game.WIDTH // 2, image = img)
        self.image_container.image = img
        self.image_container.pack(side=LEFT,fill=Y)
        self.image_container.pack_propagate(False)  #prevent the image from modifying the size of the container that it is in
        
        #container for text
        text_container = Frame(self, width=Game.WIDTH //2)
        self.text = Text(text_container, bg="lightgrey", fg="black", state=DISABLED)
        self.text.pack(fill=Y, expand =1)
        text_container.pack(side=RIGHT, fill=Y)
        text_container.pack_propagate(False)
        
    
    def set_room_image(self):
        if self.current_room ==None:
            img = PhotoImage(file="skull.gif")
        else:
            img = PhotoImage(file=self.current_room.image)
            
        self.image_container.config(image=img)
        self.image_container.image = img 
    
    def set_status(self, status):
        self.text.config(state=NORMAL)  #makes it editable
        self.text.delete(1.0, END)  #yes 1.0 for text. It is 0 for entry elemnts
        
        if self.current_room == None:
            self.text.insert(END, Game.STATUS_DEAD)
        else:
            content = f"{self.current_room}\nYou are carrying: {self.inventory}\n\n{status}"
            self.text.insert(END, content)
            
        self.text.config(state = DISABLED)
    
    def clear_entry(self):
        self.player_input.delete(0,END)
    
    def handle_go(self, destination):
        status = Game.STATUS_BAD_EXIT
        
        if destination in self.current_room.exits:
            self.current_room = self.current_room.exits[destination]
            status = Game.STATUS_ROOM_CHANGE
            
        self.set_status(status)
        self.set_room_image()
    
    def handle_look(self, item):
        status = Game.STATUS_BAD_ITEM
        
        if item in self.current_room.items:
            status = self.current_room.items[item]
            
        self.set_status(status)
    
    def handle_take(self, grab):
        status = Game.STATUS_BAD_GRABS
        
        if grab in self.current_room.grabs:
            self.inventory.append(grab)
            self.current_room.del_grabs(grab)
            status = Game.STATUS_GRABBED
            
        self.set_status(status)
    
    def play(self):
        self.setup_game()
        self.setup_gui()
        self.set_room_image()
        self.set_status("")
    
    def process(self, event):
        action = self.player_input.get()
        action = action.lower() #lowercase
        
        if action in Game.EXIT_ACTIONS:
            exit()
            
        if self.current_room == None:
            self.clear_entry()
            return 
    
        words = action.split()
        
        if len(words) !=2:
            self.set_status(Game.STATUS_DEFAULT)
            return
        
        self.clear_entry()
        
        verb = words[0]
        noun = words[1]
        
        match verb:
            case "go":
                self.handle_go(destination = noun)
                
            case "look":
                self.handle_look(item = noun)
                
            case "take":
                self.handle_take(grab = noun)
                
            #default case: case_:
            
       
#main loop 
window = Tk()
window.title("Room Adventure.... REVOLUTIONS")
game = Game(window)
game.play()
window.mainloop()