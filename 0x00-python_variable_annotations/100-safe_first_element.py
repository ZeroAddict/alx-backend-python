#!/usr/bin/env python3
"""
Duck typing - returns first element of a sequence
Augument code with correct duck-typed annotations
"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Duck-typed function
    uses typing module and Union,Any,Sequence
    safe_first_element
    """
    if lst:
        return lst[0]
    else:
        return None
