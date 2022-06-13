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


from .QuarterOffset import QuarterOffset

class QuarterBegin(QuarterOffset):
    """
    DateOffset increments between Quarter start dates.
    
        startingMonth = 1 corresponds to dates like 1/01/2007, 4/01/2007, ...
        startingMonth = 2 corresponds to dates like 2/01/2007, 5/01/2007, ...
        startingMonth = 3 corresponds to dates like 3/01/2007, 6/01/2007, ...
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _day_opt = 'start'
    _default_starting_month = 3
    _from_name_starting_month = 1
    _prefix = 'QS'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fc5b78c75a0>'


