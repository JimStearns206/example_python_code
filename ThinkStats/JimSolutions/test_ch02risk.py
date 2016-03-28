from unittest import TestCase

__author__ = 'jimstearns'

import ch02risk
from InstructorUtilities import Pmf

class TestCh02Risk(TestCase):

    def test_ProbEarly_RejectsWrongTypeParm(self):
        floatIsWrongType = 0.0
        errMsgRegex = "^Parameter type must be Pmf, not float.$"
        self.assertRaisesRegex(TypeError, errMsgRegex, ch02risk.ProbEarly, (floatIsWrongType))

    def test_SimpleCase(self):
        simplePmf = Pmf.MakePmfFromList([30,30,40,40,40,38,39,41])
        expEarly = 0.25
        expOnTime = 0.625
        expLate = 0.125
        self.assertEqual(expEarly, ch02risk.ProbEarly(simplePmf))
        self.assertEqual(expOnTime, ch02risk.ProbOnTime(simplePmf))
        self.assertEqual(expLate, ch02risk.ProbLate(simplePmf))