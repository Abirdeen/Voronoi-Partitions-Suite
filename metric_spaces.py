from collections.abc import (
    Iterable
)
from typing import (
    Any,
    TypeVar,
    TypeAlias,
    Generic
)
from abc import (
    ABC,
    abstractmethod
)

import math
import numpy as np

PointType = TypeVar('PointType')

class MetricSpace(ABC, Generic[PointType]):
    '''Helper class that provides a standard way to construct a metric space using inheritance.
    '''
    def __init__(self):
        raise NotImplementedError
    
    @abstractmethod
    def distance(self, point1, point2) -> float:
        raise NotImplementedError
    
    def nearest_neighbours(self, points: Iterable[PointType], givenPoint: PointType, k: int) -> Iterable[PointType]:
        '''Find the `k` nearest neighbours of a given point.
        
        Parameters
        ----------
        points: Iterable[PointType]
            Iterable of points in space.
        givenPoint : PointType
            Single point in space, whose nearest neighbours you want to find.
        k : int
            Number of nearest neighbours to find.
        
        Returns
        -------
        Iterable[PointType]
            The `k` nearest neighbours of `givenPoint`.
            
        Examples
        --------
        >>> ???
        
        '''
        raise NotImplementedError

if __name__ == '__main__':

    pass