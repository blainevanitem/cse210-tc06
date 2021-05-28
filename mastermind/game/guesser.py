class Guesser():
    def __init__(self):
        self._player1_data = ["----","****"]
        self._player2_data = ["----","****"]

    def get_guess(self,playerturn,player1,player2,player1data,player2data):
        if playerturn == 1:
            player1data[0] = input("What is your guess? ")
        
        if playerturn == 2:
            player2data[0] = input("What is your guess? ")
    
