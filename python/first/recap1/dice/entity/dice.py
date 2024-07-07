class Dice:

    def __init__(self):
        self.__playerId = None
        self.__diceNumber = 0

    def setDiceNumber(self, number):
        self.__diceNumber = number

    def setPlayerId(self, playerId):
        self.__playerId = playerId

    def getDiceNumber(self):
        return self.__diceNumber

    def getPlayerId(self):
        return self.__playerId

