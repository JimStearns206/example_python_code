"""Python file equivalent to Continuum-supplied demo notebook '1 - Diagonal Plot.ipynb'"""
import numpy as np
from bokeh.plotting import figure, output_notebook, output_file, show
#output_notebook()

# # First, the simple example from Bokeh's Getting Started documentation:
# x = [1, 2, 3, 4, 5]
# y = [6, 7, 2, 4, 5]
#
# # output to static HTML file
# output_file("lines.html", title='line plot example')
#
# # create a new plot with a title and axis labels
# p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
#
# # add a line renderer with legend and line thickness
# p.line(x, y, legend="Temp.", line_width=2)
#
# # show the results
# show(p)

# output to static HTML file
output_file("1-DiagonalPlot.html", title='Diagonal Plot Example')

# Generate some random data
N = 100
x = np.random.normal(size=N)
y = np.random.normal(size=N)

p = figure(title="Diagonal Plot", width=600, height=600)
p.scatter(x, y, marker="circle", color="red", size=6)

# Now let's draw a line representing y=x
minval = min(x.min(), y.min()) * 1.1
maxval = max(x.max(), y.max()) * 1.1
p.line([minval,maxval], [minval, maxval], color='gray', line_width=3)

mids = (x+y)/2
p.segment(mids, mids, x, y, color='gray', alpha=0.6, line_width=2, line_dash='dashed')
show(p)