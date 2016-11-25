from next_number_digits import next_number


def test_next_number():
    assert [2, 4, 6, 1] == next_number([2, 4, 6 , 0])
    assert [2, 4, 7, 0] == next_number([2, 4, 6 , 9])
    assert [2, 5, 0, 0] == next_number([2, 4, 9 , 9])
    assert [3, 0, 0, 0] == next_number([2, 9, 9 , 9])
    assert [1, 1] == next_number([1, 0])
    assert [8, 8, 9] == next_number([8, 8, 8])
    assert [8, 9, 0] == next_number([8, 8, 9])
    assert [1, 0] == next_number([9])
    assert [1, 0, 0] == next_number([9, 9])
    assert [1, 0, 0, 0] == next_number([9, 9, 9])
    assert [1] == next_number([0])
    assert [4, 0, 0, 0] == next_number([3, 9, 9, 9])
    assert [4, 1, 0, 0] == next_number([4, 0, 9, 9])
    assert [0, 0, 0, 1] == next_number([0, 0, 0, 0])
