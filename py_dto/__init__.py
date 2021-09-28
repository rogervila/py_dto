#!/usr/bin/env python

import abc
from typing import get_type_hints
from runtype import isa


class DTO(abc.ABC):
    def __init__(self, data: dict, allows_nones: bool = False, allows_missing_keys: bool = False):
        hints = get_type_hints(self)

        if not allows_missing_keys:
            for key in hints.keys():
                if key not in data.keys():
                    raise KeyError(key)

        for key, value in data.items():
            try:
                if isa(value, hints[key]) or (allows_nones and value is None):
                    setattr(self, key, value)
                    continue

                raise TypeError(key)

            except KeyError as e:
                raise ValueError from e
