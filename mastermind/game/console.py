class Console():
     """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """
  
    def display_board(self,player1,player2,player1data,player2data):
         """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            player1 (string): player 1 name
            player2 (string): player 2 name
            player1data (list): guess, hint
            player2data (list): guess, hint
        """
        print("--------------------")
        print("Player " + player1 + ": " + player1data[0] + ", " +player1data[1])
        print("Player " + player2 + ": " + player2data[0] + ", " +player2data[1])
        print("--------------------")

    def display_turn(self,playersturn,player1,player2):
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            playersturn(int): whose turn it is
            player1 (string): player 1 name
            player2 (string): player 2 name
          
        """
        if playersturn == 1:
            print(player1 + " Turn:")
        else:
            print(player2 + " Turn:")

    def final_winner(self,keep_playing,player1data,player2data,player1,player2):
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            keep_playing(Bool): True or False
            player1data (list): guess, hint
            player2data (list): guess, hint
            player1 (string): player 1 name
            player2 (string): player 2 name
        """
        if player1data[1] == "xxxx":
            print("\n" + player1 + " wins!")
            return False

        elif player2data[1] == "xxxx":
            print("\n" + player2 + " wins!")
            return False

        else:
            return True
        
        