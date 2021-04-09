class C32:
    def __init__(self):
        self.condition = 'A'
    def punch(self):
        if self.condition == 'A':
            self.condition = 'B'
            return 0
        elif self.condition == 'B':
            self.condition = 'C'
            return 2
        elif self.condition == 'C':
            self.condition = 'D'
            return 4
        elif self.condition == 'D':
            self.condition = 'F'
            return 7
        elif self.condition == 'E':
            self.condition = 'F'
            return 8
        else:
            RuntimeError
    def hike(self):
        if self.condition == 'A':
            self.condition = 'C'
            return 1
        elif self.condition == 'C':
            return 5
        elif self.condition == 'B':
            self.condition = 'F'
            return 3
        elif self.condition == 'D':
            self.condition = 'E'
            return 6
        else:
            RuntimeError
