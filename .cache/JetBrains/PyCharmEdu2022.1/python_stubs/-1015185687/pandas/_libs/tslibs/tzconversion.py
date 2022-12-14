# encoding: utf-8
# module pandas._libs.tslibs.tzconversion
# from /media/Data2/ve_django4/lib/python3.9/site-packages/pandas/_libs/tslibs/tzconversion.cpython-39-x86_64-linux-gnu.so
# by generator 1.147
""" timezone conversion """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /media/Data2/ve39_sharepoint/lib/python3.9/site-packages/numpy/__init__.py
import pytz as pytz # /media/Data2/ve39_sharepoint/lib/python3.9/site-packages/pytz/__init__.py
import datetime as __datetime


# functions

def tz_convert_from_utc(*args, **kwargs): # real signature unknown
    """
    Convert the values (in i8) from UTC to tz
    
        Parameters
        ----------
        vals : int64 ndarray
        tz : tzinfo
    
        Returns
        -------
        int64 ndarray of converted
    """
    pass

def tz_convert_from_utc_single(*args, **kwargs): # real signature unknown
    """
    Convert the val (in i8) from UTC to tz
    
        This is a single value version of tz_convert_from_utc.
    
        Parameters
        ----------
        val : int64
        tz : tzinfo
    
        Returns
        -------
        converted: int64
    """
    pass

def tz_localize_to_utc(*args, **kwargs): # real signature unknown
    """
    Localize tzinfo-naive i8 to given time zone (using pytz). If
        there are ambiguities in the values, raise AmbiguousTimeError.
    
        Parameters
        ----------
        vals : ndarray[int64_t]
        tz : tzinfo or None
        ambiguous : str, bool, or arraylike
            When clocks moved backward due to DST, ambiguous times may arise.
            For example in Central European Time (UTC+01), when going from 03:00
            DST to 02:00 non-DST, 02:30:00 local time occurs both at 00:30:00 UTC
            and at 01:30:00 UTC. In such a situation, the `ambiguous` parameter
            dictates how ambiguous times should be handled.
    
            - 'infer' will attempt to infer fall dst-transition hours based on
              order
            - bool-ndarray where True signifies a DST time, False signifies a
              non-DST time (note that this flag is only applicable for ambiguous
              times, but the array must have the same length as vals)
            - bool if True, treat all vals as DST. If False, treat them as non-DST
            - 'NaT' will return NaT where there are ambiguous times
    
        nonexistent : {None, "NaT", "shift_forward", "shift_backward", "raise", timedelta-like}
            How to handle non-existent times when converting wall times to UTC
    
        Returns
        -------
        localized : ndarray[int64_t]
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class tzutc(__datetime.tzinfo):
    """
    This is a tzinfo object that represents the UTC time zone.
    
        **Examples:**
    
        .. doctest::
    
            >>> from datetime import *
            >>> from dateutil.tz import *
    
            >>> datetime.now()
            datetime.datetime(2003, 9, 27, 9, 40, 1, 521290)
    
            >>> datetime.now(tzutc())
            datetime.datetime(2003, 9, 27, 12, 40, 12, 156379, tzinfo=tzutc())
    
            >>> datetime.now(tzutc()).tzname()
            'UTC'
    
        .. versionchanged:: 2.7.0
            ``tzutc()`` is now a singleton, so the result of ``tzutc()`` will
            always return the same object.
    
            .. doctest::
    
                >>> from dateutil.tz import tzutc, UTC
                >>> tzutc() is tzutc()
                True
                >>> tzutc() is UTC
                True
    """
    def dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def fromutc(self, dt): # reliably restored by inspect
        """
        Fast track version of fromutc() returns the original ``dt`` object for
                any valid :py:class:`datetime.datetime` object.
        """
        pass

    def is_ambiguous(self, dt): # reliably restored by inspect
        """
        Whether or not the "wall time" of a given datetime is ambiguous in this
                zone.
        
                :param dt:
                    A :py:class:`datetime.datetime`, naive or time zone aware.
        
        
                :return:
                    Returns ``True`` if ambiguous, ``False`` otherwise.
        
                .. versionadded:: 2.6.0
        """
        pass

    def tzname(self, dt): # reliably restored by inspect
        # no doc
        pass

    def utcoffset(self, dt): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _TzSingleton__instance = tzutc()
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'dateutil.tz.tz\', \'__doc__\': "\\n    This is a tzinfo object that represents the UTC time zone.\\n\\n    **Examples:**\\n\\n    .. doctest::\\n\\n        >>> from datetime import *\\n        >>> from dateutil.tz import *\\n\\n        >>> datetime.now()\\n        datetime.datetime(2003, 9, 27, 9, 40, 1, 521290)\\n\\n        >>> datetime.now(tzutc())\\n        datetime.datetime(2003, 9, 27, 12, 40, 12, 156379, tzinfo=tzutc())\\n\\n        >>> datetime.now(tzutc()).tzname()\\n        \'UTC\'\\n\\n    .. versionchanged:: 2.7.0\\n        ``tzutc()`` is now a singleton, so the result of ``tzutc()`` will\\n        always return the same object.\\n\\n        .. doctest::\\n\\n            >>> from dateutil.tz import tzutc, UTC\\n            >>> tzutc() is tzutc()\\n            True\\n            >>> tzutc() is UTC\\n            True\\n    ", \'utcoffset\': <function tzutc.utcoffset at 0x7fc5b79921f0>, \'dst\': <function tzutc.dst at 0x7fc5b7992280>, \'tzname\': <function tzutc.tzname at 0x7fc5b7992310>, \'is_ambiguous\': <function tzutc.is_ambiguous at 0x7fc5b79923a0>, \'fromutc\': <function tzutc.fromutc at 0x7fc5b79924c0>, \'__eq__\': <function tzutc.__eq__ at 0x7fc5b7992550>, \'__hash__\': None, \'__ne__\': <function tzutc.__ne__ at 0x7fc5b79925e0>, \'__repr__\': <function tzutc.__repr__ at 0x7fc5b7992670>, \'__reduce__\': <method \'__reduce__\' of \'object\' objects>, \'__dict__\': <attribute \'__dict__\' of \'tzutc\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'tzutc\' objects>, \'_TzSingleton__instance\': tzutc()})'
    __hash__ = None


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b7971d60>'

__pyx_capi__ = {
    'tz_convert_from_utc_single': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (__pyx_t_5numpy_int64_t, PyDateTime_TZInfo *, int __pyx_skip_dispatch)" at 0x7fc5b797dc30>'
    'tz_convert_utc_to_tzlocal': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (__pyx_t_5numpy_int64_t, PyDateTime_TZInfo *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_12tzconversion_tz_convert_utc_to_tzlocal *__pyx_optional_args)" at 0x7fc5b797d630>'
    'tz_localize_to_utc_single': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (__pyx_t_5numpy_int64_t, PyDateTime_TZInfo *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_12tzconversion_tz_localize_to_utc_single *__pyx_optional_args)" at 0x7fc5b797d780>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.tzconversion', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b7971d60>, origin='/media/Data2/ve39_sharepoint/lib/python3.9/site-packages/pandas/_libs/tslibs/tzconversion.cpython-39-x86_64-linux-gnu.so')"

__test__ = {}

