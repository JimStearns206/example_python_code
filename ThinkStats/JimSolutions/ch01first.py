# O'Reilly "Think Stats"  Exercise 1-3
#

__author__ = 'jimstearns'

from InstructorUtilities import survey

table = survey.Pregnancies()
table.ReadRecords(data_dir="../NSFG")   # I put NSFG data in a peer directory.
print('Number of pregnancies', len(table.records))

# Exercise 1-3.2: Loop over table and count number of live births.
# From http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=PREG&section=&subSec=8016&srtLabel=611932
# Live birth count == 9148

nLiveBirths = 0
nFirstBirths = 0
nUnusualPrgLengths = 0

nWeeksOfFirstBirths = 0
nWeeksOfNonFirstBirths = 0

for pregrecord in table.records:
    if (pregrecord.outcome == 1):
        nLiveBirths += 1
        if (pregrecord.birthord == 1):
            nFirstBirths += 1
            nWeeksOfFirstBirths += pregrecord.prglength
        else:
            nWeeksOfNonFirstBirths += pregrecord.prglength

        if (pregrecord.prglength < 10 or pregrecord.prglength > 50):
            nUnusualPrgLengths += 1
            print("Unusual pregnancy length (weeks), birthorder:", pregrecord.prglength, pregrecord.birthord)

print("Number of live births:", nLiveBirths)

# Exercise 1-3.3: number of live births which were first births
# From http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=PREG&section=&subSec=8016&srtLabel=611933
# Expected number == 4413
print(" of which the number of first births was:", nFirstBirths)

print("Number of live birth pregnancies of length less than 10 weeks or more than 50:", nUnusualPrgLengths)
avgLenFirstBirths = nWeeksOfFirstBirths / nFirstBirths
avgLenNonFirstBirths = nWeeksOfNonFirstBirths / (nLiveBirths - nFirstBirths)
print("Average length of first births:", avgLenFirstBirths)
print("Average length of non-first births:", avgLenNonFirstBirths)

diffLenBirthsFirstVsNonFirst = avgLenFirstBirths - avgLenNonFirstBirths
print("First-NonFirst Birth Length Difference: {0:.2f} weeks, {1:.1f} days, {2:.1f} hours.".format(diffLenBirthsFirstVsNonFirst,
      diffLenBirthsFirstVsNonFirst * 7, diffLenBirthsFirstVsNonFirst * 7 * 24))

