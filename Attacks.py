class Attacks:
    "Defines the Attacks class"
    def __init__(self, type_, power, acuracy, priority=0, pp=1, special=False, name="MISSING MOVE"):
        self.type: str = type_
        self.power: int = power
        self.acuracy: int = acuracy
        self.priority: int = priority
        self.pp: int = pp
        self.special: bool = special
        self.name: str = name


#TODO Add implemetation for showdowns movelist, move effect, status moves
Psystrike = Attacks("psychic", 100, 100, 0, 16, True, "Psystrike")
Icebeam = Attacks("ice", 90, 100, 0, 16, True, "Ice beam")
Fireblast = Attacks("fire", 110, 85, 0, 8, True, "Fire blast")
Shadowball = Attacks("ghost", 80, 100, 0, 24, True, "Shadow ball")
Sludgewave = Attacks("poison", 95, 100, 0, 16, True, "Sludge wave")
Earthpower = Attacks("ground", 90, 100, 0, 16, False, "Earth power")
Thunderbolt = Attacks("electric", 90, 100, 0, 24, True, "Thunderbolt")
Firepunch = Attacks("fire", 75, 100, 0, 15, False, "Fire punch")
Thunderpunch = Attacks("electric", 75, 100, 0, 15, False, "Thunder punch")
Icepunch = Attacks("ice", 75, 100, 0, 15, False, "Ice punch")
Flamethrower = Attacks("fire", 90, 100, 0, 15, True, "Flamethrower")
Bravebird = Attacks("flying", 120, 100, 0, 15, False, "Brave bird")
Hurricane = Attacks("flying", 110, 70, 0, 16, True, "Hurricane")
Outrage = Attacks("dragon", 120, 100, 0, 10, False, "Outrage")
Extremespeed = Attacks("normal", 80, 100, 1, 5, False, "Extreme Speed")
Earthquake = Attacks("ground", 100, 100, 0, 10, False, "Earthquake")
Flashcannon = Attacks("steel", 80, 100, 0, 10, True, "Flash cannon")
Steelbeam = Attacks("steel", 140, 95, 0, 5, True, "Steel beam")
Closecombat = Attacks("fighting", 120, 100, 0, 5, False, "Close combat")
StoneEdge = Attacks("rock", 100, 80, 0, 5, False, "Stone Edge")
AquaJet = Attacks("water", 40, 100, 0, 20, False, "Aqua Jet")
FreezDry = Attacks("ice", 70, 100, 0, 20, True, "Freeze-dry")
Moonblast = Attacks("fairy", 95, 100, 0, 15, True, "Moon blast")
Psyshock = Attacks("psychic", 80, 100, 0, 10, True, "Psyshock")
Spiritbreak = Attacks("fairy", 75, 100, 0, 15, True, "Spirit Break")
Suckerpunch = Attacks("dark", 70, 100, 1, 5, False, "Sucker Punch")
