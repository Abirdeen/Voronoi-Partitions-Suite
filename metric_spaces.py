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


RealPoint: TypeAlias = np.ndarray[Any, np.dtype[np.float64]]
  
class EuclideanRealSpace(MetricSpace):
    '''Metric space class representing n-dimensional Euclidean real space.
    
    Parameters
    ----------
    dimension : int, default=2
        The dimension of the space, which should be positive. `dimension=1` gives 
        the real line, while `dimension=2` gives the plane.
    '''
    def __init__(self, dimension: int = 2):
        return None
    
    def distance(self, point1: RealPoint, 
                 point2: RealPoint) -> float:
        '''Compute the Euclidean distance between two points.
        
        Parameters
        ----------
        point1, point2 : RealPoint
            Points in Euclidean space, given by numpy arrays of floats.
        
        Returns
        -------
        distance : float
            A float representing the Euclidean distance between the given points.

        Examples
        --------
        >>> point1 = np.array([0,1])
        ... point2 = np.array([1,1])
        ... EuclideanRealSpace(2).distance(point1, point2)
        1.0

        >>> point1 = np.array([0,0,0,0])
        ... point2 = np.array([0.5,0.5,0.5,0.5])
        ... EuclideanRealSpace(4).distance(point1, point2)
        1.0
        '''
        distance=math.sqrt(np.sum((point1-point2)**2))
        return distance
   
 
if __name__ == '__main__':

    pass