from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Tuple, Union


@dataclass(frozen=True)
class Wei:
    wei_value: int
    unit: str = "wei"
    wei_factor: int = 1

    def __init__(self, value: Union[str, None] = None, wei: Union[int, None] = None):
        assert not (value is not None and wei is not None), "Only one of value or wei must be provided"
        assert value is not None or wei is not None, "One of value or wei must be provided"
        if value:
            assert isinstance(value, str), f"{value} is not a string, other types may not be precise enough"
            wei_value = Decimal(value) * self.wei_factor
            assert wei_value.as_integer_ratio()[1] == 1, f"{wei} is not an integer"
            wei = int(wei_value)
        assert isinstance(wei, int), f"{wei} is not an integer"
        object.__setattr__(self, "wei_value", int(wei))

    def __repr__(self) -> str:
        value = format(Decimal(self.wei_value) / self.wei_factor, "f")
        return f"{value} {self.unit}"

    @property
    def value(self) -> Decimal:
        return Decimal(self.wei_value) / self.wei_factor

    @property
    def wei(self) -> Wei:
        return Wei(wei=self.wei_value)

    @property
    def gwei(self) -> Gwei:
        return Gwei(wei=self.wei_value)

    @property
    def ether(self) -> Ether:
        return Ether(wei=self.wei_value)

    @property
    def eth(self) -> Ether:
        return Ether(wei=self.wei_value)

    def _add(self, x: Wei) -> Wei:
        assert isinstance(x, Wei), f"{x} is not a Wei"
        return self.__class__(wei=self.wei_value + x.wei_value)

    __add__ = _add
    __radd__ = _add

    def _sub(self, x: Wei) -> Wei:
        assert isinstance(x, Wei), f"{x} is not a Wei"
        return self.__class__(wei=self.wei_value - x.wei_value)

    __sub__ = lambda self, x: self._sub(x)
    __rsub__ = lambda self, x: -self._sub(x)

    def _mul(self, x: int) -> Wei:
        assert isinstance(x, int), f"{x} is not an integer"
        return self.__class__(wei=self.wei_value * x)

    __mul__ = _mul
    __rmul__ = _mul

    def __truediv__(self, x: Union[Wei, int]) -> Union[Wei, int]:
        quotient, _ = divmod(self, x)
        return quotient

    def __eq__(self, x: object) -> bool:
        assert isinstance(x, Wei), f"{x} is not a Wei, can't compare"
        return self.wei_value == x.wei_value

    def __lt__(self, x: Wei) -> bool:
        assert isinstance(x, Wei), f"{x} is not a Wei, can't compare"
        return self.wei_value < x.wei_value

    def __divmod__(self, x: Union[Wei, int]) -> Tuple[Union[Wei, int], Wei]:
        if isinstance(x, Wei):
            quotient, remainder = divmod(self.wei_value, x.wei_value)
            return quotient, self.__class__(wei=remainder)
        elif isinstance(x, int):
            quotient, remainder = divmod(self.wei_value, x)
            return self.__class__(wei=quotient), self.__class__(wei=remainder)
        else:
            raise TypeError(f"{x} is not a Wei or an integer")

    def __mod__(self, x: Union[Wei, int]) -> Wei:
        _, remainder = divmod(self, x)
        return remainder


class Gwei(Wei):
    unit: str = "gwei"
    wei_factor: int = 1000000000


class Ether(Wei):
    unit: str = "ether"
    wei_factor: int = 1000000000000000000


Eth = Ether


def E(value: str) -> Wei:
    value = value.lower()
    if value.endswith("gwei"):
        return Gwei(value[:-4])
    elif value.endswith("wei"):
        return Wei(value[:-3])
    elif value.endswith("ether"):
        return Ether(value[:-5])
    elif value.endswith("eth"):
        return Ether(value[:-3])
    else:
        raise ValueError(f"{value} is not a valid Wei value")
