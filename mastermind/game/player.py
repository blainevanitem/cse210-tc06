class Player():
     """A person taking part in a game. The responsibility of Player is to keep track of their identity and returns them.
    
    Stereotype: 
        Information Holder

    """

    def get_player_one(self):
        """Returns the player's name

        Args:
            self (Player): an instance of Player.
        """
        return input("Enter a name for player 1: ")
    
    def get_player_two(self):
         """Returns the player's name

        Args:
            self (Player): an instance of Player.
        """
        return input("Enter a name for player 2: ")