#TODO Add implementation of pokedex.py so that any pokemon from gens 1-9 can be used
#While this is a finished project, I will be adding more features to it in the future - 22/01/2025
import tkinter as tk
from tkinter import ttk
from time import sleep
#import main window
from Showdown import *
#the default speed of the wait between the text changing
default_speed = 6
turn = 0
button_counter = 2

#import from local files
from Pokemon import *
from CONSTANTS import *
from player import Player
from Damage_calculation import *

#temp names
#TODO add custom player names
player0 = Player("P1",[Mewtwo, Moltres, Steelix, Ninetalesalola, Hitmonchan, Grimmsnarl])
player1 = Player("P2",[Nidoking, Dragonite, Aegislash, Carracosta, Bibarel, Reuniclus])

player0pokemon = 0
player1pokemon = 0

label_text = tk.StringVar(Showdown,"default")

effect_label = ttk.Label(Showdown,textvariable= label_text, relief="ridge",padding=[20,10])
effect_label.grid(column=0,row= 1,columnspan= 2,pady=10)

class Pokewrapper(ttk.LabelFrame):
    """wrapper for the pokemon objects"""
    def __init__(self, master, pokemon: Pokemon, player:Player, position: tuple[int, int]) -> None:
        """Position: (row, column)"""
        super().__init__(master)

        # saves the player
        self.player = player

        self.setup(pokemon)

        self.grid(row=position[0], column=position[1])
    
    def setup(self, pokemon):
         # Save pokemon
        self.pokemon = pokemon

        # Create attack buttons
        self.attackButtons = []

        for i, move in enumerate(pokemon.moves):
            button = ttk.Button(self, text=move.name, command=lambda i=i: self.button_press(i))
            button.grid(column=i%2, row=i//2+4, sticky=tk.W, padx=1, pady=1)
            self.attackButtons.append(button)

        # Create health label
        self.hplabel = ttk.Label(self,text=pokemon.hp)
        self.hplabel.grid(column=0, row=1, sticky=tk.W, padx=10, pady=1)

        # Create name display
        self.namedisplay = ttk.Label(self, text=pokemon.name)
        self.namedisplay.grid(column=0, row=0, sticky=tk.W, padx=10, pady=1)
        # Create pokemon sprite
        self.imagesprite = ttk.Label(self,image=pokemon.sprite)
        self.imagesprite.grid(column=0, row=2, sticky=tk.W, padx=10, pady=1)
    
    # disabling the buttons created by the __init__ method
    def disable_button(self):
        global button_counter
        for button in self.attackButtons:
            button.config(state= "disabled")
    
    def enable_button(self):
        for i, button in enumerate(self.attackButtons):
            if self.pokemon.moves[i].pp > 0:
                button.config(state="enabled")

    def attack(self, attack_regardless: bool= False):
        """`attack regardless` is for the slower pokewrapper to attack even if it is slower"""
        global button_counter
        # set the other pokemon to be the "other" variable
        if self in player0.pokemon:
            other = player1
        else:
            other = player0
        #Turn order
        #higher priority
        if self.pokemon.moves[self.move_number].priority > other.pokemon.moves[other.move_number].priority:
            if self.pokemon.moves[self.move_number].special:
                other.pokemon.hp -= calc_spc_dmg(self,other,self.move_number)
            else:
                other.pokemon.hp -= calc_phs_dmg(self,other,self.move_number)
            other.attack( attack_regardless=True)
        # equal priority
        elif self.pokemon.speed >= other.pokemon.speed:
            if self.pokemon.moves[self.move_number].special:
                other.pokemon.hp -= calc_spc_dmg(self,other,self.move_number)
            else:
                other.pokemon.hp -= calc_phs_dmg(self,other,self.move_number)
            other.attack( attack_regardless=True)
        #these 5 lines are to make the pokemon attack despite the slower speed and priority
        elif attack_regardless:
            if self.pokemon.moves[self.move_number].special:
                other.pokemon.hp -= calc_spc_dmg(self,other,self.move_number)
            else:
                other.pokemon.hp -= calc_phs_dmg(self,other,self.move_number)
            #this line is to keep the pokemons hp at zero should it try to go lower
            if other.pokemon.hp <= 0:
                other.pokemon.hp =0
                other.switch()
                return   
        else:
            other.attack()

        if self.pokemon.speed > other.pokemon.speed:
            label_text.set(self.pokemon.name + " used " + self.pokemon.moves[self.move_number].name)
        else:
            label_text.set(other.pokemon.name + " used " + other.pokemon.moves[other.move_number].name)
        
        sleep(default_speed)

        if (bonus := calculateTypeBonus(self.pokemon,other.pokemon,self.move_number)) == 0.5 :
            label_text.set("Its Not very effective")
        elif bonus == 2:
            label_text.set("Its Super effective")
        elif bonus == 4:
            label_text.set("Its Quad effective")
        elif bonus == 0:
            label_text.set("It does not effect the foe's pokemon")
        
        sleep(default_speed)

        if other.pokemon.speed < self.pokemon.speed:
            label_text.set(other.pokemon.name + " used " + other.pokemon.moves[other.move_number].name)
        else:
            label_text.set(self.pokemon.name + " used " + self.pokemon.moves[self.move_number].name)
            
        
        button_counter = 2
        self.hplabel.config(text=self.pokemon.hp)
        self.enable_button()

    def button_press(self, move_number: int):
        global button_counter
        self.disable_button()
        button_counter -= 1
        self.move_number = move_number
        if button_counter == 0:
            self.attack()
    
    def switch(self):
        global player0pokemon, player1pokemon
        if self.player == player0:
            player0pokemon += 1

            for child in self.winfo_children():
                child.destroy()

            self.setup(player0.pokemon[player0pokemon])
        elif self.player == player1:
            player1pokemon += 1

            for child in self.winfo_children():
                child.destroy()

            self.setup(player1.pokemon[player1pokemon])
        else:
            raise Exception("lSomething has gone horibly wrong\n payer0 or player1 are not equal to themselves")

player0wrapper = Pokewrapper(Showdown, player0.pokemon[player0pokemon], player0, (0,0))
player1wrapper = Pokewrapper(Showdown, player1.pokemon[player1pokemon], player1, (0,1))

Showdown.mainloop()