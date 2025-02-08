from typing import (
    TypeVar,
    TypeAlias,
    Callable
)

PointType = TypeVar('PointType')
Metric: TypeAlias = Callable[[PointType, PointType], float]