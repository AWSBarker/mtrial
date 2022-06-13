# encoding: utf-8
# module pandas._libs.ops
# from /media/Data2/ve_django4/lib/python3.9/site-packages/pandas/_libs/ops.cpython-39-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import operator as operator # /usr/lib/python3.9/operator.py
import numpy as np # /media/Data2/ve39_sharepoint/lib/python3.9/site-packages/numpy/__init__.py

# functions

def maybe_convert_bool(*args, **kwargs): # real signature unknown
    pass

def scalar_binop(*args, **kwargs): # real signature unknown
    """
    Apply the given binary operator `op` between each element of the array
        `values` and the scalar `val`.
    
        Parameters
        ----------
        values : ndarray[object]
        val : object
        op : binary operator
    
        Returns
        -------
        result : ndarray[object]
    """
    pass

def scalar_compare(*args, **kwargs): # real signature unknown
    """
    Compare each element of `values` array with the scalar `val`, with
        the comparison operation described by `op`.
    
        Parameters
        ----------
        values : ndarray[object]
        val : object
        op : {operator.eq, operator.ne,
              operator.le, operator.lt,
              operator.ge, operator.gt}
    
        Returns
        -------
        result : ndarray[bool]
    """
    pass

def vec_binop(*args, **kwargs): # real signature unknown
    """
    Apply the given binary operator `op` pointwise to the elements of
        arrays `left` and `right`.
    
        Parameters
        ----------
        left : ndarray[object]
        right : ndarray[object]
        op : binary operator
    
        Returns
        -------
        result : ndarray[object]
    """
    pass

def vec_compare(*args, **kwargs): # real signature unknown
    """
    Compare the elements of `left` with the elements of `right` pointwise,
        with the comparison operation described by `op`.
    
        Parameters
        ----------
        left : ndarray[object]
        right : ndarray[object]
        op : {operator.eq, operator.ne,
              operator.le, operator.lt,
              operator.ge, operator.gt}
    
        Returns
        -------
        result : ndarray[bool]
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b6fdaaf0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.ops', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc5b6fdaaf0>, origin='/media/Data2/ve39_sharepoint/lib/python3.9/site-packages/pandas/_libs/ops.cpython-39-x86_64-linux-gnu.so')"

__test__ = {}

