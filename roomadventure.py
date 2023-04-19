#Name: Caiden Ledet and Julia Wilson
#Date: datetime.now()
#Description: Room Adventure Revolutions

#Improvements
#Caiden-
#1. Split game class and room class into two seperate files(creating an item class within the room class)
#2. added the basement (extra room)
#3. added the use verb and winning graphic when you use the right item to escape

#Julia
#1. Added items and grabbables (most important being the rope which is used to escape)
#2. Added the escape method exit (window)
#3. Added a throw function (gets rid of item from your inventory)


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
    STATUS_USED = "Item used."      #added used status
    STATUS_THROW = "Item thrown."    
    STATUS_BAD_GRABS = "I can't grab that."
    STATUS_BAD_ITEM = "I don't see that."
    STATUS_BAD_USE = "I can't use that."    #added bad use status
    STATUS_BAD_THROW = "I can't throw that."
    
    WIDTH = 800
    HEIGHT = 600
    
    def __init__(self, parent) -> None:
        self.inventory = []
        self.rooms = [] #added to be able to call upon rooms in other functions
        Frame.__init__(self,parent)
        self.pack(fill=BOTH, expand=1)
    
    def setup_game(self):   #added self to these in order to be able to call upon them in other functions
        
        #create rooms
        self.r1 = Room("Room 1", "room1.gif")
        self.r2 = Room("Room 2", "room2.gif")
        self.r3 = Room("Room 3", "room3.gif")
        self.r4 = Room("Room 4", "room4.gif")
        self.basement = Room("Basement", "basement_pic.gif")
        self.rooms = [self.r1, self.r2, self.r3, self.r4, self.basement]
        
        #add exits
        self.r1.add_exit("east", self.r2)
        self.r1.add_exit("south", self.r3)
        
        self.r2.add_exit("west", self.r1)
        self.r2.add_exit("south", self.r4)
        
        self.r3.add_exit("north", self.r1)
        self.r3.add_exit("east", self.r4)
        self.r3.add_exit("basement", self.basement)
        
        self.r4.add_exit("north", self.r2)
        self.r4.add_exit("west", self.r3)

        self.basement.add_exit("up", self.r3) #new, adds another exit
        self.basement.add_exit("window", None) #new, allows to live!
        
        #add items
        #item name and descriptions now call upon the item class in the Roomclass file
        self.r1.add_item(chair.name, chair.description)
        self.r1.add_item(bigger_chair.name, bigger_chair.description)
        
        self.r2.add_item(fireplace.name, fireplace.description)
        self.r2.add_item(more_chairs.name, more_chairs.description)
        
        self.r3.add_item(desk.name, desk.description)
        self.r3.add_item(dimsdale_dimmadome.name, dimsdale_dimmadome.description)
        self.r3.add_item(chair.name, chair.description)
        
        self.r4.add_item(croissant.name, croissant.description)
        self.r4.add_item(your_mother.name, your_mother.description) #new
        self.r4.add_item(pbj.name, pbj.description) #new (I'm allergic to PBJ :) )

        self.basement.add_item(potato.name, potato.description) #new
        self.basement.add_item(windows.name, windows.description) #new
        
        #add grabs to rooms
        self.r1.add_grabs("key")
        
        self.r2.add_grabs("fire")
        
        self.r3.add_grabs("doug")
        
        self.r4.add_grabs("butter")

        self.basement.add_grabs("rope") #new


        #set current room to the starting room
        self.current_room = self.r1 
        
        
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
        
    def winner(self, image):    #added to create the winning image after you have successfully escaped
        img = PhotoImage(file = image)
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
            
    def handle_use(self, item): #added to utilize a grabbable, in this case a rope, which is used to escape through window
        status = Game.STATUS_BAD_USE
        
        if item in self.inventory:
            self.inventory.remove(item)
            status = Game.STATUS_USED
            
        #if the player has the rope in their inventory and are in the basement (location of the window) they are able to escape when use is enabled
        if item == "rope" and self.current_room == self.basement:   
                    self.winner("winner.gif")
            
        self.set_status(status)
        #self.set_room_image()

    #new, sets the general message to an error unless a grab is in the inventory, 
    #in which it puts the grab form the inventory into the current room 
    def handle_throw(self, grab):
        status = Game.STATUS_BAD_THROW
        
        if grab in self.inventory:
            self.inventory.remove(grab)
            self.current_room.add_grabs(grab)
            status = Game.STATUS_THROW
            
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
            
            case "use":
                self.handle_use(item = noun)    #added to handle the match verb when use is called upon

            #new, allows for the user to command "throw"
            case "throw":
                self.handle_throw(grab = noun)
                
            #default case: case_:
               
#main loop 
window = Tk()
window.title("Room Adventure.... REVOLUTIONS")
game = Game(window)
game.play()
window.mainloop()