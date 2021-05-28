class Guesser():
    def __init__(self):
           """A maneuver in the game. The responsibility of Guesser is to ask and get a guess from the user of what the secret word is.
    
    Stereotype: 
        Information Holder

    Attributes:
        _player1_data (list): answer, hint.
        _player2_data (list): answer, hint.
    """
        self._player1_data = ["----","****"]
        self._player2_data = ["----","****"]

    def get_guess(self,playerturn,player1,player2,player1data,player2data):
         """Gets users' guess.

        """
        
        if playerturn == 1:
            player1data[0] = input("What is your guess? ")
        
        if playerturn == 2:
            player2data[0] = input("What is your guess? ")
    
