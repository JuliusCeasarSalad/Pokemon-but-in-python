from Attacks import *
import tkinter as tk
from CONSTANTS import *

class Pokemon:
    """Defines the pokemon object
    \ntype1/type2 are strings that are used in type advantage calculation 
    \nhp is an int that determines if the pokemon is still usable
    \natk/spatk is used in damage calculation on the attackers side
    \ndeff/spdef is used in damage calculation on the defenders side
    \nspeed is used in turn order
    \nname is the pokemons displayed name
    \nmoves is a list of attack objects that have their own seperate stats
    \nsprite is the image that tkinter renders on the window
    """
    def __init__(self, type1:str, type2:str, hp:int, atk:int, deff:int, spatk:int, spdef:int, speed:int, name:str, moves: list[Attacks], sprite: tk.PhotoImage):
        self.type1: int = type1
        self.type2: int = type2
        self.hp: int = (((2*hp + 31) * 100)/100) + 110
        self.atk: int = (1.5*atk)
        self.deff: int = deff
        self.spatk: int = (1.5*spatk)
        self.spdef: int = spdef
        self.speed: int = speed
        self.name: str = name
        self.moves: list[Attacks] = moves
        self.sprite: tk.PhotoImage = sprite

#TODO add abilites and form change
Mewtwo_sprite = tk.PhotoImage(file=f"{ASSET_PATH}\\Mewtwo.png")
Nidoking_sprite = tk.PhotoImage(file=f"{ASSET_PATH}\\Nidoking.png")
Moltres_sprite = tk.PhotoImage(file=f"{ASSET_PATH}\\Moltres.png")
Dragonite_sprite = tk.PhotoImage(file=f"{ASSET_PATH}\\dragonite.png")
Aegislash_sprite = tk.PhotoImage(file=f"{ASSET_PATH}\\aegislash.png")
Steelix_sprite = tk.PhotoImage(file=f"{ASSET_PATH}\\Steelix.png")
Carracosta_sprite = tk.PhotoImage(file=f"{ASSET_PATH}\\Carracosta.png")
Ninetalesalola_sprite = tk.PhotoImage(file=f"{ASSET_PATH}\\Ninetales_alola.png")
Bibarel_sprite = tk.PhotoImage(file=f"{ASSET_PATH}\\Bibarel.png")
Hitmonchan_sprite = tk.PhotoImage(file=f"{ASSET_PATH}\\Hitmonchan.png")
Reuniclus_sprite = tk.PhotoImage(file=f"{ASSET_PATH}\\Reuniclus.png")
Grimmsnarl_sptite = tk.PhotoImage(file=f"{ASSET_PATH}\\Grimsnarl.png")


Mewtwo = Pokemon("psychic", " ", 109, 110, 90, 154, 90, 130, "Mewtwo", [Psystrike, Icebeam, Fireblast, Shadowball], Mewtwo_sprite)
Nidoking = Pokemon("poison","ground", 81, 102, 77, 85, 75, 85, "Nidoking", [Sludgewave, Earthpower, Fireblast, Thunderbolt], Nidoking_sprite)
Moltres = Pokemon("fire", "flying", 90, 100, 90, 125, 85, 90, "Moltres", [Firepunch, Flamethrower, Bravebird, Fireblast], Moltres_sprite)
Dragonite = Pokemon("dragon", "flying", 91, 134, 95, 100, 100, 80, "Dragonite", [Outrage, Extremespeed, Firepunch, Earthquake], Dragonite_sprite)
Aegislash = Pokemon("steel", "ghost", 60, 70, 70, 70, 70, 60, "Aegislash", [Shadowball, Flashcannon, Steelbeam, Closecombat], Aegislash_sprite)
Steelix = Pokemon("steel", "ground", 75, 85, 200, 55, 65, 30, "Steelix", [Earthpower, Earthquake, Steelbeam, Flashcannon], Steelix_sprite)
Carracosta = Pokemon("water", "rock", 75, 108, 133, 83, 65, 32, "Carracosta", [StoneEdge, AquaJet, Earthquake, Icebeam], Carracosta_sprite)
Ninetalesalola = Pokemon("ice", "fairy", 73, 67, 75, 81, 100, 109, "Ninetails", [Icebeam, FreezDry, Moonblast, Extremespeed], Ninetalesalola_sprite)
Bibarel = Pokemon("normal", "water", 120, 120, 120, 120, 120, 120, "Bibarel", [Extremespeed, AquaJet, Firepunch, Closecombat], Bibarel_sprite)
Hitmonchan = Pokemon("fighing", " ", 50, 105, 79, 35, 110, 76, "Hitmonchan", [Firepunch, Icepunch, Thunderpunch, Closecombat], Hitmonchan_sprite)
Reuniclus = Pokemon("psychic", " ", 110, 65, 75, 125, 85, 30, "Reuniclus", [Psyshock, Shadowball, Moonblast, AquaJet], Reuniclus_sprite)
Grimmsnarl = Pokemon("dark", "fairy", 95, 120, 65, 95, 75, 60, "Grimmsnarl", [Shadowball, Spiritbreak, Suckerpunch, Moonblast], Grimmsnarl_sptite)