class Sounds:
    def __init__(self):
        self.sounds = {}
        self.load_sounds()

    def load_sounds(self):
        pass

    def play_sound(self, sound):
        self.sounds[sound].play()