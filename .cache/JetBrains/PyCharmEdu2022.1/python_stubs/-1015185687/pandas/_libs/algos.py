# encoding: utf-8
# module pandas._libs.algos
# from /media/Data2/ve_django4/lib/python3.9/site-packages/pandas/_libs/algos.cpython-39-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /media/Data2/ve39_sharepoint/lib/python3.9/site-packages/numpy/__init__.py
import pandas._libs.missing as missing # /media/Data2/ve39_sharepoint/lib/python3.9/site-packages/pandas/_libs/missing.cpython-39-x86_64-linux-gnu.so

# functions

def backfill(*args, **kwargs): # real signature unknown
    pass

def backfill_2d_inplace(*args, **kwargs): # real signature unknown
    pass

def backfill_inplace(*args, **kwargs): # real signature unknown
    pass

def diff_2d(*args, **kwargs): # real signature unknown
    pass

def ensure_float64(*args, **kwargs): # real signature unknown
    pass

def ensure_int16(*args, **kwargs): # real signature unknown
    pass

def ensure_int32(*args, **kwargs): # real signature unknown
    pass

def ensure_int64(*args, **kwargs): # real signature unknown
    pass

def ensure_int8(*args, **kwargs): # real signature unknown
    pass

def ensure_object(*args, **kwargs): # real signature unknown
    pass

def ensure_platform_int(*args, **kwargs): # real signature unknown
    pass

def groupsort_indexer(*args, **kwargs): # real signature unknown
    """
    Compute a 1-d indexer.
    
        The indexer is an ordering of the passed index,
        ordered by the groups.
    
        Parameters
        ----------
        index: np.ndarray[np.intp]
            Mappings from group -> position.
        ngroups: int64
            Number of groups.
    
        Returns
        -------
        ndarray[intp_t, ndim=1]
            Indexer
        ndarray[intp_t, ndim=1]
            Group Counts
    
        Notes
        -----
        This is a reverse of the label factorization process.
    """
    pass

def is_lexsorted(*args, **kwargs): # real signature unknown
    pass

def is_monotonic(*args, **kwargs): # real signature unknown
    """
    Returns
        -------
        tuple
            is_monotonic_inc : bool
            is_monotonic_dec : bool
            is_unique : bool
    """
    pass

def kth_smallest(*args, **kwargs): # real signature unknown
    """
    Compute the kth smallest value in arr. Note that the input
        array will be modified.
    
        Parameters
        ----------
        arr : numeric[::1]
            Array to compute the kth smallest value for, must be
            contiguous
        k : Py_ssize_t
    
        Returns
        -------
        numeric
            The kth smallest value in arr
    """
    pass

def nancorr(*args, **kwargs): # real signature unknown
    pass

def nancorr_spearman(*args, **kwargs): # real signature unknown
    pass

def pad(*args, **kwargs): # real signature unknown
    pass

def pad_2d_inplace(*args, **kwargs): # real signature unknown
    pass

def pad_inplace(*args, **kwargs): # real signature unknown
    pass

def rank_1d(*args, **kwargs): # real signature unknown
    """
    Fast NaN-friendly version of ``scipy.stats.rankdata``.
    
        Parameters
        ----------
        values : array of iu_64_floating_obj_t values to be ranked
        labels : np.ndarray[np.intp] or None
            Array containing unique label for each group, with its ordering
            matching up to the corresponding record in `values`. If not called
            from a groupby operation, will be None.
        is_datetimelike : bool, default False
            True if `values` contains datetime-like entries.
        ties_method : {'average', 'min', 'max', 'first', 'dense'}, default
            'average'
            * average: average rank of group
            * min: lowest rank in group
            * max: highest rank in group
            * first: ranks assigned in order they appear in the array
            * dense: like 'min', but rank always increases by 1 between groups
        ascending : bool, default True
            False for ranks by high (1) to low (N)
            na_option : {'keep', 'top', 'bottom'}, default 'keep'
        pct : bool, default False
            Compute percentage rank of data within each group
        na_option : {'keep', 'top', 'bottom'}, default 'keep'
            * keep: leave NA values where they are
            * top: smallest rank if ascending
            * bottom: smallest rank if descending
    """
    pass

def rank_2d(*args, **kwargs): # real signature unknown
    """ Fast NaN-friendly version of ``scipy.stats.rankdata``. """
    pass

def take_1d_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_1d_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_1d_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_1d_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_1d_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_1d_object_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_object_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_object_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_object_object(*args, **kwargs): # real signature unknown
    pass

def unique_deltas(*args, **kwargs): # real signature unknown
    """
    Efficiently find the unique first-differences of the given array.
    
        Parameters
        ----------
        arr : ndarray[int64_t]
    
        Returns
        -------
        ndarray[int64_t]
            An ordered ndarray[int64_t]
    """
    pass

def validate_limit(*args, **kwargs): # real signature unknown
    """
    Check that the `limit` argument is a positive integer.
    
        Parameters
        ----------
        nobs : int
        limit : object
    
        Returns
        -------
        int
            The limit.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class Infinity(object):
    """ Provide a positive Infinity comparison method for ranking. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pandas._libs.algos', '__doc__': '\\n    Provide a positive Infinity comparison method for ranking.\\n    ', '__lt__': <cyfunction Infinity.<lambda> at 0x7fc5b737a2b0>, '__le__': <cyfunction Infinity.<lambda> at 0x7fc5b737a380>, '__eq__': <cyfunction Infinity.<lambda> at 0x7fc5b737a450>, '__ne__': <cyfunction Infinity.<lambda> at 0x7fc5b737a520>, '__gt__': <cyfunction Infinity.<lambda> at 0x7fc5b737a5f0>, '__ge__': <cyfunction Infinity.<lambda> at 0x7fc5b737a6c0>, '__dict__': <attribute '__dict__' of 'Infinity' objects>, '__weakref__': <attribute '__weakref__' of 'Infinity' objects>, '__hash__': None})"
    __hash__ = None


class NegInfinity(object):
    """ Provide a negative Infinity comparison method for ranking. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pandas._libs.algos', '__doc__': '\\n    Provide a negative Infinity comparison method for ranking.\\n    ', '__lt__': <cyfunction NegInfinity.<lambda> at 0x7fc5b737a790>, '__le__': <cyfunction NegInfinity.<lambda> at 0x7fc5b737a860>, '__eq__': <cyfunction NegInfinity.<lambda> at 0x7fc5b737a930>, '__ne__': <cyfunction NegInfinity.<lambda> at 0x7fc5b737aa00>, '__gt__': <cyfunction NegInfinity.<lambda> at 0x7fc5b737aad0>, '__ge__': <cyfunction NegInfinity.<lambda> at 0x7fc5b737aba0>, '__dict__': <attribute '__dict__' of 'NegInfinity' objects>, '__weakref__': <attribute '__weakref__' of 'NegInfinity' objects>, '__hash__': None})"
    __hash__ = None


# variables with complex values

tiebreakers = {
    'average': 0,
    'dense': 5,
    'first': 3,
    'max': 2,
    'min': 1,
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b74b5820>'

__pyx_capi__ = {
    '__pyx_fuse_0kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int8_t (__pyx_t_5numpy_int8_t *, Py_ssize_t, Py_ssize_t)" at 0x7fc5b74b5ab0>'
    '__pyx_fuse_1kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int16_t (__pyx_t_5numpy_int16_t *, Py_ssize_t, Py_ssize_t)" at 0x7fc5b74b5ae0>'
    '__pyx_fuse_2kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int32_t (__pyx_t_5numpy_int32_t *, Py_ssize_t, Py_ssize_t)" at 0x7fc5b74b5b10>'
    '__pyx_fuse_3kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (__pyx_t_5numpy_int64_t *, Py_ssize_t, Py_ssize_t)" at 0x7fc5b74b5b40>'
    '__pyx_fuse_4kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_uint8_t (__pyx_t_5numpy_uint8_t *, Py_ssize_t, Py_ssize_t)" at 0x7fc5b74b5b70>'
    '__pyx_fuse_5kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_uint16_t (__pyx_t_5numpy_uint16_t *, Py_ssize_t, Py_ssize_t)" at 0x7fc5b74b5ba0>'
    '__pyx_fuse_6kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_uint32_t (__pyx_t_5numpy_uint32_t *, Py_ssize_t, Py_ssize_t)" at 0x7fc5b74b5bd0>'
    '__pyx_fuse_7kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_uint64_t (__pyx_t_5numpy_uint64_t *, Py_ssize_t, Py_ssize_t)" at 0x7fc5b74b5c00>'
    '__pyx_fuse_8kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float32_t (__pyx_t_5numpy_float32_t *, Py_ssize_t, Py_ssize_t)" at 0x7fc5b74b5c30>'
    '__pyx_fuse_9kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float64_t (__pyx_t_5numpy_float64_t *, Py_ssize_t, Py_ssize_t)" at 0x7fc5b74b5c60>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.algos', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b74b5820>, origin='/media/Data2/ve39_sharepoint/lib/python3.9/site-packages/pandas/_libs/algos.cpython-39-x86_64-linux-gnu.so')"

__test__ = {}

