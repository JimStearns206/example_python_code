__author__ = 'jimstearns'

# For Exercise 2-3

from InstructorUtilities import Pmf
from operator import itemgetter     # For AllModes sorting.

class HistWithMode(Pmf.Hist):
    """ Add method Mode to class Hist """


    def Extend(self, listOfValues):
        """ Helper method to create test cases """
        [self.Incr(x) for x in listOfValues]

    def Mode(self):
        """ mode is a non-negative integer (empty histogram will return mode of 0)
        List of non-negative integers is returned.
        List of one item if unimodal.
        If multi-mode (multiple indexes have same highest value),
            all values are returned as list.
        """

        idxsWithMaxValue = []
        maxValue = -1
        for k, v in self.Items():
            if (v < maxValue):
                continue
            if (v > maxValue):
                idxsWithMaxValue.clear()
                maxValue = v

            idxsWithMaxValue.append(k)

        return(idxsWithMaxValue)

    def AllModes(self):
        """ Return a list of value-frequency pairs in descending order of frequency.
            Pass second field (value, not key) as field upon which to sort.
        """
        return(sorted(self.Items(),key=itemgetter(1), reverse=True))

