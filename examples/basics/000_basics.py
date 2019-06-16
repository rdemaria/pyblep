import pyblep

line, other_data = pyblep.from_sixtrack_input('sixtrack_input')

# Build a pysixtrack line
import pysixtrack
ps_line = pysixtrack.Line.fromline(line)

# Build a pysixtracklib line
import pysixtracklib
pslib_line = pysixtracklib.Elements()
pslib_line.append_line(line)
pslib_line.BeamMonitor(num_stores=1)

# Build a pysixtrack particle
ps_part = pysixtrack.Particles(p0c=7000e9)
ps_part.x = 1e-3

# Build a pysixtracklib particle set
pslib_part_set = pysixtracklib.ParticlesSet()
pslib_part = pslib_part_set.Particles(num_particles=1)

# Attach extra sixtracklib information to pysixtrack particle:
ps_part.partid = 0
ps_part.state = 1
ps_part.elemid = 0
ps_part.turn = 0

# Set initialize pslib_part
pslib_part.from_pysixtrack(ps_part, particle_index=0)

# Track with pysisxtrack
ps_line.track(ps_part)

# Track with pysixtracklib
job = pysixtracklib.TrackJob(pslib_line, pslib_part_set)
job.track(until_turn=1)
job.collect()




