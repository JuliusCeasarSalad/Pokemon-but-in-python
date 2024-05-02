#a simple pokemon battler for python
#for now its just two pokemon
import tkinter as tk
from tkinter import ttk
import random



#all type advantages
Typeadvantage = {
    "normal": (("rock", 0.5), ("ghost", 0), ("steel", 0.5)),
    "fire": (("fire", 0.5), ("water", 0.5), ("grass", 2), ("ice", 2), ("bug", 2), ("rock", 0.5), ("dragon", 0.5), ("steel", 2)),
    "water": (("fire", 2), ("water", 0.5), ("grass", 0.5), ("ground", 2), ("rock", 2), ("dragon", 0.5)),
    "grass": (("fire", 0.5), ("water", 2), ("grass", 0.5), ("poison", 0.5), ("ground", 2), ("flying", 0.5), ("bug", 0.5), ("rock", 2), ("dragon", 0.5), ("steel", 0.5)),
    "electric": (("water", 2), ("grass", 0.5), ("electric", 0.5), ("ground", 0), ("flying", 2), ("dragon", 0.5)),
    "ice": (("fire", 0.5), ("water", 0.5), ("grass", 2), ("ice", 0.5), ("ground", 2), ("flying", 2), ("dragon", 2), ("steel", 0.5)),
    "fighting": (("normal", 2), ("ice", 2), ("poison", 0.5), ("flying", 0.5), ("psychic", 0.5), ("bug", 0.5), ("rock", 2), ("ghost", 0), ("dark", 2), ("steel", 2), ("fairy", 0.5)),
    "poison": (("grass", 2), ("poison", 0.5), ("ground", 0.5), ("rock", 0.5), ("ghost", 0.5), ("steel", 0), ("fairy", 2)),
    "ground": (("fire", 2), ("grass", 0.5), ("electric", 2), ("poison", 2), ("flying", 0), ("bug", 0.5), ("rock", 2), ("steel", 2)),
    "flying": (("grass", 2), ("electric", 0.5), ("fighting", 2), ("bug", 2), ("rock", 0.5), ("steel", 0.5)),
    "psychic": (("fighting", 2), ("poison", 2), ("psychic", 0.5), ("dark", 0), ("steel", 0.5)),
    "bug": (("fire", 0.5), ("grass", 2), ("fighting", 0.5), ("poison", 0.5), ("flying", 0.5), ("psychic", 2), ("ghost", 0.5), ("dark", 2), ("steel", 0.5), ("fairy", 0.5)),
    "rock": (("fire", 2), ("ice", 2), ("fighting", 0.5), ("ground", 0.5), ("flying", 2), ("bug", 2), ("steel", 0.5)),
    "ghost": (("normal", 0), ("psychic", 2), ("ghost", 2), ("dark", 0.5)),
    "dragon": (("dragon", 2), ("steel", 0.5), ("fairy", 0)),
    "dark": (("fighting", 0.5), ("psychic", 2), ("ghost", 2), ("dark", 0.5), ("fairy", 0.5)),
    "steel": (("fire", 0.5), ("water", 0.5), ("electric", 0.5), ("ice", 2), ("rock", 2), ("steel", 0.5), ("fairy", 2)),
    "fairy": (("fire", 0.5), ("fighting", 2), ("poison", 0.5), ("dragon", 2), ("dark", 2), ("steel", 0.5)),
    " ":()
}

#Calcuate type bonuses
def calculateTypeBonus(attacker, defender):
    "Calcuates the types bonuses between two pokémon. Returns the bonus"
    #Type of attack
    attackType = attacker.move1.type
    
    #Types of defending pokemon
    defenderTypes = defender.type1, defender.type2

    #Type bonus multiplier
    bonus = 1

    #Attack boosts
    for modifier in Typeadvantage[attackType]:
        if modifier[0] in defenderTypes: bonus *= modifier[1]

    #Return the final boost
    return bonus

class Pokemon():
    def __init__(self, type1, type2, hp, atk, deff, spatk, spdef, speed, name, move1, move2, move3, move4):
        self.type1 = type1
        self.type2 = type2
        self.hp = (((2*hp + 31) * 100)/100) + 110
        self.atk = atk
        self.deff = deff
        self.spatk = spatk
        self.spdef = spdef
        self.speed = speed
        self.name = name
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4

def attack_(self, other):
    "Attack another pokemon with first move. First slot is the attacker and the second is the defender"
    #Critical hit (1/24 chance)
    critical = 1.5 if random.choice(f"{'0'*23}1") == "1" else 1
    #Random effect
    random_ = random.randint(85, 100) / 100
    #STAB bonus
    stab = 1.5 if self.move1.type in self.type1 else 1
    #Type bonus
    typeBonus = calculateTypeBonus(self, other)
    #Calculate damage
    if self.move1.special == True:
         other.hp -= round(((42 * self.move1.power * ((self.spatk / other.spdef))/2) / 50 + 2) * critical * random_ * stab * typeBonus)
    else:
        other.hp -= round(((42 * self.move1.power * ((self.atk / other.deff))/2) / 50 + 2) * critical * random_ * stab * typeBonus)
    
    #Set health to zero if their health goes below zero
    if other.hp <= 0: other.hp = 0
    Update1HP()
    Update2HP()

def attack_2(self, other):
    "Attack another pokemon with second move. First slot is the attacker and the second is the defender"
    #Critical hit (1/24 chance)
    critical = 1.5 if random.choice(f"{'0'*23}1") == "1" else 1
    #Random effect
    random_ = random.randint(85, 100) / 100
    #STAB bonus
    stab = 1.5 if self.move2.type in self.type1 else 1
    #Type bonus
    typeBonus = calculateTypeBonus(self, other)
    #Calculate damage
    if self.move2.special == True:
         other.hp -= round(((42 * self.move2.power * ((self.spatk / other.spdef))/2) / 50 + 2) * critical * random_ * stab * typeBonus)
    else:
        other.hp -= round(((42 * self.move2.power * ((self.atk / other.deff))/2) / 50 + 2) * critical * random_ * stab * typeBonus)
    
    #Set health to zero if their health goes below zero
    if other.hp <= 0: other.hp = 0
    Update1HP()
    Update2HP()

def attack_3(self, other):
    "Attack another pokemon with third move. First slot is the attacker and the second is the defender"
    #Critical hit (1/24 chance)
    critical = 1.5 if random.choice(f"{'0'*23}1") == "1" else 1
    #Random effect
    random_ = random.randint(85, 100) / 100
    #STAB bonus
    stab = 1.5 if self.move3.type in self.type1 else 1
    #Type bonus
    typeBonus = calculateTypeBonus(self, other)
    #Calculate damage
    if self.move3.special == True:
         other.hp -= round(((42 * self.move3.power * ((self.spatk / other.spdef))/2) / 50 + 2) * critical * random_ * stab * typeBonus)
    else:
        other.hp -= round(((42 * self.move3.power * ((self.atk / other.deff))/2) / 50 + 2) * critical * random_ * stab * typeBonus)
    #Set health to zero if their health goes below zero
    if other.hp <= 0: other.hp = 0
    Update1HP()
    Update2HP()

def attack_4(self, other):
    "Attack another pokemon with fourth move. First slot is the attacker and the second is the defender"
    #Critical hit (1/24 chance)
    critical = 1.5 if random.choice(f"{'0'*23}1") == "1" else 1
    #Random effect
    random_ = random.randint(85, 100) / 100
    #STAB bonus
    stab = 1.5 if self.move4.type in self.type1 else 1
    #Type bonus
    typeBonus = calculateTypeBonus(self, other)
    #Calculate damage
    if self.move4.special == True:
         other.hp -= round(((42 * self.move4.power * ((self.spatk / other.spdef))/2) / 50 + 2) * critical * random_ * stab * typeBonus)
    else:
        other.hp -= round(((42 * self.move4.power * ((self.atk / other.deff))/2) / 50 + 2) * critical * random_ * stab * typeBonus)
    
    #Set health to zero if their health goes below zero
    if other.hp <= 0: other.hp = 0
    Update1HP()
    Update2HP()

class Attacks():
    def __init__(self, type_, power, acuracy, pp, special, name):
        self.type = type_
        self.power = power
        self.acuracy = acuracy
        self.pp = pp
        self.special = special
        self.name = name

Psystrike = Attacks("psychic", 100, 100, 16, True, "Psystrike")
Icebeam = Attacks("ice", 90, 100, 16, True, "Ice beam")
Fireblast = Attacks("fire", 110, 85, 8, True, "Fire blast")
Shadowball = Attacks("ghost", 80, 100, 24, True, "Shadow ball")
Sludgewave = Attacks("poison", 95, 100, 16, True, "Sludge wave")
Earthpower = Attacks("ground", 90, 100, 16, False, "Earth power")
Thunderbolt = Attacks("electric", 90, 100, 24, True, "Thunderbolt")

Showdown = tk.Tk()
Showdown.title("Pykemon")

Mewtwo = Pokemon("psychic", " ", 109, 110, 90, 154, 90, 130, "Mewtwo", Psystrike, Icebeam, Fireblast, Shadowball)
Nidoking = Pokemon("poison","ground", 81, 102, 77, 85, 75, 85, "Nidoking", Sludgewave, Earthpower, Fireblast, Thunderbolt)

Mewtwo_sprite = tk.PhotoImage(file=r"C:\Users\messierj\OneDrive - Conseil scolaire Viamonde\Documents\Code projects\Python\Assets\Mewtwo.png")
Nidoking_sprite = tk.PhotoImage(file=r"C:\Users\messierj\OneDrive - Conseil scolaire Viamonde\Documents\Code projects\Python\Assets\Nidoking.png")

actingpokemon1 = Mewtwo
actingpokemon2 = Nidoking

Hp1 = tk.IntVar()
Hp1.set(actingpokemon1.hp)

Hp2 = tk.IntVar()
Hp2.set(actingpokemon2.hp)

def Update1HP():
    "Changes the displayed HP value of the first pokemon"
    Hpdisplay1.config(text=f"{Mewtwo.hp}")
        
def Update2HP():
    "Changes the displayed HP value of the second pokemon"
    Hpdisplay2.config(text=f"{Nidoking.hp}")

Hpdisplay1 = tk.Label(Showdown, text=f"{actingpokemon1.hp}")
Hpdisplay1.grid(column=0, row=1, sticky=tk.W, padx=10, pady=1)

Hpdisplay2 = tk.Label(Showdown, text=f"{actingpokemon2.hp}")
Hpdisplay2.grid(column=2, row=1, sticky=tk.W, padx=10, pady=1)

Pokemondisplay1 = tk.Label(Showdown, text=actingpokemon1.name)
Pokemondisplay1.grid(column=0, row=0, sticky=tk.W, padx=10, pady=1)

Pokemondisplay2 = tk.Label(Showdown, text= actingpokemon2.name)
Pokemondisplay2.grid(column=2, row=0, sticky=tk.W, padx=10, pady=1)

Pokemon_sprite1 = ttk.Label(Showdown, image= Mewtwo_sprite, padding= 10)
Pokemon_sprite1.grid(column=0, row=2, sticky=tk.W, padx=10, pady=1)

Pokemon_sprite2 = ttk.Label(Showdown, image= Nidoking_sprite, padding= 10)
Pokemon_sprite2.grid(column=2, row= 2, sticky=tk.W, padx=10, pady=1)

Pokemon1_attack_button= tk.Button(Showdown, text= f"{actingpokemon1.move1.name}", command=lambda: attack_(actingpokemon1, actingpokemon2))
Pokemon1_attack_button.grid(column=0, row=3, sticky=tk.W, padx=100, pady=1)

Pokemon1_attack_button1= tk.Button(Showdown, text= f"{actingpokemon1.move2.name}", command= lambda: attack_2(actingpokemon1,actingpokemon2))
Pokemon1_attack_button1.grid(column=0, row=4, sticky=tk.W, padx=100, pady=1)

Pokemon1_attack_button2= tk.Button(Showdown, text= f"{actingpokemon1.move3.name}", command= lambda: attack_3(actingpokemon1,actingpokemon2))
Pokemon1_attack_button2.grid(column=0, row=3, sticky=tk.W, padx=1, pady=1)

Pokemon1_attack_button3= tk.Button(Showdown, text= f"{actingpokemon1.move4.name}", command= lambda: attack_3(actingpokemon1,actingpokemon2))
Pokemon1_attack_button3.grid(column=0, row=4, sticky=tk.W, padx=1, pady=1)

Pokemon2_attack_button= tk.Button(Showdown, text= f"{actingpokemon2.move1.name}", command= lambda: attack_(actingpokemon2,actingpokemon1))
Pokemon2_attack_button.grid(column= 2, row= 3, sticky=tk.W, padx=1, pady=1)

Pokemon2_attack_button2= tk.Button(Showdown, text= f"{actingpokemon2.move2.name}", command= lambda: attack_2(actingpokemon2,actingpokemon1))
Pokemon2_attack_button2.grid(column= 3, row= 3, sticky=tk.W, padx=1, pady=1)

Pokemon2_attack_button3= tk.Button(Showdown, text= f"{actingpokemon2.move3.name}", command= lambda: attack_3(actingpokemon2,actingpokemon1))
Pokemon2_attack_button3.grid(column= 2, row= 4, sticky=tk.W, padx=1, pady=1)

Pokemon2_attack_button4= tk.Button(Showdown, text= f"{actingpokemon2.move4.name}", command= lambda: attack_4(actingpokemon2,actingpokemon1))
Pokemon2_attack_button4.grid(column= 3, row= 4, sticky=tk.W, padx=1, pady=1)


window_width = 500
window_height = 500

Showdown.columnconfigure(0, weight=1)
Showdown.columnconfigure(1, weight=3)

screen_width = Showdown.winfo_screenwidth()
screen_height = Showdown.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

Showdown.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
Showdown.resizable(False, False)

tk.mainloop()
