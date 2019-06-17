from cpymad.madx import Madx
import pyblep

mad=Madx()
mad.options.echo=False;
mad.options.warn=False;
mad.options.info=False;

mad.call('mad/lhcwbb.seq')

line, other = pyblep.from_madx_sequence(mad.sequence.lhcb1)


