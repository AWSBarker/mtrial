# encoding: utf-8
# module pandas._libs.tslibs.offsets
# from /media/Data2/ve_django4/lib/python3.9/site-packages/pandas/_libs/tslibs/offsets.cpython-39-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import operator as operator # /usr/lib/python3.9/operator.py
import re as re # /usr/lib/python3.9/re.py
import time as time # <module 'time' (built-in)>
import warnings as warnings # /usr/lib/python3.9/warnings.py
import numpy as np # /media/Data2/ve39_sharepoint/lib/python3.9/site-packages/numpy/__init__.py
from pandas._libs.properties import cache_readonly

from pandas._libs.tslibs.timedeltas import Timedelta

from pandas._libs.tslibs.timestamps import Timestamp


from .SingleConstructorOffset import SingleConstructorOffset

class Tick(SingleConstructorOffset):
    # no doc
    def is_anchored(self, *args, **kwargs): # real signature unknown
        pass

    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _next_higher_resolution(self, *args, **kwargs): # real signature unknown
        pass

    def _repr_attrs(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    delta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _adjust_dst = False
    _attributes = (
        'n',
        'normalize',
    )
    _prefix = 'undefined'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fc5b789fd80>'


