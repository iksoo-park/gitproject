class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Singleton class can't be instantiated more than once")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance