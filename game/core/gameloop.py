class Gameloop:
    def __init__(self, game):
        self.game = game

    def run(self):
        while self.game.running:
            self.game.handle_events()
            self.game.update()
            self.game.render()
            self.game.clock.tick(self.game.fps)