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
 
if __name__ == '__main__':

    pass