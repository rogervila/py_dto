#!/usr/bin/env python

import abc
from typing import get_type_hints, Any


class DTO(abc.ABC):
    def __init__(self, data: dict):
        hints = get_type_hints(self)

        for key, value in data.items():
            try:
                if hints[key] != Any and hints[key] != type(value):
                    raise TypeError

                setattr(self, key, value)

            except KeyError as e:
                raise ValueError from e
