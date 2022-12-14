# encoding: utf-8
# module pandas._libs.hashtable
# from /media/Data2/ve_django4/lib/python3.9/site-packages/pandas/_libs/hashtable.cpython-39-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /media/Data2/ve39_sharepoint/lib/python3.9/site-packages/numpy/__init__.py

from .Factorizer import Factorizer

class ObjectFactorizer(Factorizer):
    # no doc
    def factorize(self, np_array, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Returns
                -------
                np.ndarray[np.intp]
        
                Examples
                --------
                Factorize values with nans replaced by na_sentinel
        
                >>> fac = ObjectFactorizer(3)
                >>> fac.factorize(np.array([1,2,np.nan], dtype='O'), na_sentinel=20)
                array([ 0,  1, 20])
        """
        pass

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

    table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uniques = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



