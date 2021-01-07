from typing import List

import pytest

from csbasics.datastructure import DataStructure
from csbasics.linkedlist import LinkedList


def make_empty_linked_list() -> LinkedList:
    return LinkedList()


def is_sorted(l: List) -> bool:
    return all(l[i] <= l[i+1] for i in range(len(l)-1))


def verify_order_via_interface(ds: DataStructure[int, int]) -> None:
    assert is_sorted([i for i in ds])
    ds.insert(0)
    ds.insert(3)
    ds.insert(-2)
    ds.insert(1)
    ds.insert(0)
    assert is_sorted([i for i in ds])
    ds.delete(ds.search(1)[0])
    assert is_sorted([i for i in ds])


@pytest.mark.parametrize(
    "ds, always_ordered",
    [
        (make_empty_linked_list(), False)
    ]
)
def test_correctness_via_interface(
        ds: DataStructure[int, int],
        always_ordered: bool
) -> None:
    # Results when empty
    assert len(ds) == 0
    with pytest.raises(KeyError):
        ds.at(1)
    assert ds.search(1) == []
    with pytest.raises(KeyError):
        ds.delete(1)
    # Insert one 0
    first_inserted = ds.insert(0)
    assert type(first_inserted) == int
    assert ds.at(first_inserted) == 0
    assert len(ds) == 1
    assert ds.search(0) == [first_inserted]
    assert ds.search(1) == []
    with pytest.raises(KeyError):
        ds.delete(first_inserted + 1)
    # Delete it and run some tests
    assert ds.delete(first_inserted) == 0
    with pytest.raises(KeyError):
        ds.at(first_inserted)
    assert ds.search(0) == []
    assert len(ds) == 0
    # Insert 0, 3, -2
    inserted_zero = ds.insert(0)
    assert ds.at(inserted_zero) == 0
    inserted_three = ds.insert(3)
    assert ds.at(inserted_three) == 3
    inserted_minus_two = ds.insert(-2)
    assert ds.at(inserted_minus_two) == -2
    assert ds.search(-2) == [inserted_minus_two]
    assert type(inserted_zero) == int
    assert type(inserted_three) == int
    assert type(inserted_minus_two) == int
    assert len(ds) == 3
    assert ds.search(1) == []
    here = {ds.search(-2)[0], ds.search(0)[0], ds.search(3)[0]}
    assert len(here) == 3
    with pytest.raises(KeyError):
        not_here = 0
        while not_here in here:
            not_here += 1
        ds.delete(not_here)
    # Delete 3, check that 0 and -2 are left
    three = ds.delete(ds.search(3)[0])
    assert three == 3
    assert len(ds) == 2
    assert ds.at(ds.search(-2)[0]) == -2
    assert ds.at(ds.search(0)[0]) == 0
    assert ds.search(3) == []
    assert ds.at(ds.search(-2)[0]) == -2
    # Insert another -2, check that there are two of them
    inserted_second_minus_two = ds.insert(-2)
    assert len(ds.search(-2)) == 2
    assert len(ds.search(0)) == 1
    assert len(ds) == 3
    # Empty and run order tests
    if always_ordered:
        assert ds.always_ordered
        ds.delete(ds.search(-2)[0])
        ds.delete(ds.search(-2)[0])
        ds.delete(ds.search(0)[0])
        assert len(ds) == 0
        verify_order_via_interface(ds)

