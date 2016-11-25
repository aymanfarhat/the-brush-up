from compress_string import compress_string

def test_compress_string():
    assert 'a3c1b1c5' == compress_string('aaacbccccc')
    assert 'aaacbc' == compress_string('aaacbc')
    assert 'acccbbc' == compress_string('acccbbc')
    assert 'a1c3b5c1' == compress_string('acccbbbbbc')
