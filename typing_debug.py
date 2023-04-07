from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import RelationshipProperty

# pyright: strict
# pyright: reportImplicitOverride=true


if TYPE_CHECKING:
    X = int
else:

    class X(
        RelationshipProperty
    ):  # RelationshipProperty: Type[RelationshipProperty[Unknown]]
        ...


def f():  # Method "f" is not marked as override but is overriding a method in class "Unknown"
    ...
