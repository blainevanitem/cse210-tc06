import random

class Checker():
    def __init__(self):
        self._secret = ""

    def get_secret_number(self):
        self._secret = str(random.randint(1000,9999))

    def get_hint(self,playerturn,player1data,player2data):
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