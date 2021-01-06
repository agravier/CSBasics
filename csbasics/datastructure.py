from __future__ import annotations

from abc import abstractmethod
from typing import Collection, Protocol, TypeVar, List, Iterator, Any, Final

RefT = TypeVar("RefT")
ValueT = TypeVar("ValueT")


class DataStructure(Collection, Protocol[RefT, ValueT]):

    always_ordered: bool

    @property
    @abstractmethod
    def length(self) -> int:
        """The number of elements contained in the data structure"""

    @abstractmethod
    def insert(self, val: ValueT) -> RefT:
        """Insert a value in the data structure.

        :param val: value to insert
        :return: a reference to the insertion location, only valid
            in the current state of the data structure.
        """

    @abstractmethod
    def delete(self, pos: RefT) -> ValueT:
        """Delete an element from the data structure at location pos. 
        
        :param pos: location to delete
        :return: the value that has been deleted.
        :raises: KeyError
        """

    @abstractmethod
    def at(self, pos: RefT) -> ValueT:
        """
        Access the value of the element at location pos.

        :return: The value at pos
        :raises: KeyError
        """

    @abstractmethod
    def search(self, val: Any) -> List[RefT]:
        """
        Find the locations of all elements with value val.

        :return: a vector of all found references.
        """

    @abstractmethod
    def __iter__(self) -> Iterator[ValueT]:
        ...

    def __len__(self) -> int:
        return self.length

    def __contains__(self, __x: object) -> bool:
        return not self.search(__x)
