
class RandomXY:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def json(self):
        return {'x': self.x,
                'y': self.y}


