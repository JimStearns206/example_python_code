from unittest import TestCase
import unittest

__author__ = 'jimstearns'


import PmfExtensions

class TestPmfExtensions(TestCase):
    """ Tests of Jim extensions to instructor's classes in Pmf.py. Includes Hist.
    """

    # Python unit test methods must start with "test". How quaint - haven't had to do this in over 10 years.
    # Or is this historical fallback, replaced by use of Python attribute?
    def test_UnimodeWorks(self):
        h = PmfExtensions.HistWithMode()
        h.Incr(1)
        h.Incr(2)
        h.Incr(3)
        h.Incr(2)
        print("Most frequent value is {0}".format(h.Mode()))
        modeList = h.Mode()
        self.assertTrue(len(modeList) == 1)
        self.assertTrue(modeList[0] == 2)

    def test_MultiModeReturns(self):
        h = PmfExtensions.HistWithMode()
        h.Extend([1,2,2,2,3,4,4,4,5])
        print("Most frequent valued are {0}".format(h.Mode()))
        modeList = h.Mode()
        self.assertTrue(len(modeList) == 2)
        self.assertTrue(modeList[0] == 2)
        self.assertTrue(modeList[1] == 4)

    def test_AllModes(self):
        expectedAllModesList = [(88, 8), (77, 7), (66, 6), (55, 5), (44, 4), (33, 3), (22, 2), (11, 1)]

        h = PmfExtensions.HistWithMode()
        h.Extend([11,22,22,33,33,33,44,44,44,44,55,55,55,55,55,66,66,66,66,66,66,77,77,77,77,77,77,77,88,88,88,88,88,88,88,88])
        print(h.AllModes())

        self.assertEqual(expectedAllModesList, h.AllModes())

if __name__ == '__main__':
    unittest.main()