import pytest

from python_basics.flatten import flatten_nested


def test_normal():
    test = [1, [1, 2, 3]]
    assert flatten_nested(test) == [1, 1, 2, 3]


def test_list_tupple():
    test = [[1, 2], (3, 4)]
    assert flatten_nested(test) == [1, 2, 3, 4]


def test_empty_container():
    assert flatten_nested([]) == []


def test_string():
    assert flatten_nested(["string"]) == ["string"]


def test_dict():
    assert flatten_nested([{"a": 1}]) == [{"a": 1}]


def test_sequence():
    assert flatten_nested([1, 3, 2, 4]) == [1, 3, 2, 4]


def test_unchange():
    test = [1, [1, 2, 3]]
    flatten_nested(test)
    assert test == [1, [1, 2, 3]]


def test_invalid():
    with pytest.raises(TypeError):
        flatten_nested("string")


def test_nested():
    with pytest.raises(ValueError):
        test = [1]
        for x in range(4):
            test = [1, test]
        flatten_nested(test, max_depth=3)

def test_fix():
    assert flatten_nested([[1], [2]], max_depth=1) == [1,2]

def test_ids():
    a = [1,2]
    b = [a]
    a.extend(b)
    with pytest.raises(ValueError):
        flatten_nested(a)
