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


from .FY5253Mixin import FY5253Mixin

class FY5253(FY5253Mixin):
    """
    Describes 52-53 week fiscal year. This is also known as a 4-4-5 calendar.
    
        It is used by companies that desire that their
        fiscal year always end on the same day of the week.
    
        It is a method of managing accounting periods.
        It is a common calendar structure for some industries,
        such as retail, manufacturing and parking industry.
    
        For more information see:
        https://en.wikipedia.org/wiki/4-4-5_calendar
    
        The year may either:
    
        - end on the last X day of the Y month.
        - end on the last X day closest to the last day of the Y month.
    
        X is a specific day of the week.
        Y is a certain month of the year
    
        Parameters
        ----------
        n : int
        weekday : int {0, 1, ..., 6}, default 0
            A specific integer for the day of the week.
    
            - 0 is Monday
            - 1 is Tuesday
            - 2 is Wednesday
            - 3 is Thursday
            - 4 is Friday
            - 5 is Saturday
            - 6 is Sunday.
    
        startingMonth : int {1, 2, ... 12}, default 1
            The month in which the fiscal year ends.
    
        variation : str, default "nearest"
            Method of employing 4-4-5 calendar.
    
            There are two options:
    
            - "nearest" means year end is **weekday** closest to last day of month in year.
            - "last" means year end is final **weekday** of the final month in fiscal year.
    """
    def get_year_end(self, *args, **kwargs): # real signature unknown
        pass

    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_name(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _parse_suffix(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _attributes = (
        'n',
        'normalize',
        'weekday',
        'startingMonth',
        'variation',
    )
    _prefix = 'RE'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fc5b78c7a80>'


