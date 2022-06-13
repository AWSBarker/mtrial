# encoding: utf-8
# module pandas._libs.tslibs.vectorized
# from /media/Data2/ve_django4/lib/python3.9/site-packages/pandas/_libs/tslibs/vectorized.cpython-39-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /media/Data2/ve39_sharepoint/lib/python3.9/site-packages/numpy/__init__.py
from pandas._libs.tslibs.dtypes import Resolution


# functions

def dt64arr_to_periodarr(*args, **kwargs): # real signature unknown
    pass

def get_resolution(*args, **kwargs): # real signature unknown
    pass

def ints_to_pydatetime(*args, **kwargs): # real signature unknown
    """
    Convert an i8 repr to an ndarray of datetimes, date, time or Timestamp.
    
        Parameters
        ----------
        arr : array of i8
        tz : str, optional
             convert to this timezone
        freq : str/Offset, optional
             freq to convert
        fold : bint, default is 0
            Due to daylight saving time, one wall clock time can occur twice
            when shifting from summer to winter time; fold describes whether the
            datetime-like corresponds  to the first (0) or the second time (1)
            the wall clock hits the ambiguous time
    
            .. versionadded:: 1.1.0
        box : {'datetime', 'timestamp', 'date', 'time'}, default 'datetime'
            * If datetime, convert to datetime.datetime
            * If date, convert to datetime.date
            * If time, convert to datetime.time
            * If Timestamp, convert to pandas.Timestamp
    
        Returns
        -------
        ndarray[object] of type specified by box
    """
    pass

def is_date_array_normalized(*args, **kwargs): # real signature unknown
    """
    Check if all of the given (nanosecond) timestamps are normalized to
        midnight, i.e. hour == minute == second == 0.  If the optional timezone
        `tz` is not None, then this is midnight for this timezone.
    
        Parameters
        ----------
        stamps : int64 ndarray
        tz : tzinfo or None
    
        Returns
        -------
        is_normalized : bool True if all stamps are normalized
    """
    pass

def normalize_i8_timestamps(*args, **kwargs): # real signature unknown
    """
    Normalize each of the (nanosecond) timezone aware timestamps in the given
        array by rounding down to the beginning of the day (i.e. midnight).
        This is midnight for timezone, `tz`.
    
        Parameters
        ----------
        stamps : int64 ndarray
        tz : tzinfo or None
    
        Returns
        -------
        result : int64 ndarray of converted of normalized nanosecond timestamps
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b74addc0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.vectorized', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b74addc0>, origin='/media/Data2/ve39_sharepoint/lib/python3.9/site-packages/pandas/_libs/tslibs/vectorized.cpython-39-x86_64-linux-gnu.so')"

__test__ = {}

