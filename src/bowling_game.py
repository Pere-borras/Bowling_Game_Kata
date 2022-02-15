

class Bowling_game:

    def __init__(self, scorecard=''):

        self.scorecard = scorecard
        self.tries = 2
        self.frame = 1

        self.score = 0
        self.punctuation = 0

        self.iterations = -1

    def bowling(self):

        for roll in self.scorecard:
            self.update_number_iterations()
            self.modify_tries()

            if roll == '-':
                if self.get_tries() <= 0:
                    self.reset()

            elif roll == 'X':
                if self.get_frame() >= 10:
                    self.set_punctuation(10)

                else:
                    self.set_strike()
                    self.reset()

            elif roll == '/':
                if self.get_frame() >= 10:
                    self.set_punctuation(
                        10 - self.get_another_position_scorecard(-1))

                else:
                    self.set_spare()

            elif int(roll) in range(1, 10):
                self.set_punctuation(roll)

            if self.get_tries() <= 0:
                self.reset()

        self.set_score()
        return self.get_score()

    def reset(self):
        self.set_score()
        self.reset_punctuation()
        self.update_frame()
        self.reset_tries()

    def set_spare(self):
        self.set_punctuation(
            10 - self.get_another_position_scorecard(-1) + self.get_another_position_scorecard(1))

    def set_strike(self):
        self.set_punctuation(
            10 + self.get_another_position_scorecard(1) + self.get_another_position_scorecard(2))

    def get_punctuation(self):
        return self.punctuation

    def set_punctuation(self, points):
        self.punctuation += int(points)

    def reset_punctuation(self):
        self.punctuation = 0

    def get_frame(self):
        return self.frame

    def update_frame(self):
        self.frame += 1

    def get_tries(self):
        return self.tries

    def modify_tries(self):
        self.tries -= 1

    def reset_tries(self):
        self.tries = 2

    def get_score(self):
        return self.score

    def set_score(self):
        self.score += self.punctuation

    def get_number_iterations(self):
        return self.iterations

    def update_number_iterations(self):
        self.iterations += 1

    def get_another_position_scorecard(self, pos_modifier=0):
        card_position = self.scorecard[self.get_number_iterations(
        ) + pos_modifier]

        if card_position == 'X':
            card_position = 10

        elif card_position == '-':
            card_position = 0

        elif card_position == '/':
            card_position = 10 - \
                int(self.scorecard[self.get_number_iterations() + 1])

        return int(card_position)


## TEST CASES ##


if __name__ == '__main__':
    scorecard = Bowling_game("12345123451234512345")
    assert 60 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("9-9-9-9-9-9-9-9-9-9-")
    assert 90 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("XXXXXXXXXXXX")
    assert 300 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("-79/12639--9--156-8-")
    assert 68 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("-9--5-9/-7-581-67/8-")
    assert 77 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("--337-7/9-X-57-9-9/7")
    assert 94 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("9-3561368153258-7181")
    assert 82 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("9-3/613/815/-/8-7/8-")
    assert 121 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("X9-9-9-9-9-9-9-9-9-")
    assert 100 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("X9-X9-9-9-9-9-9-9-")
    assert 110 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("9-3/613/815/-/8-7/8/8")
    assert 131 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("XX9-9-9-9-9-9-9-9-")
    assert 120 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("XXX9-9-9-9-9-9-9-")
    assert 141 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("9-3/613/815/-/8-7/8/8")
    assert 131 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("5/5/5/5/5/5/5/5/5/5/5")
    assert 150 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("9-9-9-9-9-9-9-9-9-XXX")
    assert 111 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("8/549-XX5/53639/9/X")
    assert 149 == Bowling_game.bowling(scorecard)

    scorecard = Bowling_game("X5/X5/XX5/--5/X5/")
    assert 175 == Bowling_game.bowling(scorecard)
