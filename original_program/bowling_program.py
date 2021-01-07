def bowling_game(frames):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    frames = str(frames)
    score = 0
    throw_counter = 0
    i = 0
    while throw_counter < 20:
        # integer frame
        if frames[i] in numbers:
            score += int(frames[i])
            throw_counter += 1
            i += 1
        # null frame
        elif frames[i] == '-':
            i += 1
            throw_counter += 1
        # spare frame
        elif frames[i] == '/':
            if frames[i - 1] in numbers:
                score += 10 - int(frames[i - 1])
            else:
                score += 10
            # bonus score for the spare
            if throw_counter + 1 < 20:
                if frames[i + 1] == 'X':
                    score += 10
                elif frames[i + 1] in numbers:
                    score += int(frames[i + 1])
            throw_counter += 1
            i += 1
        # strike frame
        elif frames[i] == 'X':
            score += 10
            throw_counter += 2
            i += 1
            # INT - (INT, SPARE)
            if throw_counter < 20 and frames[i] in numbers:
                score += int(frames[i])
                # - INT
                if frames[i+1] in numbers:
                    score += int(frames[i+1])
                # - SPARE
                elif frames[i+1] == '/':
                    score += 10 - int(frames[i])
            # NULL - (INT, SPARE)
            elif frames[i] == '-':
                # - INT
                if frames[i+1] in numbers:
                    score += int(frames[i+1])
                # - SPARE
                elif frames[i+1] == '/':
                    score += 10
            # STRIKE - (INT, STRIKE)
            elif throw_counter < 20 and frames[i] == 'X':
                score += 10
                # - INT
                if frames[i+1] in numbers:
                    score += int(frames[i+1])
                # - STRIKE
                elif frames[i+1] == 'X':
                    score += 10
    # bonus frames in case we make an spare or strike in our last official frame of the game
    while i < len(frames):
        if frames[i] in numbers:
            score += int(frames[i])
        elif frames[i] == 'X':
            score += 10
        elif frames[i] == '/':
            score += 10 - int(frames[i - 1])
        i += 1
    return score
