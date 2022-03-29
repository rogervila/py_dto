#!/usr/bin/env python

from abc import ABC
from typing import Any, Optional, get_type_hints
from runtype import isa


class DTO(ABC):
    def __init__(self, data: dict, allows_missing_keys: bool = False):
        self._assert(data, dict)
        self._assert(allows_missing_keys, bool)

        hints = get_type_hints(self)

        if not allows_missing_keys:
            self._raise_missing_hints(data, hints)

        self._set_attributes(data, hints)

    def _set_attributes(self, data: dict, hints: dict) -> None:
        for key, value in data.items():
            try:
                self._assert(value, hints[key], key)
                setattr(self, key, value)

            except KeyError as e:
                raise ValueError from e

    def _raise_missing_hints(self, data: dict, hints: dict) -> None:
        for hint in hints.keys():
            if hint not in data.keys():
                raise KeyError(hint)

    def _assert(self, value: Any, expected_type: Any, exception_arguments: Optional[Any] = None) -> None:
        if not isa(value, expected_type):
            raise TypeError(
                value if expected_type is None else exception_arguments
            )
