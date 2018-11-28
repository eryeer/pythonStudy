class Game(object):
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("help doc : let zombies enter")

    @classmethod
    def show_top_score(cls):
        print("history score %s" % cls.top_score)

    def start_game(self):
        print("%s game start " % self.player_name)


Game.show_help()
Game.show_top_score()
game = Game("xiaoming")
game.start_game()
