import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('apple')
        self.g3 = Guess('airplain')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')


    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')


    def testDisplayCurrent2(self):
        self.assertEqual(self.g2.displayCurrent(), '_ _ _ _ e ')
        self.g2.guess('a')
        self.assertEqual(self.g2.displayCurrent(), 'a _ _ _ e ')
        self.g2.guess('p')
        self.assertEqual(self.g2.displayCurrent(), 'a p p _ e ')
        self.g2.guess('c')
        self.assertEqual(self.g2.displayCurrent(), 'a p p _ e ')

    def testDisplayGuessed2(self):
        self.assertEqual(self.g2.displayGuessed(), ' e n ')
        self.g2.guess('a')
        self.assertEqual(self.g2.displayGuessed(), ' a e n ')
        self.g2.guess('p')
        self.assertEqual(self.g2.displayGuessed(), ' a e n p ')
        self.g2.guess('c')
        self.assertEqual(self.g2.displayGuessed(), ' a c e n p ')

    def testDisplayCurrent3(self):
        self.assertEqual(self.g3.displayCurrent(), '_ _ _ _ _ _ _ n ')
        self.g3.guess('a')
        self.assertEqual(self.g3.displayCurrent(), 'a _ _ _ _ a _ n ')
        self.g3.guess('p')
        self.assertEqual(self.g3.displayCurrent(), 'a _ _ p _ a _ n ')
        self.g3.guess('c')
        self.assertEqual(self.g3.displayCurrent(), 'a _ _ p _ a _ n ')
        self.g3.guess('i')
        self.assertEqual(self.g3.displayCurrent(), 'a i _ p _ a i n ')
        self.g3.guess('1')
        self.assertEqual(self.g3.displayCurrent(), 'a i _ p _ a i n ')

    def testDisplayGuessed3(self):
        self.assertEqual(self.g3.displayGuessed(), ' e n ')
        self.g3.guess('a')
        self.assertEqual(self.g3.displayGuessed(), ' a e n ')
        self.g3.guess('p')
        self.assertEqual(self.g3.displayGuessed(), ' a e n p ')
        self.g3.guess('c')
        self.assertEqual(self.g3.displayGuessed(), ' a c e n p ')

    def testFinished(self):
        self.assertFalse(self.g2.finished())
        self.g2.guess('a')
        self.assertFalse(self.g2.finished())
        self.g2.guess('p')
        self.assertFalse(self.g2.finished())
        self.g2.guess('l')
        self.assertTrue(self.g2.finished())
        self.assertEqual(self.g2.currentStatus, 'apple')

    def testGuessReturn(self):
        self.assertFalse(self.g2.guess('b'))
        self.assertTrue(self.g2.guess('a'))


if __name__ == '__main__':
    unittest.main()

