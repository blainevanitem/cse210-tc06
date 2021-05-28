class Roster():
     """A collection of players. The responsibility of Roster is to keep track of the players.
    
    Stereotype: 
        Information Holder

    Attributes:
        _turn (integer): The index of the current player.
        
    """
    def __init__(self):
        
        self._turn = 0

    def playersturn(self):
         """Determines player's turn.

        Args:
            self (Player): an instance of Player.
        returns:
            1 for player 1
            2 for player 2
        """
        if(self._turn % 2 == 0):
            self._turn +=1
            return 1
        else:
            self._turn +=1
            return 2