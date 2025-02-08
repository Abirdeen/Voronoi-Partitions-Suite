from typing import (
    Any,
    TypeVar,
    TypeAlias,
    Generic,
    Callable
)

import numpy as np
import math

RealPoint: TypeAlias = np.ndarray[Any, np.dtype[np.float64]]
RealMetric: TypeAlias = Callable[[RealPoint, RealPoint], float]

def euclidean_metric(point1: RealPoint, 
                     point2: RealPoint) -> float:
    '''Compute the Euclidean distance between two points.
    
    Parameters
    ----------
    point1, point2 : RealPoint
        Points in real space, given by numpy arrays of floats.
    
    Returns
    -------
    distance : float
        A float representing the Euclidean distance between the given points.

    Examples
    --------
    >>> point1 = np.array([0,1])
    ... point2 = np.array([1,1])
    ... euclidean_metric(point1, point2)
    1.0

    >>> point1 = np.array([0,0,0,0])
    ... point2 = np.array([0.5,0.5,0.5,0.5])
    ... euclidean_metric(point1, point2)
    1.0
    '''
    distance=math.sqrt(np.sum((point1-point2)**2))
    return distance

def manhattan_metric(point1: RealPoint, 
                     point2: RealPoint) -> float:
    '''Compute the Manhattan distance between two points.
    
    Parameters
    ----------
    point1, point2 : RealPoint
        Points in real space, given by numpy arrays of floats.
    
    Returns
    -------
    distance : float
        A float representing the Manhattan distance between the given points.

    Examples
    --------
    >>> point1 = np.array([0,1])
    ... point2 = np.array([1,1])
    ... manhattan_metric(point1, point2)
    1.0

    >>> point1 = np.array([0,0,0,0])
    ... point2 = np.array([0.5,0.5,0.5,0.5])
    ... manhattan_metric(point1, point2)
    2.0
    '''
    distance=np.sum(np.abs(point1-point2))
    return distance
