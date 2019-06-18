"""
Conventions:
    class in CamelCase
    fields in lower_case
    units should use SI besides energy in [eV], charge in [e]
"""

from collections import namedtuple
from dataclasses import dataclass
import dataclasses

class _MetaElement(type):
    def __new__(cls, clsname, bases, dct):
        # print('-----------------------------------')
        # print("Allocating memory for class", clsname)
        # print(clsname)
        # print(bases)
        # print(dct)
        description = dct.get('_description', [])
        ann={}
        dct['__annotations__']=ann
        for name,unit,desc in description:
            ann[name]=object
        try:
            doc = [dct['__doc__'], '\nFields:\n']
        except KeyError:
            doc = ['\nFields:\n']
        fields = [f"{field:10} [{unit+']:':5} {desc} " for field,
                  unit, desc in description]
        doc += fields
        dct['__doc__'] = "\n".join(doc)
        dct['_asdict']=dataclasses.asdict
        dct['_fields']=[dd[0] for dd in description]
        # print("named",nt,nt._fields)
        newclass=super(_MetaElement, cls).__new__(cls, clsname, bases, dct)
        return dataclass(newclass)

class Element(metaclass=_MetaElement):
    @classmethod
    def from_dict(cls,dct):
        return cls(**{kk:dct[kk] for kk in cls._fields})

