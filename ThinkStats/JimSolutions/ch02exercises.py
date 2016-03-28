"""This file contains code created by Jim Stearns for learning with "Think Stats",
by Allen B. Downey, available from greenteapress.com and O'Reilly

Use freely, with awareness author is at present a Python novice.
"""
__author__ = 'jimstearns'

from InstructorUtilities import survey
from InstructorUtilities import thinkstats as thinkStatsUtilities  # utilities
from operator import itemgetter # Used to pass keys to sorted
import matplotlib.pyplot as pyplot
# KISS: Use Downey's myplot module
from InstructorUtilities import myplot
from InstructorUtilities import Pmf
# ch02risk.py and test_ch02risk.py implemented and lightly unit-tested
from JimSolutions import ch02risk
from unittest import TestCase
import unittest
import os   # For getcwd() et al.

""" Exercise 2-1: using author-provided utilities for computing mean and variance,
write a function Pumpkin() to compute mean, variance, and standard deviation
of the set of pumpkin weights given in the book
"""

pumpkinWeights = [1, 1, 1, 3, 3, 591]
print("Pumpkin weights: {0}.".format(pumpkinWeights))
mu, var = thinkStatsUtilities.MeanVar(pumpkinWeights)

stdDev=var**0.5
print("Pumpkin mean={0:.2f}, variance={1:.2f}, stdDev={2:.2f}.".format(mu, var, stdDev))

# Exercise 2-2.
# Reusing code from survey.py and first.py, compute the standard deviation of gestation time
# for first babies and others. Does it look like the spread is the same for the two groups?
# How big is the difference in the means compared to these standard deviations?
# What does this comparison suggest about the statistical significance of the difference?

# Two alternatives:
# 1. Create two lists of gestation weeks, one for first babies and one for other.
#     Pass each into MeanVar
#     Downside: some big lists.
# 2.  Do two passes thru the pregnancies
#     Pass 1: compute mean.
#     Pass 2: compute difference from mean, squared
#     Then divide by n.
# #2 will take less space, but #1 is easier to program. #2, for a small dataset.



table = survey.Pregnancies()
table.ReadRecords(data_dir="../NSFG")   # I put NSFG data in a peer directory.
print('Number of pregnancies', len(table.records))

firstBabyGestations = []
nonFirstBabyGestations = []
nLiveBirths = 0

for pregrecord in table.records:
    if (pregrecord.outcome == 1):   # live birth
        nLiveBirths += 1
        if (pregrecord.birthord == 1):
            firstBabyGestations.append(pregrecord.prglength)
        else:
            nonFirstBabyGestations.append(pregrecord.prglength)

print('Number of live births', nLiveBirths)
firstBabyMean, firstBabyVar = thinkStatsUtilities.MeanVar(firstBabyGestations)
nonFirstBabyMean, nonFirstBabyVar = thinkStatsUtilities.MeanVar(nonFirstBabyGestations)

print("Std dev for {0} first baby gestations = {1:.2f} (Mean={2:.2f})".format(
    len(firstBabyGestations), firstBabyVar**0.5, firstBabyMean))

print("Std dev for {0} non-first baby gestations = {1:.2f} (Mean={2:.2f})".format(
    len(nonFirstBabyGestations), nonFirstBabyVar**0.5, nonFirstBabyMean))

# How big is the difference in the means compared to these standard deviations?
# Difference in means: 0.08. Difference in std devs: 0.17.
# Difference in mean is less than half the difference in a standard deviation.
#
# What does this comparison suggest about the statistical significance of the difference?
# In the noise?

# Exercise 2-3A.
# The mode of a distribution is the most frequent value (see http://wikipedia.org/wiki/ Mode_(statistics)).
# Write a function called Mode that takes a Hist object and returns the most frequent value.

# Considered multi-mode - more than one index has the maximum value.
# Implemented as a class method - superclassed Hist.

# See JimUtilities/PmfExtensions.py and unit tests in same directory.

# Exercise 2-3B.
# As a more challenging version, write a function called AllModes that takes a Hist object and
# returns a list of value-frequency pairs in descending order of frequency.
# Hint: the operator module provides a function called itemgetter which you can pass as a key to sorted.

### See JimUtilities/PmfExtensions.py and unit test in same directory.

def AllModes(self):
        """ Return a list of value-frequency pairs in descending order of frequency.
            Pass second field (value, not key) as field upon which to sort.
        """
        return sorted(self.Items(),key=itemgetter(1), reverse=True)

# Reproduce histogram plot on page 15 of first babies vs others.

# Use lists of firstBabyGestations and nonFirstBabyGestations created above.

# Kiss: two separate histograms, at first pass.

histFirst = Pmf.MakeHistFromList(firstBabyGestations, "First Babies")
histNonFirst = Pmf.MakeHistFromList(nonFirstBabyGestations, "Non-First Babies")

def kludgePlotHist(hist):
    """Excerpted from Downey's descriptive.py.Hists()
    """

    width = 0.4
    option_list = [
        dict(color='0.9'),
        dict(color='blue')
    ]

    pyplot.clf()

    vals, freqs = hist.Render()
    pyplot.bar(vals, freqs, label=hist.name, width=width, **option_list[0])
    pyplot.show()
    print("kludgePlotHist called for {0}".format(hist.name))

#kludgePlotHist(histFirst)

myplot.Hist(histFirst)
#myplot.show()       # Was not seeing anything until duh, I found this.

# Exercise 2-6.
# Create a file named risk.py. Write functions named ProbEarly, ProbOnTime, and ProbLate
# that take a PMF and compute the fraction of births that fall into each bin.
# Hint: write a generalized function that these functions call.
#
# Make three PMFs, one for first babies, one for others, and one for all live births.
# For each PMF, compute the probability of being born early, on time, or late.
# One way to summarize data like this is with relative risk, which is a ratio of two probabilities.
# For example, the probability that a first baby is born early is 18.2%. For other babies it is 16.8%,
# so the relative risk is 1.08. That means that first babies are about 8% more likely to be early.
# Write code to confirm that result, then compute the relative risks of being born on time and being late.
#
# You can download a solution from http://thinkstats.com/risk.py.
#

print("Comparing first births to non-first births, calculating relative risk of ")
print("being born early, born on time, and born late.")

firstPmf = Pmf.MakePmfFromList(firstBabyGestations, name="First")
nonFirstPmf = Pmf.MakePmfFromList(nonFirstBabyGestations, name="Non-First")
livePmf = firstPmf.Copy(firstPmf)
livePmf.name = "Live"
[livePmf.Incr(x) for x in nonFirstPmf.Values()]

print("Buckets: first={0}, non-first={1}, live={2}.".format(
    len(firstPmf.Values()), len(nonFirstPmf.Values()), len(livePmf.Values())))

def Print3Probs(pmf):

    print("Early/on-time/late probabilities: {1:.3f}, {2:.3f}, {3:.3f} for PMF {0}".format(
        pmf.name, ch02risk.ProbEarly(pmf), ch02risk.ProbOnTime(pmf), ch02risk.ProbLate(pmf))
    )
# Yes, I'm sure there's some terse, elegant way to do this in Python. Until I learn it ...
Print3Probs(firstPmf)
Print3Probs(nonFirstPmf)
Print3Probs(livePmf)

print("Relative risk of being born early (first/non-first): {0:.2f}".format(
    ch02risk.ProbEarly(firstPmf)/ch02risk.ProbEarly(nonFirstPmf)
))

print("Relative risk of being born on-time (first/non-first): {0:.2f}".format(
    ch02risk.ProbOnTime(firstPmf)/ch02risk.ProbOnTime(nonFirstPmf)
))

print("Relative risk of being born late (first/non-first): {0:.2f}".format(
    ch02risk.ProbLate(firstPmf)/ch02risk.ProbLate(nonFirstPmf)
))

# Let's do the balance of the chapter 2 exercises as unit tests

class TestCh02ConditionalProbability(TestCase):
    """
    Conditional Probability
    Imagine that someone you know is pregnant, and it is the beginning of Week 39.
    What is the chance that the baby will be born in the next week?
    How much does the answer change if it’s a first baby?

    We can answer these questions by computing a conditional probability,
    which is (ahem!) a probability that depends on a condition.
    In this case, the condition is that we know the baby didn’t arrive during Weeks 0–38.

    Here’s one way to do it:
    1. Given a PMF, generate a fake cohort of 1,000 pregnancies. For each number of
    weeks, x, the number of pregnancies with duration x is 1,000 PMF(x).
    2. Remove from the cohort all pregnancies with length less than 39.
    3. Compute the PMF of the remaining durations; the result is the conditional PMF.
    4. Evaluate the conditional PMF at x = 39 weeks.
    This algorithm is conceptually clear, but not very efficient.

    A simple alternative is to remove from the distribution the values less than 39 and then re-normalize.

    Choice: the second (simple) alternative.
    """

    ###############
    #### Tests ####
    ###############
    def test_1and1is2(self):
        self.assertEqual(2, 1+1)

    def test_conditionalProbabilityWeek39(self):
        """Exercise 2-7A.
        Write a function that implements either of these algorithms and computes the probability
        that a baby will be born during Week 39, given that it was not born prior to Week 39.
        """
        # Make sure that the livePmf PMF has been computed and is available.
        #print("Length of livePmf is {0} buckets".format(len(livePmf.Values())))
        self.assertEqual(37, len(livePmf.Values()), "Expected value of livePmf is 37 buckets.")
        # And it's normalized.
        self.assertAlmostEqual(1.0, livePmf.Total(), places=4, msg="Live birth PMF should have been normalized.")

        # Make a copy of the PMF, from which births before week 39 will be removed below.
        livePmf39Plus = livePmf.Copy(name="Live Births after 38 weeks")
        livePmf39Plus.Print()

        upperBound = 39  # U/M: weeks. Exclusive (Week 39 is not removed)
        expectedCumulativeProbLessThan39 = 0.7044
        actualProbLessThan39 = self.cumulativeProbability(livePmf39Plus, upperBound)
        self.assertAlmostEqual(expectedCumulativeProbLessThan39, actualProbLessThan39, places=4)

        # No items removed yet, so total probability should still equal 1.
        self.assertAlmostEqual(1.0, livePmf39Plus.Total(), places=4, msg="No items removed, so prob totals 1")

        # Now remove, in place.
        expectedRemainingProbability = 1 - expectedCumulativeProbLessThan39
        self.removeValuesUpTo(livePmf39Plus, upperBound)
        self.assertAlmostEqual(expectedRemainingProbability, livePmf39Plus.Total(), places=4)

        # Re-normalize and check probability total is 1 again.
        livePmf39Plus.Normalize()
        self.assertAlmostEqual(1.0, livePmf39Plus.Total(), places=4,
                               msg="Re-norm'd after items removed, so prob totals 1")
        print("Buckets for Week 39+:")
        livePmf39Plus.Print()

        expectedWeek39Probability = 0.1516
        self.assertAlmostEqual(expectedWeek39Probability, livePmf39Plus.Prob(39), places=4)

    def test_generalizedConditionalProbability(self):
        """ Baby-step: generalize computing a single week's conditional probability:
            Probability of being born in week X given not born before X.
        """
        # First check the case above, using the generalized function
        expectedWeek39Probability = 0.1516
        week39 = 39
        self.assertAlmostEqual(expectedWeek39Probability, self.conditionalProbability(livePmf, week39), places=4)

    def test_HistsWithOffset(self):
        """ Exercise utility method.
        """

        myplot.Clf()

        # Conditional probabilities by gestation week - first born
        rangeofweeks = range(35,46)
        dictOfCondProbsFirst = self.conditionalProbabilities(firstPmf, rangeofweeks)
        histOfCondProbsFirst = Pmf.MakeHistFromDict(dictOfCondProbsFirst)
        histOptions = {}
        histOptions['color'] = '0.9'
        myplot.Hist(histOfCondProbsFirst, **histOptions)

        # for now, method only accepts two hists.
        hist1 = Pmf.MakeHistFromList([1,2,2,3,3,3,4,4,5], name="hist1")
        hist2 = Pmf.MakeHistFromList([2,3,3,4,4,4,5,5,5,5,6], name="hist2")

        # One entry in list
        with self.assertRaises(TypeError):
            self.histsWithOffset([hist1])

        # And every entry must be of type Pmf.hist
        with self.assertRaises(TypeError):
            self.histsWithOffset([hist1, 2])

        overallOptions = {
            'xlabel':'X-Axis Label',
            'ylabel':'Y-Axis Label',
            'legend':True
        }
        # Now plot two PMFs to PDF file and visually inspect result
        self.histsWithOffset([hist1, hist2], overallOptions)
        self.plotToPdfAndOpen("testing123")


    def test_conditionalProbabilities(self):
        """ Exercise 2-7B
            Generalize the function to compute the probability that a baby will be born during Week x,
            given that it was not born prior to Week x, for all x.
            Plot this value as a function of x for first babies and others.

        """
        # Use range from 35 to 45 weeks inclusive.
        # Choice of this particular range is not intuitively obvious:
        # My first implementation covered the entire range of data,
        # and the differences between first-born and others is blurred
        # by both values ramping to 1.0 at Week 50.
        # No, I'm using this range first because that's what the author used, and
        # secondly because it covers the range of interest both before and after
        # the mode of 39 weeks.
        weeks = range(35,46)

        myplot.Clf()

        # Plot first and non-first histograms on same axis, with different color.
        # Requires two calls to Hist (Hists() won't work).

        # Conditional probabilities by gestation week - first born
        dictOfCondProbsFirst = self.conditionalProbabilities(firstPmf, weeks)
        histOfCondProbsFirst = Pmf.MakeHistFromDict(dictOfCondProbsFirst, name="First-Born")

        # Conditional probabilities by gestation week - not first born
        dictOfCondProbsNonFirst = self.conditionalProbabilities(nonFirstPmf, weeks)
        histOfCondProbsNonFirst = Pmf.MakeHistFromDict(dictOfCondProbsNonFirst, name="Second+ Born")

        overallOptions = {
            'xlabel':'Gestation Week',
            'ylabel':r'Prob{x $=$ weeks | x $\geq$ weeks}',  # The 'r' is for raw, I'm told
            'title':'Conditional Probability',
            'legend':True,
            'loc':0     # Upper left, I think
        }

        #self.histsWithOffset([histOfCondProbsFirst, histOfCondProbsNonFirst], overallOptions)
        self.plot_hists_as_lines([histOfCondProbsFirst, histOfCondProbsNonFirst], overallOptions)

        # Save plot to file as PDF so that it can be displayed while allowing unit test to complete.
        plotFileName = "Ch02Ex2-7_ConditionalProbabilities"
        self.plotToPdfAndOpen(plotFileName)

    def test_Exercise_2_8(self):
        """ Based on the results from the previous exercises, suppose you were asked to summarize
            what you learned about whether first babies arrive late.
            Which summary statistics would you use if you wanted to get a story on the evening news?
            Which ones would you use if you wanted to reassure an anxious patient?

            Finally, imagine that you are Cecil Adams, author of The Straight Dope (http://straightdope.com),
            and your job is to answer the question, “Do first babies arrive late?”
            Write a paragraph that uses the results in this chapter to answer the question clearly, precisely,
            and accurately.

        Summary for evening news: Difference in percentage, by week. Highlights the difference, that
        first borns lag.

        Summary for anxious patient: conditional probability line graph.
        """

    ###################
    #### Utilities ####
    ###################

    def cumulativeProbability(self, pmf, valBound):
        """Given a probability mass function object,
            Calculate the cumulative probability for values up to but excluding valBound.
        """
        if not isinstance(pmf, Pmf.Pmf):
            raise TypeError("First parameter must be of type Pmf.")

        cumFreq = 0.0

        for val, freq in pmf.Items():
            if val < valBound:
                cumFreq += freq

        return cumFreq

    def removeValuesUpTo(self, pmf, valBound):
        """ Remove frequencies for values less than valBound
        """
        if not isinstance(pmf, Pmf.Pmf):
            raise TypeError("First parameter must be of type Pmf.")

        itemsToRemove = []

        for val, freq in pmf.Items():
            if val < valBound:
                itemsToRemove.append(val)   # Can't remove during iteration. Gather and remove after.

        for val in itemsToRemove:
                pmf.Remove(val)

    def conditionalProbability(self, pmf, val):
        """ What is the probability of a baby being born in week "val" of gestation,
            given that the baby has not already been born in prior weeks?

            Parameter pmf is NOT modified - operations in this method are performed on a copy.
        """
        if not isinstance(pmf, Pmf.Pmf):
            raise TypeError("First parameter must be of type Pmf.")

        # Not sure this all works if bucket parameter isn't an integer.
        # So require it so one can be subtracted for determining prior buckets to remove.
        if not isinstance(val, int):
            raise TypeError("Second parameter must be of type integer")

        # Don't modify PMF passed in. Make a copy
        condPmf = pmf.Copy(name="conditionalPmf")
        self.removeValuesUpTo(condPmf, val)
        condPmf.Normalize()

        return condPmf.Prob(val, 0)

    def conditionalProbabilities(self, pmf, rangeofweeks):
        """ For all values in the PMF, what is the probability of that value
            given that the probability for all values less than that value is zero -
            the event hasn't occurred in earlier (lower) values.

            Applying this general statement to the gestation question:
            What is the probability of being born in gestation week x
            given that the birth has not already occurred in earlier gestation weeks?
        """
        if not isinstance(pmf, Pmf.Pmf):
            raise TypeError("First parameter must be of type Pmf.")

        # Use a copy of the pmf parameter - leave pmf unchanged.
        pmfCopy = pmf.Copy(name="pmfCopy")

        # Get a list of keys (gestation week) sorted in ascending order
        #sortedKeys = list(pmfCopy.GetDict().keys())
        #print("Keys, unsorted:", sortedKeys)
        #sortedKeys.sort()
        #print("Keys, sorted:", sortedKeys)

        condProbs = {}

        # For each gestation week in the supplied range:
        #   Remove probabilities for prior weeks, if any, and renormalize.
        #   Save that week's recomputed probability as its conditional probability in a dictionary
        #       Use a dictionary rather than a list because first gestation week may be greater than zero.

        for i in rangeofweeks: # range(len(sortedKeys)):

            condProbs[i] = self.conditionalProbability(pmfCopy, i)
            print("condProb({0}) = {1}".format(i, condProbs[i]))

        # Return dictionary of (gestationWeek, conditional probability)
        return condProbs

    def plot_hists_as_lines(self, hists, overallOptionsList):
        """Plot two (sorry, only two for now) histograms on same axis
            using different colors (sorry, fixed for now).

            hists: a list of hist
            overallOptionsList: options to apply to entire plot, not an individual hist:
                title, xlabel, ylabel, legend, loc
        """
        # Parameter check: only two entries in hists.
        if (len(hists) != 2):
            raise TypeError()

        # Parameter check: all entries must be of type InstructorUtilities.Pmf.Hist
        for hist in hists:
            print("Type of entry: {0}".format(type(hist)))
            if not isinstance(hist, Pmf.Hist):
                print("Nope, {0} is not an instance of {1}".format(type(hist), type(Pmf.Hist)))
                raise TypeError("At least one entry in hists is not of Type Pmf.Hist")


        option_list = [
            dict(color='0.9'),
            dict(color='blue')
            ]

        pyplot.clf()
        for i, hist in enumerate(hists):
            xs, fs = hist.Render()
            #xs = self.Shift(xs, shifts[i])
            #pyplot.bar(xs, fs, label=hist.name, width=width, **option_list[i])
            pyplot.plot(xs, fs, label=hist.name)
            print(hist.name, fs)

        myplot.Config(**overallOptionsList)

    def histsWithOffset(self, hists, overallOptionsList):
        """Plot two (sorry, only two for now) histograms on same axis
            using different colors (sorry, fixed for now).

            hists: a list of hist
            overallOptionsList: options to apply to entire plot, not an individual hist:
                title, xlabel, ylabel, legend, loc
        """
        # Parameter check: only two entries in hists.
        if (len(hists) != 2):
            raise TypeError()

        # Parameter check: all entries must be of type InstructorUtilities.Pmf.Hist
        for hist in hists:
            print("Type of entry: {0}".format(type(hist)))
            if not isinstance(hist, Pmf.Hist):
                print("Nope, {0} is not an instance of {1}".format(type(hist), type(Pmf.Hist)))
                raise TypeError("At least one entry in hists is not of Type Pmf.Hist")

        width = 0.4
        shifts = [-width, 0.0]

        option_list = [
            dict(color='0.9'),
            dict(color='blue')
            ]

        pyplot.clf()
        for i, hist in enumerate(hists):
            xs, fs = hist.Render()
            xs = self.Shift(xs, shifts[i])
            pyplot.bar(xs, fs, label=hist.name, width=width, **option_list[i])

        myplot.Config(**overallOptionsList)

    def Shift(self, xs, shift):
        """Instructor-Provided: Adds a constant to a sequence of values.

        Args:
          xs: sequence of values

          shift: value to add

        Returns:
          sequence of numbers
        """
        return [x+shift for x in xs]

    def plotToPdfAndOpen(self, fileName):
        """ Save plot to file as PDF so that it can be displayed while allowing unit test to complete.
        """

        plotFileSuffix = "pdf"
        myplot.SaveFormat(fileName, plotFileSuffix)

        # TODO: If fileName already ends in .pdf, don't add it again
        # TODO: Determine if absolute filepath is needed by open
        fileSpec = "'" + os.getcwd() + "/" + fileName + "." + plotFileSuffix + "\'"

        print(fileSpec)
        os.system("open " + fileSpec)


        # (This process-based timeout may work if called in main program,
        #   but when called from function, I get unix exception:
        #   "Exception Type:  EXC_BAD_ACCESS (SIGSEGV)"
        #   "*** multi-threaded process forked ***"
        #   "crashed on child side of fork pre-exec"

        # def showMyPlot(self):
        #     myplot.Show()
        #
        # def showMyPlotFor10Seconds(self):
        #     import multiprocessing
        #     import time
        #
        #     plotShowProcess = multiprocessing.Process(target=myplot.Show)
        #     plotShowProcess.start()
        #
        #     plotShowProcess.join(10)
        #
        #     if (plotShowProcess.is_alive()):
        #         plotShowProcess.terminate()
        #         plotShowProcess.join()  # Wait for termination

        # Let's try signal. Assumptions (true, here):
        #   1. On unix system (Mac OS X)
        #   2. Running on main thread.

        ## Alas, this almost but not quite worked:
        ## Need to move mouse to make this the active process.
        # def timeout(self, signum, frame):
        #     print("Alarm detected ... closing plot.")
        #     myplot.Clf()
        #     myplot.Close()
        #
        # def showMyPlotForNSeconds(self, nSeconds):
        #     import signal
        #     signal.signal(signal.SIGALRM, self.timeout)
        #
        #     signal.alarm(nSeconds)
        #
        #     #print("Matplotlib.is_interactive={0}", pyplot.isinteractive())
        #     print("Showing plot for at least {0} seconds".format(nSeconds))
        #     myplot.Show()

        # Let's try a simplified thread-based timeout:
        # Show the plot in the spawned thread, but don't try terminate or join:
        # Just wait N seconds in the spawning thread and close the plot.

        ## Nope: NSInternalInconsistencyException
        ## "is only safe to invoke on the main thread."
        ## Learning: I can't call UI rendering code from other than the main thread.
        ## Sounds like .NET!

        # def showMyPlot():
        #     myplot.Show()
        #
        # def showMyPlotForNSeconds(self):
        #     import threading
        #     import time
        #
        #     nSeconds = 5
        #
        #     plotShowThread = threading.Thread(target=showMyPlot)
        #     plotShowThread.start()
        #
        #     time.sleep(nSeconds)
        #     myplot.Close()

        # How about rendering on the main thread, plotting to a PDF file, and showing PDF in a separate window?

print("Running unit tests ...")
#
# Why does this unittest.main() as "Unittests in ch02exercises" cause this error:
# "AttributeError: 'module' object has no attribute 'ch02exercises'"?
# While running unittest.main() as "ch02exercises.py" doesn't?
unittest.main()