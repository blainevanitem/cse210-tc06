class Console():
    def __init__(self):
        pass

    def display_board(self,player1,player2,player1data,player2data):
        print("--------------------")
        print("Player " + player1 + ": " + player1data[0] + ", " +player1data[1])
        print("Player " + player2 + ": " + player2data[0] + ", " +player2data[1])
        print("--------------------")

    def display_turn(self,playersturn,player1,player2):
        if playersturn == 1:
            print(player1 + " Turn:")
        else:
            print(player2 + " Turn:")

    def final_winner(self,keep_playing,player1data,player2data,player1,player2):
        if player1data[1] == "xxxx":
            print("\n" + player1 + " wins!")
            return False

        elif player2data[1] == "xxxx":
            print("\n" + player2 + " wins!")
            return False

        else:
            return True
        
        