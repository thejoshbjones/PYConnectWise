from __future__ import annotations
from enum import Enum
from datetime import datetime
from typing import Any


class ValueType(Enum):
    STR = 1
    INT = 2
    DATETIME = 3


class Condition:
    def __init__(self):
        self._condition_string: str = ""

    def __add_to_string(self, addition: str):
        self._condition_string += str(addition) + " "

    def __add_typed_value_to_string(self, value, type: ValueType):
        if type == ValueType.STR:
            self.__add_to_string('"*' + str(value) + '*"')
        elif type == ValueType.INT:
            self.__add_to_string(str(value))
        elif type == ValueType.DATETIME:
            self.__add_to_string("[" + str(value) + "]")

        return self

    def __infer_value_type(self, value: Any):
        if isinstance(value, int) or isinstance(value, float):
            return ValueType.INT
        elif isinstance(value, datetime):
            return ValueType.DATETIME
        else:
            return ValueType.STR

    def field(self, field_name: str):
        self.__add_to_string(field_name)
        return self

    def nest(self, condition: Condition):
        self.__add_to_string("(" + condition + ")")
        return self

    def c_and(self):
        if len(self._condition_string) != 0 and self._condition_string != None:
            self.__add_to_string("AND")
        return self

    def iand(self):
        return self.c_and()

    def c_or(self):
        if len(self._condition_string) != 0 and self._condition_string != None:
            self.__add_to_string("OR")
        return self

    def ior(self):
        return self.c_or()

    def c_like(self, comparison: Any, type: ValueType = None):
        self.__add_to_string("LIKE")
        if type is None:
            type = self.__infer_value_type(comparison)
        self.__add_typed_value_to_string(comparison, type)
        return self

    def ilike(self, comparison: Any, type: ValueType = None):
        return self.c_like(comparison, type)

    def c_is(self, comparison: Any, type: ValueType = None):
        self.__add_to_string("IS")
        if type is None:
            type = self.__infer_value_type(comparison)
        self.__add_typed_value_to_string(comparison, type)
        return self

    def iis(self, comparison: Any, type: ValueType = None):
        return self.c_is(comparison, type)

    def c_greater_than(self, comparison: Any, type: ValueType = None):
        self.__add_to_string(">")
        if type is None:
            type = self.__infer_value_type(comparison)
        self.__add_typed_value_to_string(comparison, type)
        return self

    def gt(self, comparison: Any, type: ValueType = None):
        return self.c_greater_than(comparison, type)

    def c_greater_or_equal(self, comparison: Any, type: ValueType = None):
        self.__add_to_string(">=")
        if type is None:
            type = self.__infer_value_type(comparison)
        self.__add_typed_value_to_string(comparison, type)
        return self

    def gte(self, comparison: Any, type: ValueType = None):
        return self.c_greater_or_equal(comparison, type)

    def c_lessthan(self, comparison: Any, type: ValueType = None):
        self.__add_to_string("<")
        if type is None:
            type = self.__infer_value_type(comparison)
        self.__add_typed_value_to_string(comparison, type)
        return self

    def lt(self, comparison: Any, type: ValueType = None):
        return self.c_lessthan(comparison, type)

    def c_lesser_or_equal(self, comparison: Any, type: ValueType = None):
        self.__add_to_string("<=")
        if type is None:
            type = self.__infer_value_type(comparison)
        self.__add_typed_value_to_string(comparison, type)
        return self

    def lte(self, comparison: Any, type: ValueType = None):
        return self.c_lesser_or_equal(comparison, type)

    def c_equals(self, comparison: Any, type: ValueType = None):
        self.__add_to_string("=")
        if type is None:
            type = self.__infer_value_type(comparison)
        self.__add_typed_value_to_string(comparison, type)
        return self

    def eq(self, comparison: Any, type: ValueType = None):
        return self.c_equals(comparison, type)

    def __str__(self) -> str:
        return self._condition_string.strip()
