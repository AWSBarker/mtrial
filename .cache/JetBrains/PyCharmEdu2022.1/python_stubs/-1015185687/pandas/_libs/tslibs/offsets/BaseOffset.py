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


from .object import object

class BaseOffset(object):
    """ Base class for DateOffset methods that are not overridden by subclasses. """
    def apply(self, *args, **kwargs): # real signature unknown
        pass

    def apply_index(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def isAnchored(self, *args, **kwargs): # real signature unknown
        pass

    def is_anchored(self, *args, **kwargs): # real signature unknown
        pass

    def is_month_end(self, *args, **kwargs): # real signature unknown
        pass

    def is_month_start(self, *args, **kwargs): # real signature unknown
        pass

    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def is_quarter_end(self, *args, **kwargs): # real signature unknown
        pass

    def is_quarter_start(self, *args, **kwargs): # real signature unknown
        pass

    def is_year_end(self, *args, **kwargs): # real signature unknown
        pass

    def is_year_start(self, *args, **kwargs): # real signature unknown
        pass

    def onOffset(self, *args, **kwargs): # real signature unknown
        pass

    def rollback(self, *args, **kwargs): # real signature unknown
        """
        Roll provided date backward to next offset only if not on offset.
        
                Returns
                -------
                TimeStamp
                    Rolled timestamp if not on offset, otherwise unchanged timestamp.
        """
        pass

    def rollforward(self, *args, **kwargs): # real signature unknown
        """
        Roll provided date forward to next offset only if not on offset.
        
                Returns
                -------
                TimeStamp
                    Rolled timestamp if not on offset, otherwise unchanged timestamp.
        """
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    def _get_offset_day(self, *args, **kwargs): # real signature unknown
        pass

    def _offset_str(self, *args, **kwargs): # real signature unknown
        pass

    def _repr_attrs(self, *args, **kwargs): # real signature unknown
        pass

    def _validate_n(self, *args, **kwargs): # real signature unknown
        """
        Require that `n` be an integer.
        
                Parameters
                ----------
                n : int
        
                Returns
                -------
                nint : int
        
                Raises
                ------
                TypeError if `int(n)` raises
                ValueError if n != int(n)
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ Return a pickleable state """
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

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
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

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Reconstruct an instance from a pickled state """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns a copy of the calling offset object with n=1 and all other
        attributes equal.
        """

    kwds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    normalize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rule_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _cache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    freqstr = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x7fc5b7479fc0>'
    _adjust_dst = True
    _attributes = (
        'n',
        'normalize',
    )
    _day_opt = None
    _deprecations = frozenset({'isAnchored', 'onOffset'})
    _params = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x7fc5b7885800>'
    _use_relativedelta = False
    __array_priority__ = 1000


