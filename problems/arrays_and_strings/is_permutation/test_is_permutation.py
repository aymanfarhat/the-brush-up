from is_permutation import is_permutation


def test_is_permutation():
    assert is_permutation('abcd', 'badc')
    assert not is_permutation('abcdr', 'badc')
    assert is_permutation('abcdr', 'badcr')
    assert not is_permutation('abcdr', 'badccr')
