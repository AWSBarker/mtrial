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


from .BaseOffset import BaseOffset

class RelativeDeltaOffset(BaseOffset):
    """ DateOffset subclass backed by a dateutil relativedelta object. """
    def apply_index(self, *args, **kwargs): # real signature unknown
        pass

    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ Return a pickleable state """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Reconstruct an instance from a pickled state """
        pass

    _adjust_dst = False
    _attributes = (
        'n',
        'normalize',
        'seconds',
        'hours',
        'second',
        'hour',
        'minutes',
        'months',
        'weekday',
        'year',
        'weeks',
        'years',
        'minute',
        'microsecond',
        'month',
        'microseconds',
        'nanosecond',
        'nanoseconds',
        'days',
        'day',
    )


