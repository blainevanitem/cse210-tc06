from game.console import Console
from game.player import Player
from game.checker import Checker
from game.roster import Roster
from game.guesser import Guesser

class Director():
    def __init__(self):
        self._player1 = ""
        self._player2 = ""
        self._player = Player()
        self._console = Console()
        self._checker = Checker()
        self._roster = Roster()
        self._guesser = Guesser()
        self.keep_playing = True

    def start_game(self):
        self._player1 = self._player.get_player_one()
        self._player2 = self._player.get_player_two()
        self._checker.get_secret_number()
        while(self.keep_playing):
            self._console.display_board(self._player1,self._player2,self._guesser._player1_data,self._guesser._player2_data)
            self.keep_playing = False