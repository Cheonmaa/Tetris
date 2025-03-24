class Score:
    def __init__(self):
        self.score = 0

    def add(self, points):
        self.score += points

    def reset(self):
        self.score = 0

    def get(self):
        return self.score