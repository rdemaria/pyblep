"""
Conventions:
    class in CamelCase
    fields in lower_case
    units should use SI besides energy in [eV], charge in [e]
"""

from collections import namedtuple

class _MetaElement(type):
    def __new__(cls, clsname, bases, dct):
        print('-----------------------------------')
        print("Allocating memory for class", clsname)
        print(clsname)
        print(bases)
        print(dct)
        description =dct.get('_description',{})
        nt= namedtuple(clsname,[dd[0] for dd in description])
        doc = [dct['__doc__'],'\nFields:\n']
        fields=[ f"{field:10} [{unit+']:':5} {desc} " for field, unit, desc in description ]
        doc.append(fields))
        dct['__doc__']="\n".join(doc)
        print("named",nt,nt._fields)
        return super(_MetaElement, cls).__new__(cls, clsname, (nt,), dct)

class Element(metaclass=_MetaElement):
    pass

