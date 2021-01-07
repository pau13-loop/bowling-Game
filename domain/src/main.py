class Bowling():

    def __init__(self, frames):
        self.frames = frames
        self.i = 0
        self.throw_counter = 0
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def strike(self):

        points = 10
        self.throw_counter += 2
        self.i += 1

        # INT - (INT, SPARE)
        if self.throw_counter < 20 and self.frames[self.i] in self.numbers:
            points += int(self.frames[self.i])
            # - INT
            if self.frames[self.i+1] in self.numbers:
                points += int(self.frames[self.i+1])
            # - SPARE
            elif self.frames[self.i+1] == '/':
                points += 10 - int(self.frames[self.i])

        # STRIKE - (INT, STRIKE)
        elif self.throw_counter < 20 and self.frames[self.i] == 'X':
            points += 10
            # - INT
            if self.frames[self.i+1] in self.numbers:
                points += int(self.frames[self.i+1])
            # - STRIKE
            elif self.frames[self.i+1] == 'X':
                points += 10

        return points

    def spare(self):

        points = 0

        if self.frames[self.i - 1] in self.numbers:
            points += 10 - int(self.frames[self.i - 1])
        else:
            points += 10

        self.throw_counter += 1
        self.i += 1

        # bonus score for the spare
        if self.throw_counter < 20:
            if self.frames[self.i] == 'X':
                points += 10
            elif self.frames[self.i] in self.numbers:
                points += int(self.frames[self.i])

        return points

    def integer(self):

        points = int(self.frames[self.i])
        self.i += 1
        self.throw_counter += 1

        return points

    def extra_frames(self):

        points = 0

        while self.i < len(self.frames):
            if self.frames[self.i] in self.numbers:
                points += int(self.frames[self.i])
            elif self.frames[self.i] == 'X':
                points += 10
            elif self.frames[self.i] == '/':
                points += 10 - int(self.frames[self.i - 1])
            self.i += 1

        return points

    def bowling_game(self):

        score = 0

        self.frames = self.frames.replace('-', '0')

        while self.throw_counter < 20:
            if self.frames[self.i] == 'X':
                score += self.strike()
            elif self.frames[self.i] == '/':
                score += self.spare()
            else:
                score += self.integer()
        score += self.extra_frames()

        return score
