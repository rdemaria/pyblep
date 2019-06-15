import pyblep

line, other_data = pyblep.from_sixtrack_input('sixtrack_input')

# Build a pysixtrack line
import pysixtrack
ps_line = pysixtrack.Line.fromline(line)

# Build a pysixtracklib line
import pysixtracklib
pslib_line = pysixtracklib.Elements.fromline(line)
