import sixtracktools
from . import elements as pyblep_elements


def from_sixtrack_input(input_folder='./'):

    other_info = {}

    six = sixtracktools.SixInput(input_folder)
    line_data, rest, iconv = six.expand_struct()

    ele_names = [dd[0] for dd in line_data]
    ele_types = [dd[1] for dd in line_data]
    elements = [dd[2] for dd in line_data]

    line = pyblep_elements.Line(elements=elements)

    other_info['sixinput'] = six
    other_info['rest'] = rest
    other_info['iconv'] = six
    other_info['element_names'] = ele_names

    return line, other_info
