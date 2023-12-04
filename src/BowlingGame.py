# File 2 (BowlingGame.py)
# This file has information about Bowling Game for which the description is provided in project assessment.

# class BowlingGame:
#     def __init__(self):
#         self.rolls = []

#     def roll(self, pins):
#         self.rolls.append(pins)

#     def score(self):
#         result = 0
#         rollIndex = 0
#         for frameIndex in range(10):
#             if self.isStrike(rollIndex):
#                 result += self.strikeScore(rollIndex)
#                 rollIndex += 1
#             elif self.isSpare(rollIndex):
#                 result += self.spareScore(rollIndex)
#                 rollIndex += 2
#             else:
#                 result += self.frameScore(rollIndex)
#                 rollIndex += 2
#         return result

#     def isStrike(self, rollIndex):
#         return self.rolls[rollIndex] == 10

#     def isSpare(self, rollIndex):
#         return (
#             rollIndex + 1 < len(self.rolls)
#             and self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10
#         )

#     def strikeScore(self, rollIndex):
#         return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

#     def spareScore(self, rollIndex):
#         return 10 + self.rolls[rollIndex + 2]

#     def frameScore(self, rollIndex):
#         return self.rolls[rollIndex] + self.rolls[rollIndex + 1]


# UPDATE


class BowlingGame:
    def __init__(self):
        """
        Initializes a new instance of the BowlingGame class.
        This method sets up the rolls list, which will keep track of each roll's pins.
        """
        self.rolls = []

    def roll(self, pins):
        """
        Records a roll in the game.

        Args:
            pins (int): The number of pins knocked down in this roll.
        """
        self.rolls.append(pins)

    def score(self):
        """
        Calculates and returns the total score for the game.

        Returns:
            int: The total score for the game.
        """
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
        return result

    def isStrike(self, rollIndex):
        """
        Checks if a roll is a strike.

        Args:
            rollIndex (int): The index of the roll in the rolls list.

        Returns:
            bool: True if the roll is a strike, False otherwise.
        """
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        """
        Checks if a roll is a spare.

        Args:
            rollIndex (int): The index of the roll in the rolls list.

        Returns:
            bool: True if the roll is a spare, False otherwise.
        """
        return (
            rollIndex + 1 < len(self.rolls)
            and self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10
        )

    def strikeScore(self, rollIndex):
        """
        Calculates the score for a strike frame.

        Args:
            rollIndex (int): The index of the strike roll in the rolls list.

        Returns:
            int: The total score for the strike frame.
        """
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        """
        Calculates the score for a spare frame.

        Args:
            rollIndex (int): The index of the first roll in the spare frame in the rolls list.

        Returns:
            int: The total score for the spare frame.
        """
        return 10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        """
        Calculates the score for a regular frame.

        Args:
            rollIndex (int): The index of the first roll in the frame in the rolls list.

        Returns:
            int: The total score for the frame.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
