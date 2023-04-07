from typing import Any

from ... import types as sqltypes

class RangeOperators:
    class comparator_factory(sqltypes.Concatenable.Comparator):
        def __ne__(self, other: Any) -> Any: ...
        def contains(self, other: Any, **kw: Any): ...
        def contained_by(self, other: Any): ...
        def overlaps(self, other: Any): ...
        def strictly_left_of(self, other: Any): ...
        __lshift__: Any = ...
        def strictly_right_of(self, other: Any): ...
        __rshift__: Any = ...
        def not_extend_right_of(self, other: Any): ...
        def not_extend_left_of(self, other: Any): ...
        def adjacent_to(self, other: Any): ...
        def __add__(self, other: Any): ...

class INT4RANGE(RangeOperators, sqltypes.TypeEngine): ...
class INT8RANGE(RangeOperators, sqltypes.TypeEngine): ...
class NUMRANGE(RangeOperators, sqltypes.TypeEngine): ...
class DATERANGE(RangeOperators, sqltypes.TypeEngine): ...
class TSRANGE(RangeOperators, sqltypes.TypeEngine): ...
class TSTZRANGE(RangeOperators, sqltypes.TypeEngine): ...