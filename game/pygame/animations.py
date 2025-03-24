class Animations:
    def __init__(self):
        self.animations = {}

    def add(self, name, animation):
        self.animations[name] = animation

    def get(self, name):
        return self.animations[name]

    def play(self, name, x, y):
        self.animations[name].play(x, y)

    def stop(self, name):
        self.animations[name].stop()

    def stop_all(self):
        for animation in self.animations.values():
            animation.stop()

    def update(self):
        for animation in self.animations.values():
            animation.update()