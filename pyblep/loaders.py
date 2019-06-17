import sixtracktools
from .elements import Line

def from_sixtrack_input(input_folder = './'):

    other_info = {}

    six = sixtracktools.SixInput(input_folder)
    line_data, rest, iconv = six.expand_struct()

    ele_names = [dd[0] for dd in line_data]
    ele_types = [dd[1] for dd in line_data]
    elements = [dd[2] for dd in line_data]

    line = Line(elements=elements)

    other_info['sixinput'] = six
    other_info['rest'] = rest
    other_info['iconv'] = six
    other_info['element_names'] = ele_names

    return line, other_info

def from_madx_sequence(sequence):
    
    seq = sequence

    elements = seq.elements
    ele_pos = seq.element_positions()
    
    line = pbelms.Line(elements=[])
    element_names = []
    old_pp = 0.
    i_drift = 0
    for ee, pp in zip(elements, ele_pos):
        if pp>old_pp:
            line.elements.append(pbelms.Drift(length=(pp-old_pp)))
            element_names.append('drift_%d'%i_drift)
            i_drift +=1 
    
        if ee.length > 0:
            raise ValueError(f"Seq {seq} contails {el} with length>0")
    
        mad_etype = ee.base_type.name
        eename = ee.name
    
        if mad_etype in ['marker', 'monitor', 'hmonitor', 'vmonitor',
                'rcollimator', 'placeholder', 'instrument', 'solenoid']:
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
    
        elif mad_etype == 'beambeam':
            if eename.startswith('bb_par'):
                ## BB interaction is 4D
                newele = pbelms.BeamBeam4D(
                    charge  = 0.,
                    sigma_x = 1.,
                    sigma_y = 1., 
                    beta_r  = 1., 
                    x_bb    = 0.,
                    y_bb    = 0., 
                    d_px    = 0.,
                    d_py    = 0.,
                    )
    
            elif eename.startswith('bb_ho'):
                ## BB interaction is 6D
                newele = pbelms.BeamBeam6D(
                    phi     = 0., 
                    alpha   = 0.,   
                    x_bb_co = 0.,   
                    y_bb_co = 0.,   
                    charge_slices = [0.], 
                    zeta_slices = [0.],
                    sigma_11 = 1.,  
                    sigma_12 = 0.,  
                    sigma_13 = 0.,  
                    sigma_14 = 0.,  
                    sigma_22 = 1.,  
                    sigma_23 = 0.,  
                    sigma_24 = 0.,  
                    sigma_33 = 0.,  
                    sigma_34 = 0.,  
                    sigma_44 = 0.,  
                    x_co     = 0.,  
                    px_co    = 0.,  
                    y_co     = 0.,  
                    py_co    = 0.,  
                    zeta_co  = 0.,  
                    delta_co = 0.,  
                    d_x      = 0.,  
                    d_px     = 0.,  
                    d_y      = 0.,  
                    d_py     = 0.,  
                    d_zeta   = 0.,  
                    d_delta  = 0.,  
                    )
            else:
                raise ValueError(
                        'Beam beam type for element "%s" not recognized')
    
        else:
            raise ValueError('Not recognized')
    
        line.elements.append(newele)
        element_names.append(eename)

    other_info = {}
    other_info['element_names'] = element_names

    return line, other_info
