# encoding: utf-8
# module pandas._libs.tslibs.dtypes
# from /media/Data2/ve_django4/lib/python3.9/site-packages/pandas/_libs/tslibs/dtypes.cpython-39-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import enum as __enum


# no functions
# classes

class Enum(object):
    """
    Generic enumeration.
    
        Derive from this class to define new enumerations.
    """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initial start value or None
                count: the number of existing members
                last_value: the last value assigned or None
        """
        pass

    @classmethod
    def _missing_(cls, *args, **kwargs): # real signature unknown
        pass

    def __dir__(self): # reliably restored by inspect
        """ Returns all members and all public methods """
        pass

    def __format__(self, format_spec): # reliably restored by inspect
        """ Returns format using actual value type unless __str__ has been overridden. """
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    def __reduce_ex__(self, proto): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    name = None # (!) real value is '<types.DynamicClassAttribute object at 0x7fc5b94fab80>'
    value = None # (!) real value is '<types.DynamicClassAttribute object at 0x7fc5b94fabb0>'
    _member_map_ = {}
    _member_names_ = []
    _member_type_ = object
    _value2member_map_ = {}
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'enum', '__doc__': '\\n    Generic enumeration.\\n\\n    Derive from this class to define new enumerations.\\n    ', '__new__': <staticmethod object at 0x7fc5b94faca0>, '_generate_next_value_': <function Enum._generate_next_value_ at 0x7fc5b95015e0>, '_missing_': <classmethod object at 0x7fc5b94fab50>, '__repr__': <function Enum.__repr__ at 0x7fc5b9501700>, '__str__': <function Enum.__str__ at 0x7fc5b9501790>, '__dir__': <function Enum.__dir__ at 0x7fc5b9501820>, '__format__': <function Enum.__format__ at 0x7fc5b95018b0>, '__hash__': <function Enum.__hash__ at 0x7fc5b9501940>, '__reduce_ex__': <function Enum.__reduce_ex__ at 0x7fc5b95019d0>, 'name': <types.DynamicClassAttribute object at 0x7fc5b94fab80>, 'value': <types.DynamicClassAttribute object at 0x7fc5b94fabb0>, '__dict__': <attribute '__dict__' of 'Enum' objects>, '__weakref__': <attribute '__weakref__' of 'Enum' objects>, '_member_names_': [], '_member_map_': {}, '_member_type_': <class 'object'>, '_value2member_map_': {}})"


class FreqGroup(__enum.Enum):
    """ An enumeration. """
    def get_freq_group(self, *args, **kwargs): # real signature unknown
        pass

    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initial start value or None
                count: the number of existing members
                last_value: the last value assigned or None
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    FR_ANN = None # (!) real value is '<FreqGroup.FR_ANN: 1000>'
    FR_BUS = None # (!) real value is '<FreqGroup.FR_BUS: 5000>'
    FR_DAY = None # (!) real value is '<FreqGroup.FR_DAY: 6000>'
    FR_HR = None # (!) real value is '<FreqGroup.FR_HR: 7000>'
    FR_MIN = None # (!) real value is '<FreqGroup.FR_MIN: 8000>'
    FR_MS = None # (!) real value is '<FreqGroup.FR_MS: 10000>'
    FR_MTH = None # (!) real value is '<FreqGroup.FR_MTH: 3000>'
    FR_NS = None # (!) real value is '<FreqGroup.FR_NS: 12000>'
    FR_QTR = None # (!) real value is '<FreqGroup.FR_QTR: 2000>'
    FR_SEC = None # (!) real value is '<FreqGroup.FR_SEC: 9000>'
    FR_UND = None # (!) real value is '<FreqGroup.FR_UND: -10000>'
    FR_US = None # (!) real value is '<FreqGroup.FR_US: 11000>'
    FR_WK = None # (!) real value is '<FreqGroup.FR_WK: 4000>'
    _member_map_ = {
        'FR_ANN': None, # (!) real value is '<FreqGroup.FR_ANN: 1000>'
        'FR_BUS': None, # (!) real value is '<FreqGroup.FR_BUS: 5000>'
        'FR_DAY': None, # (!) real value is '<FreqGroup.FR_DAY: 6000>'
        'FR_HR': None, # (!) real value is '<FreqGroup.FR_HR: 7000>'
        'FR_MIN': None, # (!) real value is '<FreqGroup.FR_MIN: 8000>'
        'FR_MS': None, # (!) real value is '<FreqGroup.FR_MS: 10000>'
        'FR_MTH': None, # (!) real value is '<FreqGroup.FR_MTH: 3000>'
        'FR_NS': None, # (!) real value is '<FreqGroup.FR_NS: 12000>'
        'FR_QTR': None, # (!) real value is '<FreqGroup.FR_QTR: 2000>'
        'FR_SEC': None, # (!) real value is '<FreqGroup.FR_SEC: 9000>'
        'FR_UND': None, # (!) real value is '<FreqGroup.FR_UND: -10000>'
        'FR_US': None, # (!) real value is '<FreqGroup.FR_US: 11000>'
        'FR_WK': None, # (!) real value is '<FreqGroup.FR_WK: 4000>'
    }
    _member_names_ = [
        'FR_ANN',
        'FR_QTR',
        'FR_MTH',
        'FR_WK',
        'FR_BUS',
        'FR_DAY',
        'FR_HR',
        'FR_MIN',
        'FR_SEC',
        'FR_MS',
        'FR_US',
        'FR_NS',
        'FR_UND',
    ]
    _member_type_ = object
    _value2member_map_ = {
        -10000: None, # (!) real value is '<FreqGroup.FR_UND: -10000>'
        1000: None, # (!) real value is '<FreqGroup.FR_ANN: 1000>'
        2000: None, # (!) real value is '<FreqGroup.FR_QTR: 2000>'
        3000: None, # (!) real value is '<FreqGroup.FR_MTH: 3000>'
        4000: None, # (!) real value is '<FreqGroup.FR_WK: 4000>'
        5000: None, # (!) real value is '<FreqGroup.FR_BUS: 5000>'
        6000: None, # (!) real value is '<FreqGroup.FR_DAY: 6000>'
        7000: None, # (!) real value is '<FreqGroup.FR_HR: 7000>'
        8000: None, # (!) real value is '<FreqGroup.FR_MIN: 8000>'
        9000: None, # (!) real value is '<FreqGroup.FR_SEC: 9000>'
        10000: None, # (!) real value is '<FreqGroup.FR_MS: 10000>'
        11000: None, # (!) real value is '<FreqGroup.FR_US: 11000>'
        12000: None, # (!) real value is '<FreqGroup.FR_NS: 12000>'
    }


class PeriodDtypeBase(object):
    """
    Similar to an actual dtype, this contains all of the information
        describing a PeriodDtype in an integer code.
    """
    @classmethod
    def from_date_offset(cls, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    date_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Corresponding DateOffset object.

        This mapping is mainly for backward-compatibility.
        """

    freq_group_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dtype_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class Resolution(__enum.Enum):
    """ An enumeration. """
    @classmethod
    def from_attrname(cls, second): # real signature unknown; restored from __doc__
        """
        Return resolution str against resolution code.
        
                Examples
                --------
                >>> Resolution.from_attrname('second')
                <Resolution.RESO_SEC: 3>
        
                >>> Resolution.from_attrname('second') == Resolution.RESO_SEC
                True
        """
        pass

    @classmethod
    def from_freq_group(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_reso_from_freq(cls, H): # real signature unknown; restored from __doc__
        """
        Return resolution code against frequency str.
        
                `freq` is given by the `offset.freqstr` for some DateOffset object.
        
                Examples
                --------
                >>> Resolution.get_reso_from_freq('H')
                <Resolution.RESO_HR: 5>
        
                >>> Resolution.get_reso_from_freq('H') == Resolution.RESO_HR
                True
        """
        pass

    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initial start value or None
                count: the number of existing members
                last_value: the last value assigned or None
        """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    attrname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return datetime attribute name corresponding to this Resolution.

        Examples
        --------
        >>> Resolution.RESO_SEC.attrname
        'second'
        """

    freq_group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    RESO_DAY = None # (!) real value is '<Resolution.RESO_DAY: 6>'
    RESO_HR = None # (!) real value is '<Resolution.RESO_HR: 5>'
    RESO_MIN = None # (!) real value is '<Resolution.RESO_MIN: 4>'
    RESO_MS = None # (!) real value is '<Resolution.RESO_MS: 2>'
    RESO_MTH = None # (!) real value is '<Resolution.RESO_MTH: 7>'
    RESO_NS = None # (!) real value is '<Resolution.RESO_NS: 0>'
    RESO_QTR = None # (!) real value is '<Resolution.RESO_QTR: 8>'
    RESO_SEC = None # (!) real value is '<Resolution.RESO_SEC: 3>'
    RESO_US = None # (!) real value is '<Resolution.RESO_US: 1>'
    RESO_YR = None # (!) real value is '<Resolution.RESO_YR: 9>'
    _member_map_ = {
        'RESO_DAY': None, # (!) real value is '<Resolution.RESO_DAY: 6>'
        'RESO_HR': None, # (!) real value is '<Resolution.RESO_HR: 5>'
        'RESO_MIN': None, # (!) real value is '<Resolution.RESO_MIN: 4>'
        'RESO_MS': None, # (!) real value is '<Resolution.RESO_MS: 2>'
        'RESO_MTH': None, # (!) real value is '<Resolution.RESO_MTH: 7>'
        'RESO_NS': None, # (!) real value is '<Resolution.RESO_NS: 0>'
        'RESO_QTR': None, # (!) real value is '<Resolution.RESO_QTR: 8>'
        'RESO_SEC': None, # (!) real value is '<Resolution.RESO_SEC: 3>'
        'RESO_US': None, # (!) real value is '<Resolution.RESO_US: 1>'
        'RESO_YR': None, # (!) real value is '<Resolution.RESO_YR: 9>'
    }
    _member_names_ = [
        'RESO_NS',
        'RESO_US',
        'RESO_MS',
        'RESO_SEC',
        'RESO_MIN',
        'RESO_HR',
        'RESO_DAY',
        'RESO_MTH',
        'RESO_QTR',
        'RESO_YR',
    ]
    _member_type_ = object
    _value2member_map_ = {
        0: None, # (!) real value is '<Resolution.RESO_NS: 0>'
        1: None, # (!) real value is '<Resolution.RESO_US: 1>'
        2: None, # (!) real value is '<Resolution.RESO_MS: 2>'
        3: None, # (!) real value is '<Resolution.RESO_SEC: 3>'
        4: None, # (!) real value is '<Resolution.RESO_MIN: 4>'
        5: None, # (!) real value is '<Resolution.RESO_HR: 5>'
        6: None, # (!) real value is '<Resolution.RESO_DAY: 6>'
        7: None, # (!) real value is '<Resolution.RESO_MTH: 7>'
        8: None, # (!) real value is '<Resolution.RESO_QTR: 8>'
        9: None, # (!) real value is '<Resolution.RESO_YR: 9>'
    }


# variables with complex values

_attrname_to_abbrevs = {
    'day': 'D',
    'hour': 'H',
    'microsecond': 'U',
    'millisecond': 'L',
    'minute': 'T',
    'month': 'M',
    'nanosecond': 'N',
    'quarter': 'Q',
    'second': 'S',
    'year': 'A',
}

_period_code_map = {
    'A': 1000,
    'A-APR': 1004,
    'A-AUG': 1008,
    'A-DEC': 1000,
    'A-FEB': 1002,
    'A-JAN': 1001,
    'A-JUL': 1007,
    'A-JUN': 1006,
    'A-MAR': 1003,
    'A-MAY': 1005,
    'A-NOV': 1011,
    'A-OCT': 1010,
    'A-SEP': 1009,
    'B': 5000,
    'C': 5000,
    'D': 6000,
    'H': 7000,
    'L': 10000,
    'M': 3000,
    'N': 12000,
    'Q': 2000,
    'Q-APR': 2004,
    'Q-AUG': 2008,
    'Q-DEC': 2000,
    'Q-FEB': 2002,
    'Q-JAN': 2001,
    'Q-JUL': 2007,
    'Q-JUN': 2006,
    'Q-MAR': 2003,
    'Q-MAY': 2005,
    'Q-NOV': 2011,
    'Q-OCT': 2010,
    'Q-SEP': 2009,
    'S': 9000,
    'T': 8000,
    'U': 11000,
    'W': 4000,
    'W-FRI': 4005,
    'W-MON': 4001,
    'W-SAT': 4006,
    'W-SUN': 4000,
    'W-THU': 4004,
    'W-TUE': 4002,
    'W-WED': 4003,
    'Y-APR': 1004,
    'Y-AUG': 1008,
    'Y-DEC': 1000,
    'Y-FEB': 1002,
    'Y-JAN': 1001,
    'Y-JUL': 1007,
    'Y-JUN': 1006,
    'Y-MAR': 1003,
    'Y-MAY': 1005,
    'Y-NOV': 1011,
    'Y-OCT': 1010,
    'Y-SEP': 1009,
}

_reverse_period_code_map = {
    1000: 'A-DEC',
    1001: 'A-JAN',
    1002: 'A-FEB',
    1003: 'A-MAR',
    1004: 'A-APR',
    1005: 'A-MAY',
    1006: 'A-JUN',
    1007: 'A-JUL',
    1008: 'A-AUG',
    1009: 'A-SEP',
    1010: 'A-OCT',
    1011: 'A-NOV',
    2000: 'Q-DEC',
    2001: 'Q-JAN',
    2002: 'Q-FEB',
    2003: 'Q-MAR',
    2004: 'Q-APR',
    2005: 'Q-MAY',
    2006: 'Q-JUN',
    2007: 'Q-JUL',
    2008: 'Q-AUG',
    2009: 'Q-SEP',
    2010: 'Q-OCT',
    2011: 'Q-NOV',
    3000: 'M',
    4000: 'W-SUN',
    4001: 'W-MON',
    4002: 'W-TUE',
    4003: 'W-WED',
    4004: 'W-THU',
    4005: 'W-FRI',
    4006: 'W-SAT',
    5000: 'B',
    6000: 'D',
    7000: 'H',
    8000: 'T',
    9000: 'S',
    10000: 'L',
    11000: 'U',
    12000: 'N',
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b7d26f10>'

__pyx_capi__ = {
    'attrname_to_abbrevs': None, # (!) real value is '<capsule object "PyObject *" at 0x7fc5b7d26ed0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.dtypes', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b7d26f10>, origin='/media/Data2/ve39_sharepoint/lib/python3.9/site-packages/pandas/_libs/tslibs/dtypes.cpython-39-x86_64-linux-gnu.so')"

__test__ = {
    'Resolution.attrname (line 211)': "\n        Return datetime attribute name corresponding to this Resolution.\n\n        Examples\n        --------\n        >>> Resolution.RESO_SEC.attrname\n        'second'\n        ",
    'Resolution.from_attrname (line 223)': "\n        Return resolution str against resolution code.\n\n        Examples\n        --------\n        >>> Resolution.from_attrname('second')\n        <Resolution.RESO_SEC: 3>\n\n        >>> Resolution.from_attrname('second') == Resolution.RESO_SEC\n        True\n        ",
    'Resolution.get_reso_from_freq (line 238)': "\n        Return resolution code against frequency str.\n\n        `freq` is given by the `offset.freqstr` for some DateOffset object.\n\n        Examples\n        --------\n        >>> Resolution.get_reso_from_freq('H')\n        <Resolution.RESO_HR: 5>\n\n        >>> Resolution.get_reso_from_freq('H') == Resolution.RESO_HR\n        True\n        ",
}

