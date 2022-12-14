# encoding: utf-8
# module pandas._libs.tslibs.strptime
# from /media/Data2/ve_django4/lib/python3.9/site-packages/pandas/_libs/tslibs/strptime.cpython-39-x86_64-linux-gnu.so
# by generator 1.147
""" Strptime-related classes and functions. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import calendar as calendar # /usr/lib/python3.9/calendar.py
import locale as locale # /usr/lib/python3.9/locale.py
import re as re # /usr/lib/python3.9/re.py
import time as time # <module 'time' (built-in)>
import numpy as np # /media/Data2/ve39_sharepoint/lib/python3.9/site-packages/numpy/__init__.py
import pytz as pytz # /media/Data2/ve39_sharepoint/lib/python3.9/site-packages/pytz/__init__.py
from _thread import _thread_allocate_lock


# Variables with simple values

_CACHE_MAX_SIZE = 5

# functions

def array_strptime(*args, **kwargs): # real signature unknown
    """
    Calculates the datetime structs represented by the passed array of strings
    
        Parameters
        ----------
        values : ndarray of string-like objects
        fmt : string-like regex
        exact : matches must be exact if True, search if False
        errors : string specifying error handling, {'raise', 'ignore', 'coerce'}
    """
    pass

def _getlang(*args, **kwargs): # real signature unknown
    """ Figure out what language is being used for the locale """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class LocaleTime(object):
    """
    Stores and handles locale-specific information related to time.
    
        ATTRIBUTES:
            f_weekday -- full weekday names (7-item list)
            a_weekday -- abbreviated weekday names (7-item list)
            f_month -- full month names (13-item list; dummy value in [0], which
                        is added by code)
            a_month -- abbreviated month names (13-item list, dummy value in
                        [0], which is added by code)
            am_pm -- AM/PM representation (2-item list)
            LC_date_time -- format string for date/time representation (string)
            LC_date -- format string for date representation (string)
            LC_time -- format string for time representation (string)
            timezone -- daylight- and non-daylight-savings timezone representation
                        (2-item list of sets)
            lang -- Language used by instance (2-item tuple)
    """
    def _LocaleTime__calc_am_pm(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_date_time(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_month(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_timezone(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_weekday(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__pad(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Set all attributes.
        
                Order of methods called matters for dependency reasons.
        
                The locale language is set at the offset and then checked again before
                exiting.  This is to make sure that the attributes were not set with a
                mix of information from more than one locale.  This would most likely
                happen when using threads where one thread calls a locale-dependent
                function while another thread changes the locale while the function in
                the other thread is still running.  Proper coding would call for
                locks to prevent changing the locale while locale-dependent code is
                running.  The check here is done in case someone does not think about
                doing this.
        
                Only other possible issue is if someone changed the timezone and did
                not call tz.tzset .  That is an issue for the programmer, though,
                since changing the timezone is worthless without that call.
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pandas._libs.tslibs.strptime', '__doc__': '\\n    Stores and handles locale-specific information related to time.\\n\\n    ATTRIBUTES:\\n        f_weekday -- full weekday names (7-item list)\\n        a_weekday -- abbreviated weekday names (7-item list)\\n        f_month -- full month names (13-item list; dummy value in [0], which\\n                    is added by code)\\n        a_month -- abbreviated month names (13-item list, dummy value in\\n                    [0], which is added by code)\\n        am_pm -- AM/PM representation (2-item list)\\n        LC_date_time -- format string for date/time representation (string)\\n        LC_date -- format string for date representation (string)\\n        LC_time -- format string for time representation (string)\\n        timezone -- daylight- and non-daylight-savings timezone representation\\n                    (2-item list of sets)\\n        lang -- Language used by instance (2-item tuple)\\n    ', '__init__': <cyfunction LocaleTime.__init__ at 0x7fc5b78bb860>, '_LocaleTime__pad': <cyfunction LocaleTime.__pad at 0x7fc5b78bba00>, '_LocaleTime__calc_weekday': <cyfunction LocaleTime.__calc_weekday at 0x7fc5b78bbad0>, '_LocaleTime__calc_month': <cyfunction LocaleTime.__calc_month at 0x7fc5b78bbba0>, '_LocaleTime__calc_am_pm': <cyfunction LocaleTime.__calc_am_pm at 0x7fc5b78bbc70>, '_LocaleTime__calc_date_time': <cyfunction LocaleTime.__calc_date_time at 0x7fc5b78bbd40>, '_LocaleTime__calc_timezone': <cyfunction LocaleTime.__calc_timezone at 0x7fc5b78bbe10>, '__dict__': <attribute '__dict__' of 'LocaleTime' objects>, '__weakref__': <attribute '__weakref__' of 'LocaleTime' objects>})"


class TimeRE(dict):
    """
    Handle conversion from format directives to regexes.
    
        Creates regexes for pattern matching a string of text containing
        time information
    """
    def compile(self, *args, **kwargs): # real signature unknown
        """ Return a compiled re object for the format string. """
        pass

    def pattern(self, *args, **kwargs): # real signature unknown
        """
        Return regex pattern for the format string.
        
                Need to make sure that any characters that might be interpreted as
                regex syntax are escaped.
        """
        pass

    def _TimeRE__seqToRE(self, *args, **kwargs): # real signature unknown
        """
        Convert a list to a regex string for matching a directive.
        
                Want possible matching values to be from longest to shortest.  This
                prevents the possibility of a match occurring for a value that also
                a substring of a larger value that should have matched (e.g., 'abc'
                matching when 'abcdef' should have been the match).
        """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Create keys/values.
        
                Order of execution is important for dependency reasons.
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pandas._libs.tslibs.strptime', '__doc__': '\\n    Handle conversion from format directives to regexes.\\n\\n    Creates regexes for pattern matching a string of text containing\\n    time information\\n    ', '__init__': <cyfunction TimeRE.__init__ at 0x7fc5b78bbee0>, '__getitem__': <cyfunction TimeRE.__getitem__ at 0x7fc5b788c040>, '_TimeRE__seqToRE': <cyfunction TimeRE.__seqToRE at 0x7fc5b788c110>, 'pattern': <cyfunction TimeRE.pattern at 0x7fc5b788c1e0>, 'compile': <cyfunction TimeRE.compile at 0x7fc5b788c2b0>, '__dict__': <attribute '__dict__' of 'TimeRE' objects>, '__weakref__': <attribute '__weakref__' of 'TimeRE' objects>})"


# variables with complex values

_cache_lock = None # (!) real value is '<unlocked _thread.lock object at 0x7fc5b7863c90>'

_regex_cache = {}

_TimeRE_cache = {
    '%': '%',
    'A': '(?P<A>wednesday|thursday|saturday|tuesday|monday|friday|sunday)',
    'B': '(?P<B>september|february|november|december|january|october|august|march|april|june|july|may)',
    'G': '(?P<G>\\d\\d\\d\\d)',
    'H': '(?P<H>2[0-3]|[0-1]\\d|\\d)',
    'I': '(?P<I>1[0-2]|0[1-9]|[1-9])',
    'M': '(?P<M>[0-5]\\d|\\d)',
    'S': '(?P<S>6[0-1]|[0-5]\\d|\\d)',
    'U': '(?P<U>5[0-3]|[0-4]\\d|\\d)',
    'V': '(?P<V>5[0-3]|0[1-9]|[1-4]\\d|\\d)',
    'W': '(?P<W>5[0-3]|[0-4]\\d|\\d)',
    'X': '(?P<H>2[0-3]|[0-1]\\d|\\d):(?P<M>[0-5]\\d|\\d):(?P<S>6[0-1]|[0-5]\\d|\\d)',
    'Y': '(?P<Y>\\d\\d\\d\\d)',
    'a': '(?P<a>mon|tue|wed|thu|fri|sat|sun)',
    'b': '(?P<b>jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)',
    'c': '(?P<a>mon|tue|wed|thu|fri|sat|sun)\\s+(?P<b>jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\\s+(?P<d>3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])\\s+(?P<H>2[0-3]|[0-1]\\d|\\d):(?P<M>[0-5]\\d|\\d):(?P<S>6[0-1]|[0-5]\\d|\\d)\\s+(?P<Y>\\d\\d\\d\\d)',
    'd': '(?P<d>3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])',
    'f': '(?P<f>[0-9]{1,9})',
    'j': '(?P<j>36[0-6]|3[0-5]\\d|[1-2]\\d\\d|0[1-9]\\d|00[1-9]|[1-9]\\d|0[1-9]|[1-9])',
    'm': '(?P<m>1[0-2]|0[1-9]|[1-9])',
    'p': '(?P<p>am|pm)',
    'u': '(?P<u>[1-7])',
    'w': '(?P<w>[0-6])',
    'x': '(?P<m>1[0-2]|0[1-9]|[1-9])/(?P<d>3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])/(?P<y>\\d\\d)',
    'y': '(?P<y>\\d\\d)',
    'z': '(?P<z>[+-]\\d\\d:?[0-5]\\d(:?[0-5]\\d(\\.\\d{1,6})?)?|Z)',
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b78ab490>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.strptime', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b78ab490>, origin='/media/Data2/ve39_sharepoint/lib/python3.9/site-packages/pandas/_libs/tslibs/strptime.cpython-39-x86_64-linux-gnu.so')"

__test__ = {}

