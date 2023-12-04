# test_bowling_game.py

# import unittest
# from src.BowlingGame import BowlingGame


# class TestBowlingGame(unittest.TestCase):
#     def setUp(self):
#         self.game = BowlingGame()

#     # ... include all your test methods here ...

#     def rollMany(self, pins, rolls):
#         for i in range(rolls):
#             self.game.roll(pins)


# if __name__ == "__main__":
#     unittest.main()


# UPDATE
import unittest
from src.BowlingGame import BowlingGame


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        """
        Setup method to initialize a BowlingGame instance before each test.
        """
        self.game = BowlingGame()

    def testGutterGame(self):
        """
        Tests a gutter game where all rolls knock down 0 pins.
        The expected score should be 0.
        """
        self.rollMany(0, 20)
        self.assertEqual(self.game.score(), 0, "Gutter game should score 0")

    def testAllOnes(self):
        """
        Tests a game where all rolls knock down 1 pin.
        The expected score should be 20.
        """
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20, "Game of all ones should score 20")

    def testOneSpare(self):
        """
        Tests a game with one spare and subsequent rolls.
        The score should include a spare bonus.
        """
        self.game.roll(5)
        self.game.roll(5)  # Spare
        self.game.roll(3)
        self.rollMany(0, 17)
        self.assertEqual(self.game.score(), 16, "Score should include spare bonus")

    def testOneStrike(self):
        """
        Tests a game with one strike and subsequent rolls.
        The score should include a strike bonus.
        """
        self.game.roll(10)  # Strike
        self.game.roll(3)
        self.game.roll(4)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 24, "Score should include strike bonus")

    def testPerfectGame(self):
        """
        Tests a perfect game where all rolls are strikes.
        The expected score should be 300.
        """
        self.rollMany(10, 12)
        self.assertEqual(self.game.score(), 300, "Perfect game should score 300")

    def testAllSpares(self):
        """
        Tests a game where each frame is a spare.
        The expected score should be 150.
        """
        self.rollMany(5, 21)
        self.assertEqual(self.game.score(), 150, "Game of all spares should score 150")

    def testGameInitialization(self):
        """
        Ensures that the game initializes correctly with an empty list of rolls.
        """
        self.assertEqual(len(self.game.rolls), 0, "Game should start with no rolls")

    def testFrameProgression(self):
        """
        Validates the correct progression of frames in a game.
        A full game with no extra rolls should consist of 20 rolls.
        """
        self.rollMany(0, 20)
        self.assertEqual(
            len(self.game.rolls), 20, "Game should have 20 rolls for 10 frames"
        )

    def testStrikeScoring(self):
        """
        Ensures that a strike is correctly scored, including the strike bonus.
        A strike followed by two rolls should add the pins of the next two rolls as a bonus.
        """
        self.game.roll(10)  # Strike
        self.game.roll(3)
        self.game.roll(4)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 24, "Score should reflect strike bonus")

    def testSpareScoring(self):
        """
        Tests accurate scoring of spares, including the spare bonus.
        A spare followed by a roll should add the pins of the next roll as a bonus.
        """
        self.game.roll(5)
        self.game.roll(5)  # Spare
        self.game.roll(3)
        self.rollMany(0, 17)
        self.assertEqual(self.game.score(), 16, "Score should include spare bonus")

    def testOpenFrameScoring(self):
        """
        Verifies correct scoring in open frames.
        The score should match the total pins knocked down in two rolls.
        """
        self.game.roll(3)
        self.game.roll(4)
        self.rollMany(0, 18)
        self.assertEqual(
            self.game.score(), 7, "Score should match total pins knocked down"
        )

    def testFinalFrameRules(self):
        """
        Confirms the rules for the tenth frame, especially in the case of a strike.
        The final frame should handle extra rolls for a strike or a spare.
        """
        self.rollMany(0, 18)
        self.game.roll(10)  # Strike in final frame
        self.game.roll(10)  # Bonus roll
        self.game.roll(10)  # Bonus roll
        self.assertEqual(
            self.game.score(), 30, "Final frame should handle strike with extra rolls"
        )

    def testMaximumScore(self):
        """
        Tests the accurate calculation of a perfect score.
        A perfect game consists of strikes in all frames, including bonuses, resulting in a score of 300.
        """
        self.rollMany(10, 12)  # Strikes in all frames including bonuses
        self.assertEqual(self.game.score(), 300, "Perfect game should score 300")

    def rollMany(self, pins, rolls):
        """
        Helper method to roll the ball a specified number of times.

        Args:
            pins (int): The number of pins knocked down in each roll.
            rolls (int): The number of times to roll.
        """
        for i in range(rolls):
            self.game.roll(pins)


if __name__ == "__main__":
    unittest.main()
