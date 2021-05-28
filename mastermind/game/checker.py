import random

class Checker():
    """The responsibility of Checker is to compare secret word to answer and replace x means a correct number in a correct position. 
    An o means a correct number in an incorrect position. An * means an incorrect number .
    
    Stereotype: 
        Information  

    Attributes:
        _secret (string): The number to guess.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Checker): an instance of Checker.
        """
        self._secret = ""

    def get_secret_number(self):
        """Gets the a random number from 1000 and 9999 by calling it from random .
        
        Args:
            self (Checker): An instance of Checker.
        
        """
        self._secret = str(random.randint(1000,9999))

    def get_hint(self,playerturn,player1data,player2data):
        """Compares secret to guess.
        
        Args:
            self (checker): instance of checker
            playerturn(intenger): whose turn it is
            player1data(list): guess, hint
            player2data(list): guess, hint
        
       
        """
        if playerturn == 1:
            player1data[1] = ""
            for index in range(len(player1data[0])):
                if self._secret[index] == player1data[0][index]:
                    player1data[1] += "x"
                elif player1data[0][index] in self._secret:
                    player1data[1] += "o"
                else:
                    player1data[1] += "*"

        
        if playerturn == 2:
            player2data[1] = ""
            for index in range(len(player2data[0])):
                if self._secret[index] == player2data[0][index]:
                    player2data[1] += "x"
                elif player2data[0][index] in self._secret:
                    player2data[1] += "o"
                else:
                    player2data[1] += "*"