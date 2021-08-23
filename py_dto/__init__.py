#!/usr/bin/env python

import abc
from typing import get_type_hints, Any


class DTO(abc.ABC):
    def __init__(self, data: dict, allows_nones: bool = False):
        hints = get_type_hints(self)

        for key, value in data.items():
            try:
                if hints[key] == Any or hints[key] == type(value) or (allows_nones and value is None):
                    setattr(self, key, value)
                    continue

                raise TypeError(key)

            except KeyError as e:
                raise ValueError from e
