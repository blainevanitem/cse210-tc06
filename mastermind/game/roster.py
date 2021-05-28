class Roster():
    def __init__(self):
        self._turn = 0

    def playersturn(self):
        if(self._turn % 2 == 0):
            self._turn +=1
            return 1
        else:
            self._turn +=1
            return 2