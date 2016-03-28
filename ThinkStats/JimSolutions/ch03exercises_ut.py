""" ch03exercises_ut.py

This file contains code created by Jim Stearns for learning with "Think Stats",
by Allen B. Downey, available from greenteapress.com and O'Reilly.

Solutions to exercises are put in the form of a test case.

Use freely, with awareness author is at present a Python novice.
"""

__author__ = 'jimstearns'

from InstructorUtilities import Pmf
from unittest import TestCase

class Ch03Exercises_CumulativeDistributionFunctions(TestCase):
    ####
    # Exercises as unit tests
    ####
    def exercise31_classsizepmf(self):
        Pmf.MakePmfFromList()


    ####
    # Utilities
    ####
    def build_classsize_list(self):
        """ Build the list of class sizes supplied by author Downey. Use mid-point of bucket
            for key value (e.g. for bucket 20-24 students, use 22.
        """
        class_sizes = []