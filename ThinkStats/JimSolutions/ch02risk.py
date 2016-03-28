"""Exercise 2-6.
Create a file named risk.py. Write functions named ProbEarly, ProbOnTime, and ProbLate
that take a PMF and compute the fraction of births that fall into each bin.
Hint: write a generalized function that these functions call.
"""

from InstructorUtilities import Pmf

def CheckParmIsTypePmf(parmProvided):
    if not isinstance(parmProvided, Pmf.Pmf):
        actualTypeName = type(parmProvided).__name__
        raise TypeError("Parameter type must be Pmf, not {0}.".format(actualTypeName))

def threeBinAPmf(pmf):
    """Categorize PMF by percentage of values belonging in these three bins:
        < 38 (weeks)
        38 to 40 (weeks)
        > 40 (weeks)
    """
    EARLY_LT_BOUND = 38
    ONTIME_LT_BOUND = 41

    pmf.Normalize()     # So percentages add up to 1.0
    early = ontime = late = 0
    for week, prob in pmf.Items():
        if (week < EARLY_LT_BOUND):
            early += prob
        elif (week < ONTIME_LT_BOUND):
            ontime += prob
        else:
            late += prob

    return early, ontime, late

def ProbEarly(pmf):
    CheckParmIsTypePmf(pmf)
    early, ontime, late = threeBinAPmf(pmf)
    #print(early, ontime, late)
    return early

def ProbOnTime(pmf):
    CheckParmIsTypePmf(pmf)
    early, ontime, late = threeBinAPmf(pmf)
    return ontime

def ProbLate(pmf):
    CheckParmIsTypePmf(pmf)
    early, ontime, late = threeBinAPmf(pmf)
    return late