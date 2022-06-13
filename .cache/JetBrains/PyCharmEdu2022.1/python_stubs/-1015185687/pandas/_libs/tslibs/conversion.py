# encoding: utf-8
# module pandas._libs.tslibs.conversion
# from /media/Data2/ve_django4/lib/python3.9/site-packages/pandas/_libs/tslibs/conversion.cpython-39-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /media/Data2/ve39_sharepoint/lib/python3.9/site-packages/numpy/__init__.py
import pytz as pytz # /media/Data2/ve39_sharepoint/lib/python3.9/site-packages/pytz/__init__.py
from pandas._libs.tslibs.np_datetime import OutOfBoundsDatetime

from pandas._libs.tslibs.parsing import parse_datetime_string


# functions

def datetime_to_datetime64(*args, **kwargs): # real signature unknown
    """
    Convert ndarray of datetime-like objects to int64 array representing
        nanosecond timestamps.
    
        Parameters
        ----------
        values : ndarray[object]
    
        Returns
        -------
        result : ndarray[datetime64ns]
        inferred_tz : tzinfo or None
    """
    pass

def ensure_datetime64ns(*args, **kwargs): # real signature unknown
    """
    Ensure a np.datetime64 array has dtype specifically 'datetime64[ns]'
    
        Parameters
        ----------
        arr : ndarray
        copy : bool, default True
    
        Returns
        -------
        ndarray with dtype datetime64[ns]
    """
    pass

def ensure_timedelta64ns(*args, **kwargs): # real signature unknown
    """
    Ensure a np.timedelta64 array has dtype specifically 'timedelta64[ns]'
    
        Parameters
        ----------
        arr : ndarray
        copy : bool, default True
    
        Returns
        -------
        ndarray[timedelta64[ns]]
    """
    pass

def localize_pydatetime(*args, **kwargs): # real signature unknown
    """
    Take a datetime/Timestamp in UTC and localizes to timezone tz.
    
        Parameters
        ----------
        dt : datetime or Timestamp
        tz : tzinfo or None
    
        Returns
        -------
        localized : datetime or Timestamp
    """
    pass

def precision_from_unit(*args, **kwargs): # real signature unknown
    """
    Return a casting of the unit represented to nanoseconds + the precision
        to round the fractional part.
    
        Notes
        -----
        The caller is responsible for ensuring that the default value of "ns"
        takes the place of None.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class OutOfBoundsTimedelta(ValueError):
    """
    Raised when encountering a timedelta value that cannot be represented
        as a timedelta64[ns].
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class _TSObject(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

DT64NS_DTYPE = None # (!) real value is "dtype('<M8[ns]')"

TD64NS_DTYPE = None # (!) real value is "dtype('<m8[ns]')"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b7d37b50>'

__pyx_capi__ = {
    'cast_from_unit': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *, PyObject *)" at 0x7fc5b7d390c0>'
    'convert_datetime_to_tsobject': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_10conversion__TSObject *(PyDateTime_DateTime *, PyDateTime_TZInfo *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_convert_datetime_to_tsobject *__pyx_optional_args)" at 0x7fc5b7d39030>'
    'convert_to_tsobject': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyDateTime_TZInfo *, PyObject *, int, int, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_convert_to_tsobject *__pyx_optional_args)" at 0x7fc5b7d37fc0>'
    'get_datetime64_nanos': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *)" at 0x7fc5b7d39060>'
    'localize_pydatetime': None, # (!) real value is '<capsule object "PyDateTime_DateTime *(PyDateTime_DateTime *, PyDateTime_TZInfo *, int __pyx_skip_dispatch)" at 0x7fc5b7d39090>'
    'normalize_i8_stamp': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (__pyx_t_5numpy_int64_t)" at 0x7fc5b7d39120>'
    'precision_from_unit': None, # (!) real value is '<capsule object "__pyx_ctuple___dunderpyx_t_5numpy_int64_t__and_int (PyObject *, int __pyx_skip_dispatch)" at 0x7fc5b7d390f0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.conversion', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b7d37b50>, origin='/media/Data2/ve39_sharepoint/lib/python3.9/site-packages/pandas/_libs/tslibs/conversion.cpython-39-x86_64-linux-gnu.so')"

__test__ = {}

