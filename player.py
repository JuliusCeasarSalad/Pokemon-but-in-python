from Pokemon import Pokemon
class Player:
    def __init__(self, name:str, pokemon:list[Pokemon]) -> None:
        self.name = name
        self.pokemon = pokemon