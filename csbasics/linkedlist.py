"""An uncomplicated implementation of single-linked lists."""
from __future__ import annotations

from itertools import chain
from typing import List, Optional, Union, Iterator, Reversible, Final, Any

from csbasics.datastructure import DataStructure, ValueT, RefT


MAX_LENGTH_DISPLAY_LIST = 10


class _EOL:
    pass


EOL = _EOL()


def hopn(node: LinkedList, n: int) -> LinkedList:
    assert n >= 0
    i = n
    while i > 0 and node.data is not EOL:  # type: ignore
        i -= 1
        node = node.tail  # type: ignore
    if i > 0:
        raise KeyError(n)
    return node


class LinkedList(DataStructure[int, ValueT]):

    always_ordered: bool = False
    data: Union[ValueT, _EOL]
    tail: Optional[LinkedList[ValueT]]

    def __iter__(self) -> Iterator[ValueT]:
        node = self
        while node.data is not EOL:  # type: ignore
            yield node.data  # type: ignore
            node = node.tail  # type: ignore

    def __init__(self, elems: Optional[Reversible[ValueT]] = None) -> None:
        next_node = None
        data: Union[ValueT, _EOL] = EOL
        if elems is not None:
            for e in chain(reversed(elems)):
                node = self._make_node(data, next_node)
                next_node = node
                data = e
        self.tail = next_node
        self.data = data

    @classmethod
    def _make_node(
            cls,
            elem: Union[ValueT, _EOL],
            tail: Optional[LinkedList[ValueT]],
    ) -> LinkedList[ValueT]:
        assert (tail is None and elem is EOL) or \
               (tail is not None and elem is not EOL)
        node = cls()
        node.data = elem
        node.tail = tail
        return node

    @property
    def length(self) -> int:
        ll = self
        i = 0
        while (ll := ll.tail) is not None:  # type: ignore
            i += 1
        return i

    def insert(self, val: ValueT) -> int:
        new_node = self._make_node(elem=self.data, tail=self.tail)
        self.data = val
        self.tail = new_node
        return 0

    def delete(self, pos: int) -> ValueT:
        node: LinkedList[ValueT] = hopn(self, pos)
        if node.data == EOL:
            raise KeyError(pos)
        ret = node.data
        node.data = node.tail.data  # type: ignore
        node.tail = node.tail.tail  # type: ignore
        return ret  # type: ignore

    def at(self, pos: int) -> ValueT:
        node = hopn(self, pos)
        if node.data == EOL:
            raise KeyError(pos)
        return node.data  # type: ignore

    def search(self, val: Any) -> List[int]:
        return [i for (i, e) in enumerate(self) if e == val]

    def __str__(self) -> str:
        node = self
        elems = []
        i = 0
        while node.data is not EOL and i < MAX_LENGTH_DISPLAY_LIST:
            elems.append(str(node.data))
            node = node.tail  # type: ignore
            i += 1
        if node.tail is not None and node.tail.data is not EOL:
            elems[-1] = "…"
        return f"LinkedList[{' → '.join(elems)}]"

