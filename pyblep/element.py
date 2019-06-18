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
        description = dct.get('_description', {})
        nt = namedtuple(clsname, [dd[0] for dd in description])
        try:
            doc = [dct['__doc__'], '\nFields:\n']
        except KeyError:
            doc = ['\nFields:\n']
        fields = [f"{field:10} [{unit+']:':5} {desc} " for field,
                  unit, desc in description]
        doc += fields
        dct['__doc__'] = "\n".join(doc)
        # print("named",nt,nt._fields)
        return super(_MetaElement, cls).__new__(cls, clsname, (nt,), dct)

class _MetaElement2(type):
    def __new__(cls, clsname, bases, dct):
        # print('-----------------------------------')
        # print("Allocating memory for class", clsname)
        # print(clsname)
        # print(bases)
        # print(dct)
        description = dct.get('_description', {})
        base=type(clsname,(object,),{})
        base.__annotations__={}
        for name,unit,desc in description:
            base.__annotations__[name]=object
        base=dataclass(base)
        try:
            doc = [dct['__doc__'], '\nFields:\n']
        except KeyError:
            doc = ['\nFields:\n']
        fields = [f"{field:10} [{unit+']:':5} {desc} " for field,
                  unit, desc in description]
        doc += fields
        dct['__doc__'] = "\n".join(doc)
        dct['_asdict']=dataclasses.asdict
        # print("named",nt,nt._fields)
        return super(_MetaElement2, cls).__new__(cls, clsname, (base,), dct)

class Element(metaclass=_MetaElement2):
    pass
