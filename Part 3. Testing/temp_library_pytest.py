from temp_library import reverse_string
import pytest


def test_empty():
    assert reverse_string('') == ''


def test_odd_len():
    assert reverse_string('abc') == 'cba'


def test_wrong_type():
    with pytest.raises(TypeError):
        reverse_string(1)
    with pytest.raises(TypeError):
        reverse_string([1, 2, 3])

