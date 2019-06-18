import numpy as np

def get_elems_of_type(line, element_type):

    pyst_ele_type_list = [ee.__class__.__name__ for ee in line.elements]
    indlist = np.where([ss == element_type for ss in pyst_ele_type_list])[0]
    ele_list = [line.elements[ind] for ind in indlist]
    name_list = [line.elements[ind] for ind in indlist]

    return indlist, name_list, ele_list

