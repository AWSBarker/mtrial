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


from .YearOffset import YearOffset

class BYearBegin(YearOffset):
    """
    DateOffset increments between the first business day of the year.
    
        Examples
        --------
        >>> from pandas.tseries.offsets import BYearBegin
        >>> ts = pd.Timestamp('2020-05-24 05:01:15')
        >>> ts + BYearBegin()
        Timestamp('2021-01-01 05:01:15')
        >>> ts - BYearBegin()
        Timestamp('2020-01-01 05:01:15')
        >>> ts + BYearBegin(-1)
        Timestamp('2020-01-01 05:01:15')
        >>> ts + BYearBegin(2)
        Timestamp('2022-01-03 05:01:15')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _day_opt = 'business_start'
    _default_month = 1
    _outputName = 'BusinessYearBegin'
    _prefix = 'BAS'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fc5b78c7300>'


