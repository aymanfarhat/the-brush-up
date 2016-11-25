from unique_characters import unique_characters


def test_unique_characters():
    assert unique_characters('abcde')
    assert unique_characters('12345')
    assert not unique_characters('abcade')
    assert not unique_characters('abfi34iji')
