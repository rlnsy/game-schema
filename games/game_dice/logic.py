from games.logic_interface import GameLogic

class DiceLogic(GameLogic):

    def default_creator_roles(self):
        return ['Dice_roller']
