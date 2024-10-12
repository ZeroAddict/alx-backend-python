#!/usr/bin/env python3
"""
More type annotations
Add type annotations to function safely_get_value
"""
from typing import Sequence, Union, Any, TypeVar, Mapping

R = TypeVar('X')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[X, None] = None) -> Union[Any, X]:
    """
    Add type annotations to function
    safely_get_value
    """
    if key in dct:
        return dct[key]
    else:
        return default
