import random
from CONSTANTS import TYPE_ADVATAGES


def calc_phs_dmg(attacker, defender , movenumber) -> float:
    """Calculates the physical damage, using this formula :
    \n `42 * power * (attack / defence) / 50 + 2) * critical * random_ * stab * typeBonus) / 2`
    """
    #Critical hit (1/24 chance)
    critical = 1.5 if random.choice(f"{'0'*23}1") == "1" else 1
    #Random effect
    random_ = random.randint(85, 100) / 100
    #STAB bonus
    stab = 1.5 if attacker.pokemon.moves[movenumber].type in attacker.pokemon.type1 else 1
    #Type bonus
    typeBonus = calculateTypeBonus(attacker.pokemon, defender.pokemon, movenumber)
    #attack formula
    Formula = round(((42 * attacker.pokemon.moves[movenumber].power * (attacker.pokemon.atk / defender.pokemon.deff) / 50 + 2) * critical * random_ * stab * typeBonus) / 2)
    
    return Formula

def calc_spc_dmg(attacker, defender, movenumber) -> float:
    """Calculates the special damage, using this formula :
    \n `42 * power * (special attack / special defence) / 50 + 2) * critical * random_ * stab * typeBonus) / 2`
    """
    #Critical hit (1/24 chance)
    critical = 1.5 if random.choice(f"{'0'*23}1") == "1" else 1
    #Random effect
    random_ = random.randint(85, 100) / 100
    #STAB bonus
    stab = 1.5 if attacker.pokemon.moves[movenumber].type in attacker.pokemon.type1 else 1
    #Type bonus
    typeBonus = calculateTypeBonus(attacker.pokemon, defender.pokemon, movenumber)
    #special attack formula
    SpeFormula = round(((42 * attacker.pokemon.moves[movenumber].power * (attacker.pokemon.spatk / defender.pokemon.spdef) / 50 + 2) * critical * random_ * stab * typeBonus) / 2)

    return SpeFormula

#Calcuate type bonuses
def calculateTypeBonus(attacker, defender, movenumber) -> int | float:
    "Calcuates the types bonuses between two pokémon. Returns the bonus"
    global label_text
    #Type of attack
    
    attackType = attacker.moves[movenumber].type
    
    #Types of defending pokemon
    defenderTypes = (defender.type1, defender.type2)

    #Type bonus multiplier
    bonus = 1

    #Attack boosts
    for modifier in TYPE_ADVATAGES[attackType]:
        if modifier[0] in defenderTypes: 
            bonus *= modifier[1]
    
    #Return the final boost
    return bonus