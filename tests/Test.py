# File 1 (Test.py)
# This file has information about test cases which you need to test.

# import unittest
# import BowlingGame


# class TestBowlingGame(unittest.TestCase):
#     def setUp(self):
#         self.game = BowlingGame.BowlingGame()

#     def testGutterGame(self):
#         for i in range(0, 20):
#             self.game.rolls(0)
#         assert self.game.score() == 0

#     def testAllOnes(self):
#         self.rollMany(1, 20)
#         assert self.game.score() == 20

#     def testOneSpare(self):
#         self.game.rolls(5)
#         self.game.rolls(5)
#         self.game.rolls(3)
#         self.rollMany(0, 17)
#         assert self.game.score() == 16

#     def testOneStrike(self):
#         self.game.rolls(10)
#         self.game.rolls(4)
#         self.game.rolls(3)
#         self.rollMany(0, 16)
#         assert self.game.score() == 24

#     def testPerfectGame(self):
#         self.rollMany(10, 12)
#         assert self.game.score() == 300

#     def testOneSpare(self):
#         self.rollMany(5, 21)
#         assert self.game.score() == 150

#     def rollMany(self, pins, rolls):
#         for i in range(rolls):
#             self.game.rolls(pins)


# UPDATE
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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
        for i in range(0, 20):
            self.game.roll(0)
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
        Tests if the game initializes correctly with no rolls.
        """
        self.assertEqual(len(self.game.rolls), 0, "Game should start with no rolls")

    def testFrameProgression(self):
        """
        Validates the correct progression between frames.
        The game should have 20 rolls for 10 frames.
        """
        self.rollMany(0, 20)
        self.assertEqual(
            len(self.game.rolls), 20, "Game should have 20 rolls for 10 frames"
        )

    def testStrikeScoring(self):
        """
        Ensures a strike is correctly scored, including the strike bonus.
        """
        self.game.roll(10)  # Strike
        self.game.roll(3)
        self.game.roll(4)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 24, "Score should reflect strike bonus")

    def testSpareScoring(self):
        """
        Tests accurate scoring of spares, including the spare bonus.
        """
        self.game.roll(5)
        self.game.roll(5)  # Spare
        self.game.roll(3)
        self.rollMany(0, 17)
        self.assertEqual(self.game.score(), 16, "Score should include spare bonus")

    def testOpenFrameScoring(self):
        """
        Verifies correct scoring in open frames.
        The score should match the total pins knocked down.
        """
        self.game.roll(3)
        self.game.roll(4)
        self.rollMany(0, 18)
        self.assertEqual(
            self.game.score(), 7, "Score should match total pins knocked down"
        )

    def testFinalFrameRules(self):
        """
        Confirms the rules for the tenth frame, especially for a strike in the final frame.
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
        Tests accurate calculation of a perfect score (300).
        This includes strikes in all frames and bonus rolls.
        """
        self.rollMany(10, 12)  # Strikes in all frames including bonuses
        self.assertEqual(self.game.score(), 300, "Perfect game should score 300")

    def rollMany(self, pins, rolls):
        """
        Helper method to roll the ball 'rolls' times knocking down 'pins' pins each time.
        """
        for i in range(rolls):
            self.game.roll(pins)


if __name__ == "__main__":
    unittest.main()
