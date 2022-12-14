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


# Variables with simple values

INVALID_FREQ_ERR_MSG = 'Invalid frequency: {0}'

# functions

def apply_array_wraps(*args, **kwargs): # real signature unknown
    pass

def apply_index_wraps(*args, **kwargs): # real signature unknown
    pass

def apply_wrapper_core(*args, **kwargs): # real signature unknown
    pass

def apply_wraps(*args, **kwargs): # real signature unknown
    pass

def delta_to_tick(*args, **kwargs): # real signature unknown
    pass

def easter(year, method=3): # reliably restored by inspect
    """
    This method was ported from the work done by GM Arts,
        on top of the algorithm by Claus Tondering, which was
        based in part on the algorithm of Ouding (1940), as
        quoted in "Explanatory Supplement to the Astronomical
        Almanac", P.  Kenneth Seidelmann, editor.
    
        This algorithm implements three different easter
        calculation methods:
    
        1 - Original calculation in Julian calendar, valid in
            dates after 326 AD
        2 - Original method, with date converted to Gregorian
            calendar, valid in years 1583 to 4099
        3 - Revised method, in Gregorian calendar, valid in
            years 1583 to 4099 as well
    
        These methods are represented by the constants:
    
        * ``EASTER_JULIAN   = 1``
        * ``EASTER_ORTHODOX = 2``
        * ``EASTER_WESTERN  = 3``
    
        The default method is method 3.
    
        More about the algorithm may be found at:
    
        `GM Arts: Easter Algorithms <http://www.gmarts.org/index.php?go=415>`_
    
        and
    
        `The Calendar FAQ: Easter <https://www.tondering.dk/claus/cal/easter.php>`_
    """
    pass

def roll_convention(*args, **kwargs): # real signature unknown
    """
    Possibly increment or decrement the number of periods to shift
        based on rollforward/rollbackward conventions.
    
        Parameters
        ----------
        other : int, generally the day component of a datetime
        n : number of periods to increment, before adjusting for rolling
        compare : int, generally the day component of a datetime, in the same
                  month as the datetime form which `other` was taken.
    
        Returns
        -------
        n : int number of periods to increment
    """
    pass

def roll_qtrday(*args, **kwargs): # real signature unknown
    """
    Possibly increment or decrement the number of periods to shift
        based on rollforward/rollbackward conventions.
    
        Parameters
        ----------
        other : datetime or Timestamp
        n : number of periods to increment, before adjusting for rolling
        month : int reference month giving the first month of the year
        day_opt : {'start', 'end', 'business_start', 'business_end'}
            The convention to use in finding the day in a given month against
            which to compare for rollforward/rollbackward decisions.
        modby : int 3 for quarters, 12 for years
    
        Returns
        -------
        n : int number of periods to increment
    
        See Also
        --------
        get_day_of_month : Find the day in a month provided an offset.
    """
    pass

def shift_day(*args, **kwargs): # real signature unknown
    """
    Increment the datetime `other` by the given number of days, retaining
        the time-portion of the datetime.  For tz-naive datetimes this is
        equivalent to adding a timedelta.  For tz-aware datetimes it is similar to
        dateutil's relativedelta.__add__, but handles pytz tzinfo objects.
    
        Parameters
        ----------
        other : datetime or Timestamp
        days : int
    
        Returns
        -------
        shifted: datetime or Timestamp
    """
    pass

def shift_month(*args, **kwargs): # real signature unknown
    """
    Given a datetime (or Timestamp) `stamp`, an integer `months` and an
        option `day_opt`, return a new datetimelike that many months later,
        with day determined by `day_opt` using relativedelta semantics.
    
        Scalar analogue of shift_months
    
        Parameters
        ----------
        stamp : datetime or Timestamp
        months : int
        day_opt : None, 'start', 'end', 'business_start', 'business_end', or int
            None: returned datetimelike has the same day as the input, or the
                  last day of the month if the new month is too short
            'start': returned datetimelike has day=1
            'end': returned datetimelike has day on the last day of the month
            'business_start': returned datetimelike has day on the first
                business day of the month
            'business_end': returned datetimelike has day on the last
                business day of the month
            int: returned datetimelike has day equal to day_opt
    
        Returns
        -------
        shifted : datetime or Timestamp (same as input `stamp`)
    """
    pass

def shift_months(*args, **kwargs): # real signature unknown
    """
    Given an int64-based datetime index, shift all elements
        specified number of months using DateOffset semantics
    
        day_opt: {None, 'start', 'end', 'business_start', 'business_end'}
           * None: day of month
           * 'start' 1st day of month
           * 'end' last day of month
    """
    pass

def to_offset(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Return DateOffset object from string or tuple representation
        or datetime.timedelta object.
    
        Parameters
        ----------
        freq : str, datetime.timedelta, BaseOffset or None
    
        Returns
        -------
        DateOffset or None
    
        Raises
        ------
        ValueError
            If freq is an invalid frequency
    
        See Also
        --------
        BaseOffset : Standard kind of date increment used for a date range.
    
        Examples
        --------
        >>> to_offset("5min")
        <5 * Minutes>
    
        >>> to_offset("1D1H")
        <25 * Hours>
    
        >>> to_offset("2W")
        <2 * Weeks: weekday=6>
    
        >>> to_offset("2B")
        <2 * BusinessDays>
    
        >>> to_offset(pd.Timedelta(days=1))
        <Day>
    
        >>> to_offset(Hour())
        <Hour>
    """
    pass

def _get_offset(EOM): # real signature unknown; restored from __doc__
    """
    Return DateOffset object associated with rule name.
    
        Examples
        --------
        _get_offset('EOM') --> BMonthEnd(1)
    """
    pass

def __pyx_unpickle_BaseOffset(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_RelativeDeltaOffset(*args, **kwargs): # real signature unknown
    pass

# classes

from .ApplyTypeError import ApplyTypeError
from .BaseOffset import BaseOffset
from .SingleConstructorOffset import SingleConstructorOffset
from .BusinessMixin import BusinessMixin
from .BusinessDay import BusinessDay
from .BDay import BDay
from .MonthOffset import MonthOffset
from .BusinessMonthBegin import BusinessMonthBegin
from .BMonthBegin import BMonthBegin
from .BusinessMonthEnd import BusinessMonthEnd
from .BMonthEnd import BMonthEnd
from .QuarterOffset import QuarterOffset
from .BQuarterBegin import BQuarterBegin
from .BQuarterEnd import BQuarterEnd
from .BusinessHour import BusinessHour
from .YearOffset import YearOffset
from .BYearBegin import BYearBegin
from .BYearEnd import BYearEnd
from ._CustomBusinessMonth import _CustomBusinessMonth
from .CustomBusinessMonthBegin import CustomBusinessMonthBegin
from .CBMonthBegin import CBMonthBegin
from .CustomBusinessMonthEnd import CustomBusinessMonthEnd
from .CBMonthEnd import CBMonthEnd
from .CustomBusinessDay import CustomBusinessDay
from .CDay import CDay
from .CustomBusinessHour import CustomBusinessHour
from .RelativeDeltaOffset import RelativeDeltaOffset
from .DateOffset import DateOffset
from .Tick import Tick
from .Day import Day
from .Easter import Easter
from .FY5253Mixin import FY5253Mixin
from .FY5253 import FY5253
from .FY5253Quarter import FY5253Quarter
from .Hour import Hour
from .WeekOfMonthMixin import WeekOfMonthMixin
from .LastWeekOfMonth import LastWeekOfMonth
from .Micro import Micro
from .Milli import Milli
from .Minute import Minute
from .MonthBegin import MonthBegin
from .MonthEnd import MonthEnd
from .Nano import Nano
from .OffsetMeta import OffsetMeta
from .QuarterBegin import QuarterBegin
from .QuarterEnd import QuarterEnd
from .relativedelta import relativedelta
from .Second import Second
from .SemiMonthOffset import SemiMonthOffset
from .SemiMonthBegin import SemiMonthBegin
from .SemiMonthEnd import SemiMonthEnd
from .Week import Week
from .WeekOfMonth import WeekOfMonth
from .YearBegin import YearBegin
from .YearEnd import YearEnd
# variables with complex values

int_to_weekday = {
    0: 'MON',
    1: 'TUE',
    2: 'WED',
    3: 'THU',
    4: 'FRI',
    5: 'SAT',
    6: 'SUN',
}

MONTH_ALIASES = {
    1: 'JAN',
    2: 'FEB',
    3: 'MAR',
    4: 'APR',
    5: 'MAY',
    6: 'JUN',
    7: 'JUL',
    8: 'AUG',
    9: 'SEP',
    10: 'OCT',
    11: 'NOV',
    12: 'DEC',
}

MONTH_TO_CAL_NUM = {
    'APR': 4,
    'AUG': 8,
    'DEC': 12,
    'FEB': 2,
    'JAN': 1,
    'JUL': 7,
    'JUN': 6,
    'MAR': 3,
    'MAY': 5,
    'NOV': 11,
    'OCT': 10,
    'SEP': 9,
}

opattern = None # (!) real value is "re.compile('([+\\\\-]?\\\\d*|[+\\\\-]?\\\\d*\\\\.\\\\d*)\\\\s*([A-Za-z]+([\\\\-][\\\\dA-Za-z\\\\-]+)?)')"

prefix_mapping = {
    'A': YearEnd,
    'AS': YearBegin,
    'B': BusinessDay,
    'BA': BYearEnd,
    'BAS': BYearBegin,
    'BH': BusinessHour,
    'BM': BusinessMonthEnd,
    'BMS': BusinessMonthBegin,
    'BQ': BQuarterEnd,
    'BQS': BQuarterBegin,
    'C': CustomBusinessDay,
    'CBH': CustomBusinessHour,
    'CBM': CustomBusinessMonthEnd,
    'CBMS': CustomBusinessMonthBegin,
    'D': Day,
    'H': Hour,
    'L': Milli,
    'M': MonthEnd,
    'MS': MonthBegin,
    'N': Nano,
    'Q': QuarterEnd,
    'QS': QuarterBegin,
    'RE': FY5253,
    'REQ': FY5253Quarter,
    'S': Second,
    'SM': SemiMonthEnd,
    'SMS': SemiMonthBegin,
    'T': Minute,
    'U': Micro,
    'W': Week,
    'WOM': WeekOfMonth,
}

weekday_to_int = {
    'FRI': 4,
    'MON': 0,
    'SAT': 5,
    'SUN': 6,
    'THU': 3,
    'TUE': 1,
    'WED': 2,
}

_dont_uppercase = None # (!) real value is "{'MS', 'ms'}"

_lite_rule_alias = {
    'A': 'A-DEC',
    'AS': 'AS-JAN',
    'BA': 'BA-DEC',
    'BAS': 'BAS-JAN',
    'BY': 'BA-DEC',
    'BYS': 'BAS-JAN',
    'Min': 'T',
    'Q': 'Q-DEC',
    'W': 'W-SUN',
    'Y': 'A-DEC',
    'YS': 'AS-JAN',
    'min': 'T',
    'ms': 'L',
    'ns': 'N',
    'us': 'U',
}

_offset_map = {}

_relativedelta_kwds = None # (!) real value is "{'seconds', 'hours', 'second', 'hour', 'minutes', 'months', 'weekday', 'year', 'weeks', 'years', 'minute', 'microsecond', 'month', 'microseconds', 'nanosecond', 'nanoseconds', 'days', 'day'}"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b789f460>'

__pyx_capi__ = {
    'is_offset_object': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x7fc5b789fc90>'
    'is_tick_object': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x7fc5b789fcc0>'
    'to_offset': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x7fc5b789fc60>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.offsets', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b789f460>, origin='/media/Data2/ve39_sharepoint/lib/python3.9/site-packages/pandas/_libs/tslibs/offsets.cpython-39-x86_64-linux-gnu.so')"

__test__ = {
    'to_offset (line 3580)': '\n    Return DateOffset object from string or tuple representation\n    or datetime.timedelta object.\n\n    Parameters\n    ----------\n    freq : str, datetime.timedelta, BaseOffset or None\n\n    Returns\n    -------\n    DateOffset or None\n\n    Raises\n    ------\n    ValueError\n        If freq is an invalid frequency\n\n    See Also\n    --------\n    BaseOffset : Standard kind of date increment used for a date range.\n\n    Examples\n    --------\n    >>> to_offset("5min")\n    <5 * Minutes>\n\n    >>> to_offset("1D1H")\n    <25 * Hours>\n\n    >>> to_offset("2W")\n    <2 * Weeks: weekday=6>\n\n    >>> to_offset("2B")\n    <2 * BusinessDays>\n\n    >>> to_offset(pd.Timedelta(days=1))\n    <Day>\n\n    >>> to_offset(Hour())\n    <Hour>\n    ',
}

