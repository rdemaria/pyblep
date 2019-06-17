from cpymad.madx import Madx
import pyblep.elements as pbelms

mad=Madx()
mad.options.echo=False;
mad.options.warn=False;
mad.options.info=False;

mad.call('mad/lhcwbb.seq')

seq = mad.sequence.lhcb1

elements = seq.elements
ele_pos = seq.element_positions()

line = pbelms.Line(elements=[])
old_pp = 0.
for ee, pp in zip(elements, ele_pos):
    if pp>old_pp:
        line.elements.append(pbelms.Drift(length=(pp-old_pp)))
    
    if ee.length > 0:
        raise ValueError(f"Seq {seq} contails {el} with length>0")

    mad_etype = ee.base_type.name
    
    if mad_etype in ['marker', 'monitor', 'hmonitor', 'vmonitor',
            'rcollimator', 'placeholder', 'instrument']:
        newele = pbelms.Drift(length=0.)

    elif mad_etype == 'multipole':
         knl = ee.knl if hasattr(ee, 'knl') else [0]
         ksl = ee.ksl if hasattr(ee, 'ksl') else [0]
         newele = pbelms.Multipole(
             knl=knl,
             ksl=ksl,
             hxl=knl[0],
             hyl=0,
             length=ee.lrad)

    elif mad_etype == 'tkicker':
         hkick = -ee.hkick if hasattr(ee, 'hkick') else []
         vkick = ee.vkick if hasattr(ee, 'vkick') else []
         newele = pbelms.Multipole(knl=hkick, ksl=vkick,
                        length=ee.lrad, hxl=0, hyl=0)

    elif mad_etype == 'vkicker':
        newele = pbelms.Multipole(knl=[], ksl=[ee.kick],
                        length=ee.lrad, hxl=0, hyl=0)

    elif mad_etype == 'hkicker':
        newele = pbelms.Multipole(knl=[-ee.kick], ksl=[],
                       length=ee.lrad, hxl=0, hyl=0)

    elif mad_etype == 'rfcavity':
        newele = pbelms.Cavity(voltage=ee.volt * 1e6,
                    frequency=ee.freq * 1e6, lag=ee.lag * 360)
    else:
        raise ValueError('Not recognized')

    line.elements.append(newele)
