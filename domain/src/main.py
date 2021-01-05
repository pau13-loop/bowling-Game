i = 0
throw_counter = 0
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


class Bowling:

    def __init__(self, frames):
        self.frames = frames

    def strike(self):

        global i
        global throw_counter
        global numbers

        points = 0

        points += 10
        throw_counter += 2
        i += 1
        # INT - (INT, SPARE)
        if throw_counter < 20 and self.frames[i] in numbers:
            points += int(self.frames[i])
            # - INT
            if self.frames[i+1] in numbers:
                points += int(self.frames[i+1])
            # - SPARE
            elif self.frames[i+1] == '/':
                points += 10 - int(self.frames[i])
        # NULL - (INT, SPARE)
        elif self.frames[i] == '-':
            # - INT
            if self.frames[i+1] in numbers:
                points += int(self.frames[i+1])
            # - SPARE
            elif self.frames[i+1] == '/':
                points += 10
        # STRIKE - (INT, STRIKE)
        elif throw_counter < 20 and self.frames[i] == 'X':
            points += 10
            # - INT
            if self.frames[i+1] in numbers:
                points += int(self.frames[i+1])
            # - STRIKE
            elif self.frames[i+1] == 'X':
                points += 10

        return points

    def spare(self):

        global i
        global throw_counter
        global numbers

        points = 0

        if self.frames[i - 1] in numbers:
            points += 10 - int(self.frames[i - 1])
        else:
            points += 10

        throw_counter += 1
        i += 1

        # bonus score for the spare
        if throw_counter < 20:
            if self.frames[i] == 'X':
                points += 10
            elif self.frames[i] in numbers:
                points += int(self.frames[i])

        return points

    def null(self):

        global i
        global throw_counter

        i += 1
        throw_counter += 1

    def integer(self):

        global throw_counter
        global i

        points = int(self.frames[i])
        i += 1
        throw_counter += 1

        return points

    def extra_frames(self):

        global i
        global numbers

        points = 0

        while i < len(self.frames):
            if self.frames[i] in numbers:
                points += int(self.frames[i])
            elif self.frames[i] == 'X':
                points += 10
            elif self.frames[i] == '/':
                points += 10 - int(self.frames[i - 1])
            i += 1

        return points

    def bowling_game(self):

        global i
        global throw_counter
        global numbers

        score = 0

        while throw_counter < 20:
            if self.frames[i] == 'X':
                score += self.strike()
            elif self.frames[i] == '/':
                score += self.spare()
            elif self.frames[i] == '-':
                self.null()
            else:
                score += self.integer()
        score += self.extra_frames()

        return score
