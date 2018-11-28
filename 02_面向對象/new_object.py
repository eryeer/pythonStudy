class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        print("create obj, assign area")
        return super().__new__(cls)

    def __init__(self):
        print("palyer init")


player = MusicPlayer()
print(player)