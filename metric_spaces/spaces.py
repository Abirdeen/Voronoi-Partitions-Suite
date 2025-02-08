from collections.abc import (
    Iterable
)
from typing import (
    Any,
    TypeVar,
    TypeAlias,
    Generic,
    Callable
)
from abc import (
    ABC,
    abstractmethod
)

import math
import numpy as np

from metrics.realmetrics import 

PointType = TypeVar('PointType')
Metric: TypeAlias = Callable[[PointType, PointType], float]

class MetricSpace(ABC, Generic[PointType]):
    '''Helper class that provides a standard way to construct a metric space using inheritance.

    Generics
    --------
    PointType : Any
        The type of points in the metric space. For example, this might be an array of floats 
        for real space.

    Parameters
    ----------
    metric : Metric
        A metric in the sense of `metric spaces <https://en.wikipedia.org/wiki/Metric_space>`__. 
        This should take in a pair of points and return a non-negative float, with value zero 
        exactly if both points are the same.
    '''
    def __init__(self, metric: Metric):
        self.distance = metric
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
  
class RealSpace(MetricSpace[RealPoint]):
    '''Metric space class representing n-dimensional real space.
    
    Parameters
    ----------
    dimension : int, default=2
        The dimension of the space, which should be positive. `dimension=1` gives 
        a real line, while `dimension=2` gives a plane.
    
    '''
    def __init__(self, metric: RealMetric, dimension: int = 2):
        return None

if __name__ == '__main__':
    point1 = np.array([2,0,0,0])
    point2 = np.array([0.5,0.5,0.5,0.5])
    print(np.abs(point1-point2))
    pass