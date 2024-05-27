import tkinter as tk
from tkinter import ttk
import random
import os

assetpath = f"{os.path.dirname(__file__)}\\Assets"

#all type advantages
Typeadvantage = {
    #defender    attacker
    "normal": (("rock", 0.5), ("ghost", 0), ("steel", 0.5)),
    "fire": (("fire", 0.5), ("water", 0.5), ("grass", 2), ("ice", 2), ("bug", 2), ("rock", 0.5), ("dragon", 0.5), ("steel", 2)),
    "water": (("fire", 2), ("water", 0.5), ("grass", 0.5), ("ground", 2), ("rock", 2), ("dragon", 0.5)),
    "grass": (("fire", 0.5), ("water", 2), ("grass", 0.5), ("poison", 0.5), ("ground", 2), ("flying", 0.5), ("bug", 0.5), ("rock", 2), ("dragon", 0.5), ("steel", 0.5)),
    "electric": (("water", 2), ("grass", 0.5), ("electric", 0.5), ("ground", 0), ("flying", 2), ("dragon", 0.5)),
    "ice": (("fire", 0.5), ("water", 0.5), ("grass", 2), ("ice", 0.5), ("ground", 2), ("flying", 2), ("dragon", 2), ("steel", 0.5)),
    "fighting": (("normal", 2), ("ice", 2), ("poison", 0.5), ("flying", 0.5), ("psychic", 0.5), ("bug", 0.5), ("rock", 2), ("ghost", 0), ("dark", 2), ("steel", 2), ("fairy", 0.5)),
    "poison": (("grass", 2), ("poison", 0.5), ("ground", 0.5), ("rock", 0.5), ("ghost", 0.5), ("steel", 0), ("fairy", 2)),
    "ground": (("fire", 2), ("grass", 0.5), ("electric", 2), ("poison", 2), ("flying", 0), ("bug", 0.5), ("rock", 2), ("steel", 2)),
    "flying": (("grass", 0.5), ("electric", 2), ("fighting", 0.5), ("bug", 0.5), ("rock", 2), ("steel", 0.5)),
    "psychic": (("fighting", 0.5), ("poison", 2), ("psychic", 0.5), ("dark", 2), ("steel", 0.5)),
    "bug": (("fire", 0.5), ("grass", 2), ("fighting", 0.5), ("poison", 0.5), ("flying", 0.5), ("psychic", 2), ("ghost", 0.5), ("dark", 2), ("steel", 0.5), ("fairy", 0.5)),
    "rock": (("fire", 2), ("ice", 2), ("fighting", 0.5), ("ground", 0.5), ("flying", 2), ("bug", 2), ("steel", 0.5)),
    "ghost": (("normal", 0), ("psychic", 2), ("ghost", 2), ("dark", 0.5)),
    "dragon": (("dragon", 2), ("steel", 0.5), ("fairy", 0)),
    "dark": (("fighting", 0.5), ("psychic", 2), ("ghost", 2), ("dark", 0.5), ("fairy", 0.5)),
    "steel": (("fire", 0.5), ("water", 0.5), ("electric", 0.5), ("ice", 2), ("rock", 2), ("steel", 0.5), ("fairy", 2)),
    "fairy": (("fire", 0.5), ("fighting", 2), ("poison", 0.5), ("dragon", 2), ("dark", 2), ("steel", 0.5)),
    " " : ()
}

turn = 0

playerone = "DO NOT REUSE THIS STRING NUMBER 1"
playertwo = "DO NOT REUSE THIS STRING NUMBER 2"

onemove1 = True
onemove2 = True
onemove3 = True
onemove4 = True
twomove1 = True
twomove2 = True
twomove3 = True
twomove4 = True

#Calcuate type bonuses
def calculateTypeBonus(attacker, defender, movenumber):
    "Calcuates the types bonuses between two pokémon. Returns the bonus"
    #Type of attack
    
    attackType = attacker.moves[movenumber].type
    
    #Types of defending pokemon
    defenderTypes = (defender.type1, defender.type2)

    #Type bonus multiplier
    bonus = 1

    #Attack boosts
    for modifier in Typeadvantage[attackType]:
        if modifier[0] in defenderTypes: 
            bonus *= modifier[1]

    #Return the final boost
    return bonus

class Pokemon():
    "Defines the pokemon object"
    def __init__(self, type1, type2, hp, atk, deff, spatk, spdef, name, moves, sprite):
        self.type1 = type1
        self.type2 = type2
        self.hp = (((2*hp + 31) * 100)/100) + 110
        self.atk = (1.5*atk)
        self.deff = deff
        self.spatk = (1.5*spatk)
        self.spdef = spdef
        self.name = name
        self.moves = moves
        self.sprite = sprite

class Attacks():
    "Defines the Attacks class"
    def __init__(self, type_, power, acuracy, pp, special, name):
        self.type = type_
        self.power = power
        self.acuracy = acuracy
        self.pp = pp
        self.special = special
        self.name = name

def attack_(self, other, movenumber):
    "Attack another pokemon with first move. First slot is the attacker and the second is the defender"
    #Critical hit (1/24 chance)
    critical = 1.5 if random.choice(f"{'0'*23}1") == "1" else 1
    #Random effect
    random_ = random.randint(85, 100) / 100
    #STAB bonus
    stab = 1.5 if self.moves[movenumber].type in self.type1 else 1
    #Type bonus
    typeBonus = calculateTypeBonus(self, other, movenumber)
    #Calculate damage
    if random.randint(1, 100) <= self.moves[movenumber].acuracy:
        if self.moves[movenumber].special == True:
            other.hp -= round(((42 * self.moves[movenumber].power * (self.spatk / other.spdef) / 50 + 2) * critical * random_ * stab * typeBonus) / 2)
        else:
            other.hp -= round(((42 * self.moves[movenumber].power * (self.atk / other.deff) / 50 + 2) * critical * random_ * stab * typeBonus) / 2)
    
    #Set health to zero if their health goes below zero
    if other.hp <= 0: other.hp = 0

    self.moves[movenumber].pp -= 1
    
    if actingpokemon2[len(actingpokemon2)-1].hp == 0:
        win(playerone)
    else:
        if actingpokemon1[len(actingpokemon1)-1].hp == 0:
            win(playertwo)
        else:
            deathswitch()
            UpdateHP()
            Turnswitch()
            movedisable(self)

def Turnswitch():
    "Changes the turn"
    global turn
    if turn == 0:
        turn = 1
    else:
        turn = 0
    Turnmovedisable()

def switch_1():
    "Switches the first pokemon"
    global playeronepokemon
    playeronepokemon += 1
    UpdateHP()
    UpdateMoves()
    UpdateName()
    Updatesprite()

def switch_2():
    "Switches the second pokemon"
    global playertwopokemon
    playertwopokemon += 1
    UpdateHP()
    UpdateMoves()
    UpdateName()
    Updatesprite()

def UpdateHP():
    "Changes the displayed HP value of the pokemons"
    Hpdisplay1.config(text=f"{actingpokemon1[playeronepokemon].hp}")
    Hpdisplay2.config(text=f"{actingpokemon2[playertwopokemon].hp}")

def UpdateMoves():
    "Updates the moves of the pokemon"
    Pokemon1_attack_button.config(text=f"{actingpokemon1[playeronepokemon].moves[0].name}",command= lambda: attack_(actingpokemon1[playeronepokemon], actingpokemon2[playertwopokemon],0))
    Pokemon1_attack_button1.config(text=f"{actingpokemon1[playeronepokemon].moves[1].name}",command= lambda: attack_(actingpokemon1[playeronepokemon], actingpokemon2[playertwopokemon],1))
    Pokemon1_attack_button2.config(text=f"{actingpokemon1[playeronepokemon].moves[2].name}",command= lambda: attack_(actingpokemon1[playeronepokemon], actingpokemon2[playertwopokemon],2))
    Pokemon1_attack_button3.config(text=f"{actingpokemon1[playeronepokemon].moves[3].name}",command= lambda: attack_(actingpokemon1[playeronepokemon], actingpokemon2[playertwopokemon],3))
    Pokemon2_attack_button.config(text=f"{actingpokemon2[playertwopokemon].moves[0].name}", command= lambda: attack_(actingpokemon2[playertwopokemon],actingpokemon1[playeronepokemon],0))
    Pokemon2_attack_button2.config(text=f"{actingpokemon2[playertwopokemon].moves[1].name}", command= lambda: attack_(actingpokemon2[playertwopokemon],actingpokemon1[playeronepokemon],1))
    Pokemon2_attack_button3.config(text=f"{actingpokemon2[playertwopokemon].moves[2].name}", command= lambda: attack_(actingpokemon2[playertwopokemon],actingpokemon1[playeronepokemon],2))
    Pokemon2_attack_button4.config(text=f"{actingpokemon2[playertwopokemon].moves[3].name}", command= lambda: attack_(actingpokemon2[playertwopokemon],actingpokemon1[playeronepokemon],3))

def movedisable(self):
    "disables the pokemons moves"
    global onemove1, onemove2, onemove3, onemove4, twomove1, twomove2, twomove3, twomove4
    if self.moves[0].pp == 0 and actingpokemon1[playeronepokemon] == self:
        onemove1 = False
        Pokemon1_attack_button.config(state= "disabled")
    if self.moves[1].pp == 0 and actingpokemon1[playeronepokemon] == self:
        onemove2 = False
        Pokemon1_attack_button1.config(state= "disabled")
    if self.moves[2].pp == 0 and actingpokemon1[playeronepokemon] == self:
        onemove3 = False
        Pokemon1_attack_button2.config(state= "disabled")
    if self.moves[3].pp == 0 and actingpokemon1[playeronepokemon] == self:
        onemove4 = False
        Pokemon1_attack_button3.config(state= "disabled")
    if self.moves[0].pp == 0 and actingpokemon2[playertwopokemon] == self:
        twomove1 = False
        Pokemon2_attack_button.config(state= "disabled")
    if self.moves[1].pp == 0 and actingpokemon2[playertwopokemon] == self:
        twomove2 = False
        Pokemon2_attack_button2.config(state= "disabled")
    if self.moves[2].pp == 0 and actingpokemon2[playertwopokemon] == self:
        twomove3 = False
        Pokemon2_attack_button3.config(state= "disabled")
    if self.moves[3].pp == 0 and actingpokemon2[playertwopokemon] == self:
        twomove4 = False
        Pokemon2_attack_button4.config(state= "disabled")
        
def UpdateName():
    "Updates the name"
    Pokemondisplay1.config(text=f"{actingpokemon1[playeronepokemon].name}")
    Pokemondisplay2.config(text=f"{actingpokemon2[playertwopokemon].name}")

def Updatesprite():
    "Updates the sprite"
    Pokemon_sprite1.config(image=f"{actingpokemon1[playeronepokemon].sprite}")
    Pokemon_sprite2.config(image=f"{actingpokemon2[playertwopokemon].sprite}")

def win(winner):
    "destroys the wigets and show the winner"
    for wiget in Showdown.winfo_children():
        wiget.destroy()
    if winner == playerone:
        winnerlabel = ttk.Label(Showdown, text="Player 1 won!",font=("Arial", 36))
        winnerlabel.grid(column= 1, row= 0, padx=100, pady= 200)
    elif winner == playertwo:
        winnerlabel = ttk.Label(Showdown, text="Player 2 won!",font=("Arial", 36))
        winnerlabel.grid(column= 1, row= 0, padx=100, pady= 200)

def deathswitch():
    "Switches when the acting pokemon dies"
    if actingpokemon1[playeronepokemon].hp == 0:
        switch_1()
    elif actingpokemon2[playertwopokemon].hp == 0:
        switch_2()

Psystrike = Attacks("psychic", 100, 100, 16, True, "Psystrike")
Icebeam = Attacks("ice", 90, 100, 16, True, "Ice beam")
Fireblast = Attacks("fire", 110, 85, 8, True, "Fire blast")
Shadowball = Attacks("ghost", 80, 100, 24, True, "Shadow ball")
Sludgewave = Attacks("poison", 95, 100, 16, True, "Sludge wave")
Earthpower = Attacks("ground", 90, 100, 16, False, "Earth power")
Thunderbolt = Attacks("electric", 90, 100, 24, True, "Thunderbolt")
Firepunch = Attacks("fire", 75, 100, 15, False, "Fire punch")
Thunderpunch = Attacks("electric", 75, 100, 15, False, "Thunder punch")
Icepunch = Attacks("ice", 75, 100, 15, False, "Ice punch")
Flamethrower = Attacks("fire", 90, 100, 15, True, "Flamethrower")
Bravebird = Attacks("flying", 120, 100, 15, False, "Brave bird")
Hurricane = Attacks("flying", 110, 70, 16, True, "Hurricane")
Outrage = Attacks("dragon", 120, 100, 10, False, "Outrage")
Extremespeed = Attacks("normal", 80, 100, 5, False, "Extreme Speed")
Earthquake = Attacks("ground", 100, 100, 10, False, "Earthquake")
Flashcannon = Attacks("steel", 80, 100, 10, True, "Flash cannon")
Steelbeam = Attacks("steel", 140, 95, 5, True, "Steel beam")
Closecombat = Attacks("fighting", 120, 100, 5, False, "Close combat")
StoneEdge = Attacks("rock", 100, 80, 5, False, "Stone Edge")
AquaJet = Attacks("water", 40, 100, 20, False, "Aqua Jet")
FreezDry = Attacks("ice", 70, 100, 20, True, "Freeze-dry")
Moonblast = Attacks("fairy", 95, 100, 15, True, "Moon blast")
Psyshock = Attacks("psychic", 80, 100, 10, True, "Psyshock")
Spiritbreak = Attacks("fairy", 75, 100, 15, True, "Spirit Break")
Suckerpunch = Attacks("dark", 70, 100, 5, False, "Sucker Punch")

Showdown = tk.Tk()
Showdown.title("Pykemon")

playeronepokemon = 0
playertwopokemon = 0

Mewtwo_sprite = tk.PhotoImage(file=f"{assetpath}\\Mewtwo.png")
Nidoking_sprite = tk.PhotoImage(file=f"{assetpath}\\Nidoking.png")
Moltres_sprite = tk.PhotoImage(file=f"{assetpath}\\Moltres.png")
Dragonite_sprite = tk.PhotoImage(file=f"{assetpath}\\dragonite.png")
Aegislash_sprite = tk.PhotoImage(file=f"{assetpath}\\aegislash.png")
Steelix_sprite = tk.PhotoImage(file=f"{assetpath}\\Steelix.png")
Carracosta_sprite = tk.PhotoImage(file=f"{assetpath}\\Carracosta.png")
Ninetalesalola_sprite = tk.PhotoImage(file=f"{assetpath}\\Ninetales_alola.png")
Bibarel_sprite = tk.PhotoImage(file=f"{assetpath}\\Bibarel.png")
Hitmonchan_sprite = tk.PhotoImage(file=f"{assetpath}\\Hitmonchan.png")
Reuniclus_sprite = tk.PhotoImage(file=f"{assetpath}\\Reuniclus.png")
Grimmsnarl_sptite = tk.PhotoImage(file=f"{assetpath}\\Grimsnarl.png")

Mewtwo = Pokemon("psychic", " ", 109, 110, 90, 154, 90, "Mewtwo", [Psystrike, Icebeam, Fireblast, Shadowball], Mewtwo_sprite)
Nidoking = Pokemon("poison","ground", 81, 102, 77, 85, 75, "Nidoking", [Sludgewave, Earthpower, Fireblast, Thunderbolt], Nidoking_sprite)
Moltres = Pokemon("fire", "flying", 90, 100, 90, 125, 85, "Moltres", [Firepunch, Flamethrower, Bravebird, Fireblast], Moltres_sprite)
Dragonite = Pokemon("dragon", "flying", 91, 134, 95, 100, 100, "Dragonite", [Outrage, Extremespeed, Firepunch, Earthquake], Dragonite_sprite)
Aegislash = Pokemon("steel", "ghost", 60, 70, 70, 70, 70, "Aegislash", [Shadowball, Flashcannon, Steelbeam, Closecombat], Aegislash_sprite)
Steelix = Pokemon("steel", "ground", 75, 85, 200, 55, 65, "Steelix", [Earthpower, Earthquake, Steelbeam, Flashcannon], Steelix_sprite)
Carracosta = Pokemon("water", "rock", 75, 108, 133, 83, 65, "Carracosta", [StoneEdge, AquaJet, Earthquake, Icebeam], Carracosta_sprite)
Ninetalesalola = Pokemon("ice", "fairy", 73, 67, 75, 81, 100, "Ninetails", [Icebeam, FreezDry, Moonblast, Extremespeed], Ninetalesalola_sprite)
Bibarel = Pokemon("normal", "water", 120, 120, 120, 120, 120, "Bibarel", [Extremespeed, AquaJet, Firepunch, Closecombat], Bibarel_sprite)
Hitmonchan = Pokemon("fighing", " ", 50, 105, 79, 35, 110, "Hitmonchan", [Firepunch, Icepunch, Thunderpunch, Closecombat], Hitmonchan_sprite)
Reuniclus = Pokemon("psychic", " ", 110, 65, 75, 125, 85, "Reuniclus", [Psyshock, Shadowball, Moonblast, AquaJet], Reuniclus_sprite)
Grimmsnarl = Pokemon("dark", "fairy", 95, 120, 65, 95, 75, "Grimmsnarl", [Shadowball, Spiritbreak, Suckerpunch, Moonblast], Grimmsnarl_sptite)

actingpokemon1 = [Mewtwo, Moltres, Steelix, Ninetalesalola, Hitmonchan, Grimmsnarl]
actingpokemon2 = [Nidoking, Dragonite, Aegislash, Carracosta, Bibarel, Reuniclus]

Hpdisplay1 = ttk.Label(Showdown, text=f"{actingpokemon1[playeronepokemon].hp}")
Hpdisplay1.grid(column=0, row=1, sticky=tk.W, padx=10, pady=1)

Hpdisplay2 = ttk.Label(Showdown, text=f"{actingpokemon2[playertwopokemon].hp}")
Hpdisplay2.grid(column=2, row=1, sticky=tk.W, padx=10, pady=1)

Pokemondisplay1 = ttk.Label(Showdown, text=actingpokemon1[playeronepokemon].name)
Pokemondisplay1.grid(column=0, row=0, sticky=tk.W, padx=10, pady=1)

Pokemondisplay2 = ttk.Label(Showdown, text= actingpokemon2[playertwopokemon].name)
Pokemondisplay2.grid(column=2, row=0, sticky=tk.W, padx=10, pady=1)

Pokemon_sprite1 = ttk.Label(Showdown, image= actingpokemon1[playeronepokemon].sprite, padding= 10)
Pokemon_sprite1.grid(column=0, row=2, sticky=tk.W, padx=10, pady=1)

Pokemon_sprite2 = ttk.Label(Showdown, image= actingpokemon2[playertwopokemon].sprite, padding= 10)
Pokemon_sprite2.grid(column=2, row= 2, sticky=tk.W, padx=10, pady=1)

Pokemon1_attack_button= ttk.Button(Showdown, text= f"{actingpokemon1[playeronepokemon].moves[0].name}", command=lambda: attack_(actingpokemon1[playeronepokemon], actingpokemon2[playertwopokemon],0))
Pokemon1_attack_button.grid(column=0, row=3, sticky=tk.W, padx=100, pady=1)

Pokemon1_attack_button1= ttk.Button(Showdown, text= f"{actingpokemon1[playeronepokemon].moves[1].name}", command= lambda: attack_(actingpokemon1[playeronepokemon],actingpokemon2[playertwopokemon],1))
Pokemon1_attack_button1.grid(column=0, row=4, sticky=tk.W, padx=100, pady=1)

Pokemon1_attack_button2= ttk.Button(Showdown, text= f"{actingpokemon1[playeronepokemon].moves[2].name}", command= lambda: attack_(actingpokemon1[playeronepokemon],actingpokemon2[playertwopokemon],2))
Pokemon1_attack_button2.grid(column=0, row=3, sticky=tk.W, padx=1, pady=1)

Pokemon1_attack_button3= ttk.Button(Showdown, text= f"{actingpokemon1[playeronepokemon].moves[3].name}", command= lambda: attack_(actingpokemon1[playeronepokemon],actingpokemon2[playertwopokemon],3))
Pokemon1_attack_button3.grid(column=0, row=4, sticky=tk.W, padx=1, pady=1)

Pokemon2_attack_button= ttk.Button(Showdown, text= f"{actingpokemon2[playertwopokemon].moves[0].name}", command= lambda: attack_(actingpokemon2[playertwopokemon],actingpokemon1[playeronepokemon],0))
Pokemon2_attack_button.grid(column= 2, row= 3, sticky=tk.W, padx=1, pady=1)

Pokemon2_attack_button2= ttk.Button(Showdown, text= f"{actingpokemon2[playertwopokemon].moves[1].name}", command= lambda: attack_(actingpokemon2[playertwopokemon],actingpokemon1[playeronepokemon],1))
Pokemon2_attack_button2.grid(column= 3, row= 3, sticky=tk.W, padx=1, pady=1)

Pokemon2_attack_button3= ttk.Button(Showdown, text= f"{actingpokemon2[playertwopokemon].moves[2].name}", command= lambda: attack_(actingpokemon2[playertwopokemon],actingpokemon1[playeronepokemon],2))
Pokemon2_attack_button3.grid(column= 2, row= 4, sticky=tk.W, padx=1, pady=1)

Pokemon2_attack_button4= ttk.Button(Showdown, text= f"{actingpokemon2[playertwopokemon].moves[3].name}", command= lambda: attack_(actingpokemon2[playertwopokemon],actingpokemon1[playeronepokemon],3))
Pokemon2_attack_button4.grid(column= 3, row= 4, sticky=tk.W, padx=1, pady=1)

def Turnmovedisable():
    "Disables the moves of the inactive pokemon"
    if turn == 0:
        if onemove1 == False:
            Pokemon2_attack_button.config(state= "disabled")
            Pokemon2_attack_button2.config(state= "disabled")
            Pokemon2_attack_button3.config(state= "disabled")
            Pokemon2_attack_button4.config(state= "disabled")
            Pokemon1_attack_button1.config(state= "active")
            Pokemon1_attack_button2.config(state= "active")
            Pokemon1_attack_button3.config(state= "active")
        elif onemove2 == False:
            Pokemon2_attack_button.config(state= "disabled")
            Pokemon2_attack_button2.config(state= "disabled")
            Pokemon2_attack_button3.config(state= "disabled")
            Pokemon2_attack_button4.config(state= "disabled")
            Pokemon1_attack_button.config(state= "active")  
            Pokemon1_attack_button2.config(state= "active")
            Pokemon1_attack_button3.config(state= "active")
        elif onemove3 == False:
            Pokemon2_attack_button.config(state= "disabled")
            Pokemon2_attack_button2.config(state= "disabled")
            Pokemon2_attack_button3.config(state= "disabled")
            Pokemon2_attack_button4.config(state= "disabled")
            Pokemon1_attack_button.config(state= "active")
            Pokemon1_attack_button1.config(state= "active")
            Pokemon1_attack_button3.config(state= "active")
        elif onemove4 == False:
            Pokemon2_attack_button.config(state= "disabled")
            Pokemon2_attack_button2.config(state= "disabled")
            Pokemon2_attack_button3.config(state= "disabled")
            Pokemon2_attack_button4.config(state= "disabled")
            Pokemon1_attack_button.config(state= "active")
            Pokemon1_attack_button1.config(state= "active")
            Pokemon1_attack_button2.config(state= "active")
        else:
            Pokemon2_attack_button.config(state= "disabled")
            Pokemon2_attack_button2.config(state= "disabled")
            Pokemon2_attack_button3.config(state= "disabled")
            Pokemon2_attack_button4.config(state= "disabled")
            Pokemon1_attack_button.config(state= "active")
            Pokemon1_attack_button1.config(state= "active")
            Pokemon1_attack_button2.config(state= "active")
            Pokemon1_attack_button3.config(state= "active")
    else:
        if twomove1 == False:
            Pokemon2_attack_button2.config(state= "active")
            Pokemon2_attack_button3.config(state= "active")
            Pokemon2_attack_button4.config(state= "active")
            Pokemon1_attack_button.config(state= "disabled")
            Pokemon1_attack_button1.config(state= "disabled")
            Pokemon1_attack_button2.config(state= "disabled")
            Pokemon1_attack_button3.config(state= "disabled")
        elif twomove2 == False:
            Pokemon2_attack_button.config(state= "active")
            Pokemon2_attack_button3.config(state= "active")
            Pokemon2_attack_button4.config(state= "active")
            Pokemon1_attack_button.config(state= "disabled")
            Pokemon1_attack_button1.config(state= "disabled")
            Pokemon1_attack_button2.config(state= "disabled")
            Pokemon1_attack_button3.config(state= "disabled")
        elif twomove3 == False:
            Pokemon2_attack_button.config(state= "active")
            Pokemon2_attack_button2.config(state= "active")
            Pokemon2_attack_button4.config(state= "active")
            Pokemon1_attack_button.config(state= "disabled")
            Pokemon1_attack_button1.config(state= "disabled")
            Pokemon1_attack_button2.config(state= "disabled")
            Pokemon1_attack_button3.config(state= "disabled")
        elif twomove4 == False:
            Pokemon2_attack_button.config(state= "active")
            Pokemon2_attack_button2.config(state= "active")
            Pokemon2_attack_button3.config(state= "active")
            Pokemon1_attack_button.config(state= "disabled")
            Pokemon1_attack_button1.config(state= "disabled")
            Pokemon1_attack_button2.config(state= "disabled")
            Pokemon1_attack_button3.config(state= "disabled")
        else:
            Pokemon2_attack_button.config(state= "active")
            Pokemon2_attack_button2.config(state= "active")
            Pokemon2_attack_button3.config(state= "active")
            Pokemon2_attack_button4.config(state= "active")
            Pokemon1_attack_button.config(state= "disabled")
            Pokemon1_attack_button1.config(state= "disabled")
            Pokemon1_attack_button2.config(state= "disabled")
            Pokemon1_attack_button3.config(state= "disabled")

Turnmovedisable()

window_width = 500
window_height = 230

Showdown.columnconfigure(0, weight=1)
Showdown.columnconfigure(1, weight=3)

screen_width = Showdown.winfo_screenwidth()
screen_height = Showdown.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

Showdown.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
Showdown.resizable(False, False)

Showdown.mainloop()
