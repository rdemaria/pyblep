import sixtracktools
from .elements import Line

def from_sixtrack_input(input_folder = './'):

    sixtrack_specific = {}

    six = sixtracktools.SixInput(input_folder)
    line_data, rest, iconv = six.expand_struct()

    ele_names = [dd[0] for dd in line_data]
    ele_types = [dd[1] for dd in line_data]
    elements = [dd[2] for dd in line_data]

    line = Line(elements=elements)

    sixtrack_specific['sixinput'] = six
    sixtrack_specific['rest'] = rest
    sixtrack_specific['iconv'] = six

    return line, sixtrack_specific
