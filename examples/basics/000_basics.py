import pyblep

line, other_data = pyblep.from_sixtrack_input('sixtrack_input')

# Build a pysixtrack line
import pysixtrack
psline = pysixtrack.Line.fromline(line)
