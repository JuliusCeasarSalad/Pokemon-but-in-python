from CONSTANTS import *            
from pokedex import pokédex            
            
bonus = 1            
            
end = False            
            
defendingpokemon = input("Defending pokemon:\t").lower()            
while end == False:            
    attackType = input("Attacking type:\t").lower()            
    #Types of defending pokemon            
    defenderTypes = pokédex[defendingpokemon]["types"]            
    defenderTypes = [type.lower() for type in defenderTypes]            
    #Type bonus multiplier            
            
    #Attack boosts            
    for modifier in TYPE_ADVATAGES[attackType]:            
        if modifier[0] in defenderTypes:             
            bonus *= modifier[1]            
            
    print(bonus)            
            
    end_choice = input("Do you want to end the program:\t").lower()            
    if end_choice == "yes":            
        break            
    else:            
        pass            
    